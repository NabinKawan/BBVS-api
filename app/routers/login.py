from fastapi import APIRouter, Depends, HTTPException
from app.auth.jwt_handler import sign_jwt
from app.service import very_voter_login, very_admin_login
from app.schemas import AdminLogin, VoterLogin

router = APIRouter(prefix="/api/login", tags=['Login'])


@router.post('')
def voter_login(login_credentials: VoterLogin):
    if very_voter_login(login_credentials):
        return sign_jwt(login_credentials.voter_id.upper())
    else:
        raise HTTPException(
            status_code=401, detail="Invalid credentials")


@router.post('/adminLogin')
def admin_login(login_credentials: AdminLogin):
    if very_admin_login(login_credentials):
        return sign_jwt(login_credentials.admin_id, end_time_ms=7*24*60*60*1000)
    else:
        raise HTTPException(
            status_code=401, detail="Invalid credentials")
