# Напишите программу, которая принимает на вход число N и выдает
# последовательность из N членов.
# Пример:
# N = 5: 1, -3, 9, -27, 81

def sequence(N):
    array = []
    # numbers = 1
    for i in range(N+1):
        array.append((-3) ** i)
        # numbers *= -3
    return array

array = sequence(4)
print(array)