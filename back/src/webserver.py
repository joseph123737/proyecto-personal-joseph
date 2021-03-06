from flask import Flask, request
from flask_cors import CORS
from src.domain.stats_user import UsersStats
from src.domain.login_users import Users, UsersRepository
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

    @app.route("/api/quizz/add-quizz", methods=["POST"])
    def post_new_quizz():
        body = request.json
        quizz_to_save = Quizzes(
            id_quizz=body["id_quizz"],
            quizz_name=body["quizz_name"],
            quizzes=body["quizzes"],
        )
        repositories["quizzes"].save_quizz(quizz_to_save)
        return "", 200

    @app.route("/api/users/login-users/<id>", methods=["GET"])
    def get_user_by_id(id):
        data = repositories["users"].get_user_by_id(id)
        user = object_to_json(data)
        return user

    @app.route("/api/users/login-users/add-new-user", methods=["POST"])
    def register_new_users():
        body = request.json
        new_user = Users(
            user_id=body["user_id"],
            password=body["password"],
            user_name=body["user_name"],
        )
        response_of_user_is_ok = repositories["users"].register_new_user(new_user)
        if response_of_user_is_ok == 409:
            return "", 409
        else:
            return "", 200

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
        user = repositories["users"].get_user_by_name(body["user_name"])
        if user == 404:
            return "", 404
        if user == 409:
            return "", 409
        if user.password != body["password"] or user == None:
            return "", 401
        else:
            return object_to_json(user)

    return app
