from pony.orm import db_session
from fastapi import HTTPException
from app.dbsync.sql import SQL_ADD_ADMIN, SQL_ADD_ADMIN_CREDENTIAL, SQL_ADD_CANDIDATE, SQL_ADD_VOTER, SQL_CANDIDATES, SQL_DELETE_CANDIDATE, SQL_DELETE_VOTER, SQL_SINGLE_ADMIN_CREDENTIAL_BY_ID, SQL_SINGLE_VOTER_BY_ID, SQL_UPDATE_CANDIDATE, SQL_UPDATE_VOTER, SQL_VOTERS
from app.schemas import CandidateCreate, VoterCreate
from app.models import Candidate
from app.db import db
from pony.orm.dbapiprovider import IntegrityError


class CandidateService:
    @db_session
    def create_candidate(self, candidate_ob: CandidateCreate):
        sql = SQL_ADD_CANDIDATE.format(id=candidate_ob.id,
                                       first_name=candidate_ob.first_name,
                                       middle_name=candidate_ob.middle_name,
                                       last_name=candidate_ob.last_name,
                                       post=candidate_ob.post,
                                       image=candidate_ob.image)
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="Candidate already registered")

    @db_session
    def get_all_candidates(self):
        sql = SQL_CANDIDATES
        cursor = db.execute(sql)

        candidates = []
        for row in cursor.fetchall():
            id, first_name, middle_name, last_name, post, image = row
            document = {
                'id': id,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'post': post,
                'image': image
            }

            candidates.append(document)

        return candidates

    @db_session
    def delete_candidate(self, id):
        sql = SQL_DELETE_CANDIDATE.format(id=id)

        db.execute(sql)

    @db_session
    def update_candidate(self, candidate_ob: CandidateCreate):
        sql = SQL_UPDATE_CANDIDATE.format(
            id=candidate_ob.id,
            first_name=candidate_ob.first_name,
            middle_name=candidate_ob.middle_name,
            last_name=candidate_ob.last_name,
            post=candidate_ob.post,
            image=candidate_ob.image)

        db.execute(sql)


class VoterService:

    @db_session
    def get_all_voters(self):
        sql = SQL_VOTERS
        cursor = db.execute(sql)

        voters = []
        for row in cursor.fetchall():
            id, first_name, middle_name, last_name, image = row
            document = {
                'id': id,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'image': image
            }

            voters.append(document)

        return voters

    @db_session
    def get_voter_by_id(self, id):
        sql = SQL_SINGLE_VOTER_BY_ID.format(id=id)
        cursor = db.execute(sql)
        voters = []
        for row in cursor.fetchall():
            id, first_name, middle_name, last_name, image = row
            document = {
                'id': id,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'image': image
            }

            voters.append(document)

        return voters

    @db_session
    def create_voter(self, voter_ob: VoterCreate):
        sql = SQL_ADD_VOTER.format(id=voter_ob.id,
                                   first_name=voter_ob.first_name,
                                   middle_name=voter_ob.middle_name,
                                   last_name=voter_ob.last_name,
                                   image=voter_ob.image)
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="Voter already registered")

    @db_session
    def delete_voter(self, id):
        sql = SQL_DELETE_VOTER.format(id=id)

        db.execute(sql)

    @db_session
    def update_voter(self, voter_ob: VoterCreate):
        sql = SQL_UPDATE_VOTER.format(
            id=voter_ob.id,
            first_name=voter_ob.first_name,
            middle_name=voter_ob.middle_name,
            last_name=voter_ob.last_name,
            image=voter_ob.image)

        db.execute(sql)


class AdminService:

    @db_session
    def initialize_admin(self):
        sql1 = SQL_ADD_ADMIN
        sql2 = SQL_ADD_ADMIN_CREDENTIAL

        try:
            db.execute(sql1)
            db.execute(sql2)

        except:
            print("already exist")

    @db_session
    def get_admin_credential_by_id(self, id):
        sql = SQL_SINGLE_ADMIN_CREDENTIAL_BY_ID.format(id=id)
        cursor = db.execute(sql)
        admin_credential = {}
        for row in cursor.fetchall():
            id, password = row
            document = {
                'id': id,
                'password': password
            }

            admin_credential = document

        return admin_credential
