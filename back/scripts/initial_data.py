import sys

sys.path.insert(0, "")
from src.domain.login_users import Users, UsersRepository
from src.domain.stats_user import UsersStats, UserStatsRepository
from src.domain.quizzes import Quizzes, QuizzesRepository


def main():

    database_path = "data/database.db"

    users_repository = UsersRepository(database_path)

    users_repository.save(Users("01", "dos", "joseph"))

    quizzes_repository = QuizzesRepository(database_path)

    quizzes_repository.save_quizz(
        Quizzes(
            id_quizz="03",
            quizz_name="tres(preguntas LOL)",
            quizzes=[
                {
                    "id": 1,
                    "question_quizz": "Que tipo de daño ignora la armadura",
                    "answer_01": {
                        "title": "Fisico",
                        "is_correct": False,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "Mágico",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "Verdaero",
                        "is_correct": True,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "Teemo",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
                {
                    "id": 2,
                    "question_quizz": "Actualmen quien esta considerado el  mejor jugador de LOL a nivel profesional",
                    "answer_01": {
                        "title": "Faker",
                        "is_correct": True,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "Darkvapor",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "Inorks",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "Citric",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
                {
                    "id": 3,
                    "question_quizz": "Quien de los siguientes personajes pertenece a Noxus",
                    "answer_01": {
                        "title": "Teemo",
                        "is_correct": False,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "Irelia",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "Yasuo",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "Darius",
                        "is_correct": True,
                        "id_button": "4",
                    },
                },
            ],
        )
    )
    quizzes_repository.save_quizz(
        Quizzes(
            id_quizz="01",
            quizz_name="uno",
            quizzes=[
                {
                    "id": 1,
                    "question_quizz": "que hace la siguiente list comprehension :  [( i) for i in range (5) ]",
                    "answer_01": {
                        "title": "hace un for del 1 al 5",
                        "is_correct": True,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "la verdad que no se",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "print los nombre de una lista",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "splitea una string",
                        "is_correct": False,
                        "id_button": "4",
                    },
                }
            ],
        )
    )
    quizzes_repository.save_quizz(
        Quizzes(
            id_quizz="02",
            quizz_name="Dos",
            quizzes=[
                {
                    "id": 1,
                    "question_quizz": "Cualde los siguientes lenguajes no es una de alto nivel",
                    "answer_01": {
                        "title": "Compilacion",
                        "is_correct": False,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "Maquina",
                        "is_correct": True,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "Interpretado",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "C++",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
                {
                    "id": 2,
                    "question_quizz": "¿Cual es el lenguaje de mas bajo nivel de los siguentes?",
                    "answer_01": {
                        "title": "Python",
                        "is_correct": False,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "Emsablador",
                        "is_correct": True,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "JavaScript",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "PHP",
                        "is_correct": False,
                        "id_button": "4",
                    },
                },
            ],
        )
    )
    users_stast_repository = UserStatsRepository(database_path)
    users_stast_repository.save_users_stats(UsersStats(12, 2, "01", "joseph"))


if __name__ == "__main__":
    main()
