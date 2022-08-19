from email.policy import default
from app.db import db
from pony.orm import PrimaryKey, Required, Optional


class Candidate(db.Entity):
    __table__ = "candidate table"

    id = PrimaryKey(str)
    first_name = Required(str)
    middle_name = Optional(str, default="")
    last_name = Required(str)
    post = Required(str)
    image = Required(str)


class Voter(db.Entity):
    __table__ = "voter table"

    id = PrimaryKey(str)
    first_name = Required(str)
    middle_name = Optional(str, default="")
    last_name = Required(str)
    image = Required(str)


class Admin(db.Entity):
    __table__ = "admin table"

    id = PrimaryKey(str)
    first_name = Required(str)
    middle_name = Optional(str, default="")
    last_name = Required(str)
    image = Required(str)


class AdminCredential(db.Entity):
    __table__ = "admin_credential table"

    id = PrimaryKey(str)
    password = Required(str)
