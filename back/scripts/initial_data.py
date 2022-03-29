import sys

sys.path.insert(0, "")
from src.domain.users import Users, UsersRepository


def main():

    database_path = "data/database.db"

    users_repository = UsersRepository(database_path)

    users_repository.save(Users(app_name="f5-seed-app"))


if __name__ == "__main__":
    main()
