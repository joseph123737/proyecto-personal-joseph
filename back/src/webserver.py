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
    def get_all_quizzes():
        data = repositories["quizzes"].get_all_quizzes()
        return object_to_json(data)

    @app.route("/api/quizz/<id>", methods=["GET"])
    def get_quizz_by_id(id):
        data = repositories["quizzes"].get_quizz_by_id(id)
        quizz = object_to_json(data)
        return quizz

    @app.route("/api/login-users/<id>", methods=["GET"])
    def get_user_by_id(id):
        data = repositories["users"].get_user_by_id(id)
        user = object_to_json(data)
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
