import pymysql
class DB:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        # self.database = database
        self.connection = None

    def connect(self):
        """
        连接数据库
        """
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            # database=self.database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def close(self):
        """
        关闭数据库连接
        """
        if self.connection:
            self.connection.close()

    def query(self, sql, params=None):
        """
        执行查询语句
        """
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute(self, sql, params=None):
        """
        执行增删改语句
        """
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute(sql, params)
        self.connection.commit()
        cursor.close()

# honmaKr-stage-数据库地址
dbProd = DB(
    host="172.20.250.141",
    port=4000,
    user="develop",
    password="Password@123"
)

# honmaKr-prod-数据库地址
dbStage = DB(
    host="172.20.250.150",
    port=4000,
    user="develop",
    password="Password@123"
)

