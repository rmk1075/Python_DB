import pymysql

connection = None
cursor = None
query = ""

# docker-compose로 database container를 실행 시에 host url로 localhost를 주는 것이 아닌 해당 database service의 이름을 주어야 한다.
# 이 예제에서는 db를 이름으로 사용한다.
connection = pymysql.connect(host='db', port=3306, user='init', password='init123!!', db='project', charset='utf8')
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
