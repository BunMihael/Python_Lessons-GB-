Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

Список полей предопределен: Фамилия, Имя, Класс/Отдел и в процессе работы не меняется.
Запись должна иметь уникальный ID (increment), продумать вопрос о реализации безусловной уникальности.
Выбрать подходящие структуры данных для хранения записей и БД целиком, продумать распределение по model-view-controller

Функционал программы
- CRUD:
- CREATE: Создать запись по заданному множеству полей и записать ее в БД. Поля вводятся пользователем.
- READ: Извлечь запись по ID. Запись извлекается и выводится в консоль
- UPDATE: Обновить запись по ID.
- DELETE: Удалить запись по ID.
- Импорт из CSV файла с ID. Использовать пакет csv стандартной библиотеки.
Пример:
1#Сидоров#Алексей#9А
2#Соколов#Григорий#9А
Данные в БД добавляются, считаем, что уникальность реализуется с помощью ID.
- Импорт из CSV файла без ID
Пример:
Иванов#Иван#9Б
Петров#Василий#8А

ополнительно(усложнение):
- Реализовать эскпорт БД в оба текстовых формата (с ID и без него)
- Реализовать SELECT по одному полю. Пользователь выбирает по какому полю делать выборку, затем указывает что искать.
Найденные записи выводятся на экран вместе с ID.

"last_name": last_name, "first_name": first_name, "group": group
{1: "last_name": last_name, "first_name": first_name, "group": group, 2: "last_name": last_name, "first_name": first_name, "group": group}

def update_record(db: dict, rec_id: int, data: list):
db[rec_id] = {"last_name": last_name, "first_name": first_name, "group": group}


view
Предложить юзеру меню:
1 CREATE
2 READ
3 UPDATE
4 DELETE
5 EXPORT
6 IMPORT1 (with ID)
7 IMPORT (without ID)
8 EXIT

Model
1 CREATE Добавить новую запись
(input: str -> new data: dict)
Принемает строку или строки
Возвращает запись
Запись, принятая от пользователя, новая. {"last_name": last_name, "first_name": first_name, "group": group}
Уникальный ID добавленный к записи, словарь словарей {number:{запись от пользователя1} number1:{запись2}}


2 READ Отобразить запись по ID
(db: {dict}, id: int -> rec: dict)
Принимает уникальный ID ввиде цифры

3 UPDATE Обновить запись по ID
(db: {dict}, ID: int, new data: str -> rec: dict)

4 DELETE Удалить запись по ID
(db: {dict}, ID: int -> updated db : {dict})


ID REALIZATION
ID stored in separated File
get_id (file_name: str) -> next free ID: int


store_id (file_name: str, last used ID: int) -> None


import_with_id (db: {dict}, file_name: str) -> updated db: {dict}
В файле уже содержатся уникальные ID

import_without_id (db: {dict}, file_name: str) -> updated db: {dict}
Парсим строку из файла сплитом, получаем список строк, заносим его в словарь для записи
(Нужно применять get_id и store_id)