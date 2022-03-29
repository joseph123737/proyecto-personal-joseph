from urllib import response
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.users import Users, UsersRepository


def test_check_if_update_correct():
    users_repository = UsersRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()
    user = Users(12, 2, "1", "Valentina")
    users_repository.save(user)
    body = {
        "user_id": "1",
        "quizz_guest": 13,
        "quizz_miss": 45,
        "user_name": " Valentina",
    }
    response = client.put("/api/users", json=body)
    assert response.status_code == 200
