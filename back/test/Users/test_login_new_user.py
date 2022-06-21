from itsdangerous import json
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.login_users import Users, UsersRepository


def test_should_save_a_new_user_correctly():
    users_repository = UsersRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()
    new_user = {"user_name": "okami", "user_id": "02", "password": "Tucanrosa32"}
    response = client.post("/api/users/login-users/add-new-user", json=new_user)

    assert response.status_code == 200
    body = {"user_name": "okami", "password": "Tucanrosa32"}
    response_get = client.post("/auth/login", json=body)

    assert response_get.json == {
        "user_name": "okami",
        "user_id": "02",
        "password": "Tucanrosa32",
    }
