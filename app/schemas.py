from pydantic import BaseModel


# candidate


class CandidateBase(BaseModel):
    candidate_id: str
    first_name: str
    middle_name: str
    last_name: str
    post: str
    image: str
    logo: str
    # class Config:
    #     orm_mode=True


class CandidateCreate(CandidateBase):
    pass


class CandidateRead(CandidateBase):
    pass


# voter


class VoterBase(BaseModel):
    voter_id: str
    first_name: str
    middle_name: str
    last_name: str
    image: str
    # class Config:
    #     orm_mode=True


class VoterCreate(VoterBase):
    pass


class VoterLogin(BaseModel):
    voter_id: str
    password: str


# Admin

class AdminLogin(BaseModel):
    admin_id: str
    password: str
