from math import prod
import common

WARN_OUT_OF_RANGE = "Error."
user_answer = True

while(user_answer):
    common.Console.clear()
    common.print_title('Формирование списка произведений чисел от 1 до N')

    n = common.get_user_input_int(
        'Введите натуральное число N: ', WARN_OUT_OF_RANGE, lambda x: x>0)

    lst = list(map(lambda i: prod(range(1, i+1)), range(1, n+1)))
    print(f'\nВывод: {n} -> {lst}')

    print(f'\nСумма цифр числа {num_str} = {dsum}')
    print()

    user_answer = common.ask_for_repeat()