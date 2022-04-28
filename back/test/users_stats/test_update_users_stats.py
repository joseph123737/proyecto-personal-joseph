from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.stats_user import UsersStats, UserStatsRepository


def test_check_status_code_is_200():
    users_repository = UserStatsRepository(temp_file())
    app = create_app(repositories={"users_stats": users_repository})
    client = app.test_client()
    user = UsersStats(12, 2, "1", "Valentina")
    users_repository.save_users_stats(user)
    body = {
        "quizz_guest": 13,
        "quizz_miss": 45,
    }
    response = client.put("/api/users/users-stats/change-stats/1", json=body)
    assert response.status_code == 200


def test_check_if_update_correct():
    users_repository = UserStatsRepository(temp_file())
    app = create_app(repositories={"users_stats": users_repository})
    client = app.test_client()
    user = UsersStats(12, 2, "1", "Valentina")
    users_repository.save_users_stats(user)
    body = {
        "quizz_guest": 2,
        "quizz_miss": 5,
    }
    response_of_put = client.put("/api/users/users-stats/change-stats/1", json=body)
    assert response_of_put.status_code == 200
    response_of_get = client.get("/api/users/users-stats/1")
    assert response_of_get.json == {
        "quizz_guest": 14,
        "quizz_miss": 7,
        "user_id": "1",
        "user_name": "Valentina",
    }
