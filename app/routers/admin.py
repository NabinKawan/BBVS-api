from fastapi import APIRouter
from app.dbsync import service

admin_service = service.AdminService()

router = APIRouter(prefix='/api/admin', tags=['Admin'])


@router.get('/initialize')
def initialize_admin():
    admin_service.initialize_admin()
