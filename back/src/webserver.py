from flask import Flask, request
from flask_cors import CORS
from src.domain.stats_user import UserQuizzes
from src.domain.login_users import Users
from src.domain.quizzes import Quizzes
from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/quizz", methods=["GET"])
    def quizz_get():
        quizz = {
            "id_quizz": "01",
            "quizz_name": "prueba uno",
            "quizz": [
                {
                    "id": 1,
                    "question_quizz": "que hace la siguiente list comprehension :  [( i) for i in range (5) ]",
                    "answer_01": {
                        "title": "hace un for del 1 al 5",
                        "is_correct": True,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "la verdad que no se",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "print los nombre de una lista",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "splitea una string",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
                {
                    "id": 2,
                    "question_quizz": "que tipo de dato es este : 01  ",
                    "answer_01": {
                        "title": "Integer",
                        "is_correct": True,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "string",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "objeto",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "clase",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
            ],
        }
        return quizz

    @app.route("/api/quizz/<id>", methods=["GET"])
    def get_quizz_by_id(id):
        data = repositories["quizzes"].get_quizz_by_id(id)
        quizz = object_to_json(data)
        print("----------")
        return quizz

    @app.route("/api/login-users/<id>", methods=["GET"])
    def get_user_by_id(id):
        data = repositories["users"].get_user_by_id(id)
        user = object_to_json(data)
        print("----------")
        return user

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_user_by_id(body["user_id"])
        if user.password != body["password"] or user == None:
            return "", 401
        else:
            return object_to_json(user)

    return app
