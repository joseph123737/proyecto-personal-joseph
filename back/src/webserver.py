from flask import Flask, request
from flask_cors import CORS
from src.domain.stats_user import UsersStats
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

    @app.route("/api/users/login-users/<id>", methods=["GET"])
    def get_user_by_id(id):
        data = repositories["users"].get_user_by_id(id)
        user = object_to_json(data)
        return user

    @app.route("/api/users/users-stats/<id>", methods=["GET"])
    def get_stats_user_by_id(id):
        data = repositories["users_stats"].get_user_stats_by_id(id)
        user_stats = object_to_json(data)
        return user_stats

    @app.route("/api/users/users-stats/change-stats/<id>", methods=["PUT"])
    def update_user(id):
        new_stats = {}
        body = request.json
        print(body)
        data = repositories["users_stats"].get_user_stats_by_id(id)
        new_stats["quizz_guest"] = body["quizz_guest"] + data.quizz_guest
        new_stats["quizz_miss"] = body["quizz_miss"] + data.quizz_miss
        repositories["users_stats"].update_user_quizzes(new_stats, id)
        return "", 200

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_user_by_id(body["user_id"])
        if user.password != body["password"] or user == None:
            return "", 401
        else:
            return object_to_json(user)

    return app
