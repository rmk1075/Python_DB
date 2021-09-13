from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

name = 'init'
password = 'init123!!'
url = 'db' # database service name in docker-compose
port = '3306'
database = 'project'
setting = f'mysql+pymysql://{name}:{password}@{url}:{port}/{database}'

engine = create_engine(setting)
Session = sessionmaker(bind=engine)