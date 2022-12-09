# main
db_main = dict()
global_mapping = {"lastname": "Фамилия", "firstname": "Имя", "group": "Класс"}

id = 32
data_1 = ["Иванов", "Иван", "9F"]


def update_record(db: dict, rec_id: int, data: list, mapping: dict):
    db[rec_id] = {name: value for name, value in zip(mapping.keys(), data)}
    return db


update_record(db_main, id, data_1, global_mapping)