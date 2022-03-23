from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/quizz", methods=["GET"])
    def info_get():
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
                        "title": "esta no",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "esta tampoco",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "empieza a leer de nuevo",
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
                        "title": "esta no",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "esta tampoco",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "empieza a leer de nuevo",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
                {
                    "id": 3,
                    "question_quizz": "esto",
                    "answer_01": {"title": "si", "is_correct": True, "id_button": "1"},
                    "answer_02": {
                        "title": "esta no",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "esta tampoco",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "empieza a leer de nuevo",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
                {
                    "id": 4,
                    "question_quizz": "funciona",
                    "answer_01": {"title": "si", "is_correct": True, "id_button": "1"},
                    "answer_02": {
                        "title": "esta no",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "esta tampoco",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "empieza a leer de nuevo",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
            ],
        }
        return quizz

    return app
