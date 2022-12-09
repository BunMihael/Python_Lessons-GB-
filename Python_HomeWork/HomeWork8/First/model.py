# Model
# 1 CREATE Добавить новую запись
# (input: str -> new data: dict)
# Принемает строку или строки
# Возвращает запись
# Запись, принятая от пользователя, новая. {"last_name": last_name, "first_name": first_name, "group": group}
# Уникальный ID добавленный к записи, словарь словарей {number:{запись от пользователя1} number1:{запись2}}

import csv

def create_rec(surname, name, grade) -> dict:
    """
    Creating a record in the form of a dictionary based on data
    :param surname: surname
    :param name: name
    :param grade: grade
    :return: record in the form of a dictionary
    """
    return {'surname': surname, 'name': name, 'grade': grade}


def import_file(filename: str, delimiter="#") -> list:
    """
    Import data from file
    :param filename: file name(directory)
    :param delimiter: field separator
    :return: list of dictionaries
    """
    rez = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            surname, name, grade = line.strip().split(delimiter)
            rez.append({'surname': surname, 'name': name, 'grade': grade})
    return rez


def export_file(filename: str, data: list, delimiter=","):
    """
    Export dictionary to file
    :param filename: file name(directory)
    :param data: list of dictionaries
    :param delimiter: field separator
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as file:
        for rec in data:
            file.write(".".join(rec.values()))
            file.write(f"\n")
            
def update_record(db: dict, rec_id: int, data: list, mapping: dict):
    db[rec_id] = {name: value for name, value in zip(mapping.keys(), data)}
    return db

# # delete
# rec_id = view.