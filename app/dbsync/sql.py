SQL_CANDIDATES = 'select * from "Candidate"'

SQL_ADD_CANDIDATE = """
INSERT INTO "Candidate" (id,first_name,middle_name,last_name,post,image)
VALUES ('{id}','{first_name}','{middle_name}','{last_name}','{post}','{image}');
"""

SQL_DELETE_CANDIDATE = """
delete from "Candidate" where id='{id}'
"""

SQL_UPDATE_CANDIDATE = """
update "Candidate" 
set first_name='{first_name}', middle_name='{middle_name}', last_name='{last_name}', post='{post}', image='{image}'
where id='{id}'
"""

SQL_VOTERS = 'select * from "Voter"'

SQL_SINGLE_VOTER_BY_ID = """
select * from "Voter" where id='{id}'
"""

SQL_ADD_VOTER = """
INSERT INTO "Voter" (id,first_name,middle_name,last_name,image)
VALUES ('{id}','{first_name}','{middle_name}','{last_name}','{image}');
"""

SQL_DELETE_VOTER = """
delete from "Voter" where id='{id}'
"""

SQL_UPDATE_VOTER = """
update "Voter" 
set first_name='{first_name}', middle_name='{middle_name}', last_name='{last_name}',image='{image}'
where id='{id}'
"""
SQL_SINGLE_ADMIN_CREDENTIAL_BY_ID = """
select * from "AdminCredential" where id='{id}'
"""

SQL_ADD_ADMIN = """
INSERT INTO "Candidate" (id,first_name,middle_name,last_name,image)
VALUES ('admin','Nabin','','Kawan','   static/images/d07907be811379588986.jpeg');
"""

SQL_ADD_ADMIN_CREDENTIAL = """
INSERT INTO "Candidate" (id,password)
VALUES ('admin','admin');
"""
