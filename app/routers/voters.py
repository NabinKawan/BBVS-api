from fastapi import APIRouter, HTTPException, Depends
from app.auth.jwt_bearer import JWTBearer
import app.dbsync.service as service
from app.schemas import VoterCreate


router = APIRouter(prefix="/api/voters",
                   tags=["Voters"], dependencies=[Depends(JWTBearer())])

voter_service = service.VoterService()


def generate_voter_response(voters):
    total_items = len(voters)
    return {
        'total_items': total_items,
        'content': voters}


@router.get('')
def get_all_voters():
    all_voters = voter_service.get_all_voters()
    response = generate_voter_response(voters=all_voters)
    return response


@router.get("/{id}")
def get_voter_by_id(id: str):
    single_voter = voter_service.get_voter_by_id(id)
    response = generate_voter_response(single_voter)
    return response


@router.post("/addVoter")
def add_voter(voter_ob: VoterCreate):
    voter_service.create_voter(voter_ob=voter_ob)


@router.put("/updateVoter")
def update_voter(voter_ob: VoterCreate):
    voter_service.update_voter(voter_ob=voter_ob)


@router.delete("/deleteVoter/{id}")
def delete_voter(id: str):
    voter_service.delete_voter(id=id)
