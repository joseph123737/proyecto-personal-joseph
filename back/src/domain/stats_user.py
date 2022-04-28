import sqlite3


class UsersStats:
    def __init__(self, quizz_guest, quizz_miss, user_id, user_name):
        self.quizz_guest = quizz_guest
        self.quizz_miss = quizz_miss
        self.user_id = user_id
        self.user_name = user_name

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "quizz_guest": self.quizz_guest,
            "quizz_miss": self.quizz_miss,
            "user_name": self.user_name,
        }


class UserStatsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists users_stats (
                user_id varchar,
                quizz_guest integer,
                quizz_miss integer,
                user_name varchar
                
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def save_users_stats(self, user):
        sql = """insert into users_stats (user_id,quizz_guest,quizz_miss,user_name) values (
            :user_id, :quizz_guest, :quizz_miss, :user_name
         ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "user_id": user.user_id,
                "quizz_guest": user.quizz_guest,
                "quizz_miss": user.quizz_miss,
                "user_name": user.user_name,
            },
        )
        conn.commit()

    def update_user_quizzes(self, new_values, user_id):
        sql = """
        UPDATE users_stats SET quizz_guest = :quizz_guest,
                         quizz_miss = :quizz_miss
                     WHERE user_id = :user_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "quizz_guest": new_values["quizz_guest"],
                "quizz_miss": new_values["quizz_miss"],
                "user_id": user_id,
            },
        )
        conn.commit()

    def get_user_stats_by_id(self, user_id):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM users_stats WHERE user_id =?""", (user_id,))
        data = cursor.fetchone()
        user = UsersStats(
            user_id=data["user_id"],
            quizz_guest=data["quizz_guest"],
            quizz_miss=data["quizz_miss"],
            user_name=data["user_name"],
        )
        return user
