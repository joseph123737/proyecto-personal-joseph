from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.login_users import Users

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
    user = Users("01", "mata_bebes", "Valentina")
    assert "01" == user.user_id
    assert "Valentina" == user.user_name
    assert "mata_bebes" == user.password
