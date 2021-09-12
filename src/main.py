import sqlalchemy as db

name = 'init'
password = 'init123!!'
url = 'db' # database service name in docker-compose
port = '3306'
database = 'project'
conn = f'mysql+pymysql://{name}:{password}@{url}:{port}/{database}'

engine = db.create_engine(conn)
connection = engine.connect()
metadata = db.MetaData()

table_name = 'test'
table = db.Table(table_name, metadata, autoload=True, autoload_with=engine)

print(table.columns.keys())