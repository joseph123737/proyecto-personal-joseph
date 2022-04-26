import sqlite3


class Users:
    def __init__(self, user_id, password, user_name):
        self.user_id = user_id
        self.password = password
        self.user_name = user_name

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "password": self.password,
            "user_name": self.user_name,
        }


class UsersRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def init_tables(self):
        sql = """
            create table if not exists users (
                user_id varchar,
                password varchar,
                user_name varchar
                
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def save(self, user):
        sql = """insert into users (user_id,password,user_name) values (
            :user_id, :password, :user_name
         ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "user_id": user.user_id,
                "password": user.password,
                "user_name": user.user_name,
            },
        )
        conn.commit()

    def get_user_by_id(self, user_id):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM users WHERE user_id =?""", (user_id,))
        data = cursor.fetchone()
        user = Users(
            user_id=data["user_id"],
            user_name=data["user_name"],
            password=data["password"],
        )
        return user
