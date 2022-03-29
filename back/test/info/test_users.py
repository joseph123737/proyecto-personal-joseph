from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.users import Users

""" 
def test_should_return_info_in_database():
    info_repository = InfoRepository(temp_file())
    app = create_app(repositories={"info": info_repository})
    client = app.test_client()

    info_repository.save(
        Info(
            app_name="test application",
        )
    )

    response = client.get("/api/info")
    assert response.json == {
        "app_name": "test application",
    }
 """


def test_if_constructor_is_correct():
    user = Users(12, 2, "1", "Valentina")
    assert "1" == user.user_id
    assert 12 == user.quizz_guest
    assert 2 == user.quizz_miss
    assert "Valentina" == user.user_name
