from fastapi import APIRouter, Depends
from app.auth.jwt_bearer import JWTBearer
from app.dbsync import service

admin_service = service.AdminService()

router = APIRouter(prefix='/api/admin', tags=['Admin'])


@router.get('/initialize')
def initialize_admin():
    admin_service.initialize_admin()

@router.get('/{admin_id}',dependencies=[Depends(JWTBearer())])
def get_admin(admin_id:str):
    admin=admin_service.get_admin_by_id(admin_id)
    return admin

@router.get('/adminCredential/{admin_id}',dependencies=[Depends(JWTBearer())])
def get_admin(admin_id:str):
    admin_credential=admin_service.get_admin_credential_by_id(admin_id)
    return admin_credential

