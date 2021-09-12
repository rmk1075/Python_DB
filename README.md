# Python_DB

python programming with database

## Development environment

python을 사용하여 백엔드 DB 연결 구현을 진행하기 위해서 ubuntu18.04 이미지에 python 개발 환경을 구축한 Dockerfile과 mariadb 이미지를 사용하여 docker container 개발환경 구축

```Dockerfile
version: "3.9"
services:
  # python backend service
  python_backend:
    # docker build
    build:
      context: .
      dockerfile: ./Dockerfile
    # docker run -i
    stdin_open: true
    # docker run -t
    tty: true
    # build from the Dockerfile in current directory
    build: .
    # mount the project directory (./) on the host to /usr/app inside the container
    volumes:
      - ../../PYTHON_DB:/usr/app
    # set environment variables
    environment:
      # set encoding C.UTF-8
      LC_ALL: C.UTF-8
    # start after db container started
    depends_on:
      - db
  # maria db service
  db:
    image: mariadb
    restart: always
    ports:
      - 3306:3306
    # mount database data storage
    volumes:
      - ../db/data:/var/lib/mysql
    # environment variables
    env_file: ../db/.env
    environment:
      TZ: Asia/Seoul
```

## DB Connection Test

python backend 컨테이너에서 db 컨테이너에 커넥션 생성 후 test 테이블을 생성하는 소스 코드.

mariaDB는 MySQL 기반이기 때문에 파이썬에서 MySQL DB를 사용할 때 사용되는 모듈인 pymysql을 사용하여서 DB 커넥션을 수행한다.

소스를 작성할 때 주의해야할 사항은 host이다. localhost나 DB가 설치되어 있는 곳의 주소와 같이 url을 적는 것이 아니라 docker-compose에서 service로 실행한 service name을 사용해야 한다.

이 예제에서는 'db'라는 이름으로 db 서비스가 수행되기 때문에 'db'라는 이름을 host로 입력한다.

```python
import pymysql

connection = None
cursor = None
query = ""

# docker-compose로 database container를 실행 시에 host url로 localhost를 주는 것이 아닌 해당 database service의 이름을 주어야 한다.
# 이 예제에서는 db를 이름으로 사용한다.
connection = pymysql.connect(host='db', port=3306, user=id, password=password, db=database, charset='utf8')
cursor = connection.cursor()

sql = """
        CREATE TABLE IF NOT EXISTS
            test (
                id      char(4),
                name    char(10)
            )
    """

cursor.execute(sql)
connection.commit()
connection.close()

```
