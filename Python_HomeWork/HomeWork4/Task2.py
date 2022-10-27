# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент -
# целое число и возвращает список его простых множителей.

# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];


from itertools import count


def factoring_a_num(num):
    answer = []
    d = 2
    while d*d <= num:
        if num % d == 0:
            answer.append(d)
            num //= d
        else:
            d += 1
    else:
        answer.append(num)
    print(answer)


factoring_a_num(147420)
factoring_a_num(374220)
