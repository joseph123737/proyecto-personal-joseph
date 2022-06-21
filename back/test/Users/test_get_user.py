from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.login_users import Users, UsersRepository


def test_should_get_a_correct_user():
    users_repository = UsersRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()
    user_02 = Users("02", "patata", "zino")
    user_01 = Users("01", "mata_bebes", "Valentina")
    users_repository.save(user_02)
    users_repository.save(user_01)
    body = {"user_name": "Valentina", "password": "mata_bebes"}
    response = client.post("/auth/login", json=body)
    assert response.json == {
        "user_id": "01",
        "user_name": "Valentina",
        "password": "mata_bebes",
    }
