import sqlite3
from src.domain.stats_user import UserStatsRepository, UsersStats


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
                user_id varchar  PRIMARY KEY NOT NULL ,
                password varchar,
                user_name varchar UNIQUE 
                
                
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
        conn.close()

    def get_user_by_name(self, user_name):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM users WHERE user_name =?""", (user_name,))
        data = cursor.fetchone()
        user = Users(
            user_id=data["user_id"],
            user_name=data["user_name"],
            password=data["password"],
        )
        return user

    def register_new_user(self, body):
        conn = self.create_conn()
        cursor = conn.cursor()
        sql = """insert into users (user_id,password,user_name) values (
            :user_id, :password, :user_name
         ) 
         """
        params = {
            "user_id": body.user_id,
            "password": body.password,
            "user_name": body.user_name,
        }
        cursor.execute(sql, params)
        conn.commit()
        conn.close()
        new_user_stats = UsersStats(
            user_id=body.user_id, quizz_guest=0, quizz_miss=0, user_name=body.user_name
        )
        stats_repository = UserStatsRepository("data/database.db")
        stats_repository.save_users_stats(new_user_stats)
