from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.login_users import Users, UsersRepository


def test_should_get_a_correct_user():
    users_repository = UsersRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()
    user = Users("01", "mata_bebes", "Valentina")
    users_repository.save(user)
    body = {"user_id": "01"}
    response = client.get("/api/users/login-users/01", json=body)
    assert response.json == {
        "user_id": "01",
        "user_name": "Valentina",
        "password": "mata_bebes",
    }
