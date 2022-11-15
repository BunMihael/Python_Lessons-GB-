# Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200. Использовать comprehensions.

def odd_int_list():
    # lst = [0,1]
    # lst = [n for n in range(1, number + 1, 2) if n * 2 < 200]
    # return lst
    lst = [n for n in range(0, int(input("Input num: "))) if n % 2 != 0 or n == 0 and n * 2 < 200]
    return lst

print(odd_int_list())

# l = [i for i in range(1, int(input()) + 1, 2)]
# print(l)