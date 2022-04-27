from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.login_users import Users, UsersRepository


def setup():
    users_repository = UsersRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()
    user = Users("01", "mata_bebes", "Valentina")
    user_2 = Users("02", "patata", "alfredo")
    users_repository.save(user)
    users_repository.save(user_2)

    return client


def test_should_return_correct_status_code():
    client = setup()
    body = {"user_id": "02", "password": "patata"}
    response = client.post("/auth/login", json=body)
    assert response.status_code == 200


def test_should_get_a_correct_user():
    client = setup()
    body = {"user_id": "02", "password": "patata"}
    response = client.post("/auth/login", json=body)
    assert response.status_code == 200
    assert response.json == {
        "user_name": "alfredo",
        "user_id": "02",
        "password": "patata",
    }


def test_should_return_401_when_the_password_is_incorrect():
    client = setup()
    body = {"user_id": "02", "password": "pataa"}
    response = client.post("/auth/login", json=body)
    assert response.status_code == 401
    assert response.json == None
