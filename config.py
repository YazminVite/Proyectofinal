import web

db_host = 'localhost'
db_name = 'final'
db_user = 'admin'
db_pw = 'admin'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )