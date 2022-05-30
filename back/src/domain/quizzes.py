import sqlite3
import json


class Quizzes:
    def __init__(self, id_quizz, quizz_name, quizzes):
        self.id_quizz = id_quizz
        self.quizz_name = quizz_name
        self.quizzes = quizzes

    def to_dict(self):
        return {
            "id_quizz": self.id_quizz,
            "quizz_name": self.quizz_name,
            "quizzes": self.quizzes,
        }


class QuizzesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def init_tables(self):
        sql = """
            create table if not exists quizzes (
                id_quizz varchar,
                quizz_name varchar,
                quizzes varchar,
                user_id varchar,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
                ON DELETE  CASCADE
                
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

    def save_quizz(self, quizz):
        sql = """insert into quizzes (id_quizz,quizz_name,quizzes) values (
            :id_quizz, :quizz_name, :quizzes
         ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id_quizz": quizz.id_quizz,
                "quizz_name": quizz.quizz_name,
                "quizzes": json.dumps(quizz.quizzes),
            },
        )
        conn.commit()

    def get_quizz_by_id(self, quizz_id):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM quizzes WHERE id_quizz =?""", (quizz_id,))
        data = cursor.fetchone()
        quizz = Quizzes(
            id_quizz=data["id_quizz"],
            quizz_name=data["quizz_name"],
            quizzes=json.loads(data["quizzes"]),
        )
        return quizz

    def get_all_quizzes(self):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM quizzes""")
        data = cursor.fetchall()
        quizzes_list = []
        for item in data:
            quizz = Quizzes(
                id_quizz=item["id_quizz"],
                quizz_name=item["quizz_name"],
                quizzes=json.loads(item["quizzes"]),
            )
            quizzes_list.append(quizz)
        return quizzes_list
