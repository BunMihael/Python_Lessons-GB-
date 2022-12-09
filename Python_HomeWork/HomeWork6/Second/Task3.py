#  Задан список чисел. Необходимо создать список, содержащий те его элементы,
# значения которых больше предыдущего.
# Примеры/Тесты:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def more_than_last_element(src):
    lst = [src[i + 1] for i in range(len(src) - 1) if src[i] < src[i + 1]]
    return lst

print(more_than_last_element(src))

# input_data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# print(
#     [value for key, value in enumerate(input_data[1:], start=1) if value > input_data[key - 1]]
# )