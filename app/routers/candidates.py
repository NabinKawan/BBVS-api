from fastapi import APIRouter, HTTPException, Depends
from app.auth.jwt_bearer import JWTBearer
import app.dbsync.service as service
from app.schemas import CandidateCreate

router = APIRouter(prefix="/api/candidates",
                   tags=["Candidates"], dependencies=[Depends(JWTBearer())])

candidate_service = service.CandidateService()


def generate_candidate_response(candidates):
    total_items = len(candidates)
    posts = set([e['post'] for e in candidates])
    return {
        'total_items': total_items,
        'posts': posts,
        'content': candidates}


@router.get('')
def get_all_candidates():
    all_candidates = candidate_service.get_all_candidates()
    response = generate_candidate_response(all_candidates)
    return response


@router.post("/addCandidate")
def add_candidate(candidate_ob: CandidateCreate):
    candidate_service.create_candidate(candidate_ob=candidate_ob)


@router.put("/updateCandidate")
def update_candidate(candidate_ob: CandidateCreate):
    candidate_service.update_candidate(candidate_ob=candidate_ob)


@router.delete("/deleteCandidate/{id}")
def delete_candidate(id: str):
    candidate_service.delete_candidate(id=id)
