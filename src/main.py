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

print(f'table columns - {table.columns.keys()}\n')

# select * from table
query = db.select([table])
print(f'query: {query}\n')

# execute query
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

print(result_set)
