import sys

sys.path.insert(0, "")


from src.domain.info import InfoRepository, Info

database_path = "data/database.db"

info_repository = InfoRepository(database_path)

info_repository.save(Info(app_name="f5-seed-app"))
