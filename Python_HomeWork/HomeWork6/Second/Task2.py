# Есть два списка: tutors - имена учеников, groups - названия их классов.
# Необходимо сформировать список кортежей вида (tutor, group).

# Результат, где учеников меньше


import itertools


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

# Результат, где учеников меньше

tutors2 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

groups2 = ['9А', '7В', '9Б', '9В']


#  Решение через zip и zip_longest. 

# def creating_lists(tutors, groups):
#     if len(tutors) > len(groups):
#         lst = list(itertools.zip_longest(tutors, groups, fillvalue=None))
#         print('Tutors > groups.')
#     else:
#         lst = list(zip(tutors, groups))
#         print('Tutors < groups.')
#     return lst

# Решение помощью list comprehension без zip и zip_longest.

def creating_lists(tutors, groups):
    lst = [(tutors[i], groups[i]) if i < len(groups) else (tutors[i], None) for i in range(len(tutors))]
    return lst


print(f"List 1: {creating_lists(tutors, groups)}")
print(f"List 2: {creating_lists(tutors2, groups2)}")



