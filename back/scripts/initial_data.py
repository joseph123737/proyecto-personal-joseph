import sys

sys.path.insert(0, "")
from src.domain.login_users import Users, UsersRepository


def main():

    database_path = "data/database.db"

    users_repository = UsersRepository(database_path)

    users_repository.save(Users("01", "mata_bebes", "Valentina"))


if __name__ == "__main__":
    main()
