import web

db_host = 'l7cup2om0gngra77.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'lw8p3gekg3hgd6p6'
db_user = 'u5deyv5rb075qenk'
db_pw = 'ub7nhidylwbedo7q'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
