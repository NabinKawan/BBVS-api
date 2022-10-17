from app.schemas import VoterLogin, AdminLogin
from app.dbsync.service import AdminService, VoterService

voter_service = VoterService()
admin_service = AdminService()


def very_voter_login(login_credentials: VoterLogin):
    voter_id = login_credentials.voter_id.upper()
    single_voter = voter_service.get_voter_by_id(voter_id)
    if len(single_voter) != 0:
        voter = single_voter[0]
        if voter['voter_id'] == login_credentials.password.upper():
            return True
        else:
            return False
    else:
        return False


def very_admin_login(login_credentials: AdminLogin):
    print(login_credentials)
    admin_id = login_credentials.admin_id
    admin = admin_service.get_admin_credential_by_id(admin_id)
    print(admin)
    if admin:
        if admin['password'] == login_credentials.password:
            return True
        else:
            return False
    else:
        return False
