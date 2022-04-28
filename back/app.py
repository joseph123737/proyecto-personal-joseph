import sqlite3
from src.domain.quizzes import QuizzesRepository
from src.webserver import create_app
from src.domain.login_users import UsersRepository


database_path = "data/database.db"

repositories = {
    "users": UsersRepository(database_path),
    "quizzes": QuizzesRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
