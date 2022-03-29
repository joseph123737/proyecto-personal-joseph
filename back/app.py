import sqlite3
from src.webserver import create_app
from domain.users import UsersRepository, Users


database_path = "data/database.db"

repositories = {"users": UsersRepository(database_path)}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
