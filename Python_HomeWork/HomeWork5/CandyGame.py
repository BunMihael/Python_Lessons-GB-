from random import randint


def introducing_players(menu_data):
    player1 = input('Чтобы начать игру, пожалуйста, введите свое имя\n')
    bot = 'БОТик'
    if menu_data == 1:
        print(f'Приятно познакомися {player1}! Меня зовут {bot} и я буду с тобой играть.')
    elif menu_data == 2:
        print(f'Приятно познакомися {player1}! Пожалуйста, введите имя второго игрока.\n')
        player2 = input()
        print(f'Приятно познакомися {player2}!\n Давайте начнем игру!\n')
    return [player1, bot, player2]


def main_menu():
    menu = int(input('Здравствуйте, Вас приветствует игра "CandyGame"!\n '
                     'ГЛАВНОЕ МЕНЮ (Выберите число):\n'
                     '1. Игра с БОТиком\n'
                     '2. Игра с человеком\n'
                     '3. Правила игры\n'
                     '4. Автор\n'))
    if menu > 4 or menu < 1:
        print('Такого номера меню не существует. Попробуйте выбрать еще раз.\n')
        main_menu()
    elif menu == 3:
        print('Основные правила игры:\n '
              'Нам будет дано некоторое количество конфет, за один ход\n'
              'мы можем взять не более определённого количества,\n '
              'о котором мы с вами договоримся.\n '
              'Итак, давайте начнём!\n')
        main_menu()
    elif menu == 4:
        print('Меня зовут Бунь Михаил. Это моя первая игра, которую я создал.\n'
              'Желаю насладится игрой и хорошо провести время.\n'
              'Желаю хорошего дня!\n')
        main_menu()
    return menu


def input_rules(players):
    candy_max = int(input(
        f'{players[0]}, напишите пожалуйста, сколько конфет будет участвовать в игре?\n'))
    candy_move = int(input(f'Сколько конфет можно взять за 1 ход?\n'))
    first_move = int(input(f'{players[0]}, если хотите ходить первым, то напишити число 1.\n'
                    'Если не хотите ходить первым, то напишите число 2.\n'
                    'Если хотите чтобы выбор был случайным, то напишите любое целое число.'))
    if first_move != 1 and first_move != 2:
        first_move = randint(1, 2)
    return [candy_max, candy_move, first_move]


def bot_mind(rules, cadies_count):
    if cadies_count > rules[1] * 3:
        return randint(1, rules[1] + 1)
    elif cadies_count <= rules[2] * 3 and cadies_count >= rules[3] * 2 + 2:
        for x in range(1, rules[1] + 1):
            if (cadies_count - x) % 10 == 5 or 0:
                result = x
        return result
    elif cadies_count <= rules[1] * 2 + 2 and cadies_count > rules[1] + rules[1] / 2 - 1:
        return int(rules[1]/cadies_count * 15)
    elif cadies_count < rules[1] + rules[1] / 2 and cadies_count > rules[1]:
        return (cadies_count / 100) * int(rules[1]/cadies_count * 15)
    elif cadies_count <= rules[1]:
        return cadies_count


def game(players, rules, menu_data):
    cadies_count = 0
    while cadies_count <= rules[0]:
        if menu_data == 1 and rules[2] == 1:
            i = 1
            if players[i] == players[0]:
                move = int(
                    input(f'{players[i]}, возьмите от 1 до {rules[1]} конфет.\n'))
                if move > rules[1]:
                    print(
                        f'Вы взяли {move} конфет, это больше, чем позволено. Возьмите от 1 до {rules[1]} конфет.\n')
                else:
                    cadies_count += move
                    print(f'Осталось {rules[0] - cadies_count} конфет.')
            if players[i] == players[1]:
                move = bot_mind(rules, cadies_count)
                cadies_count += move
                print(f'Я взял {move} конфет. Осталось {cadies_count} конфет')
                print(f'Осталось {rules[0] - cadies_count} конфет.')
            i = 1 if i == 2 else 2
            print(f'{players[i]} выйграл.')

        if menu_data == 1 and rules[2] == 2:
            i = 2
            if players[i] == players[0]:
                move = int(input(f'{players[i]}, возьмите от 1 до {rules[1]} конфет.\n'))
                if move > rules[1]:
                    print(
                        f'Вы взяли {move} конфет, это больше, чем позволено. Возьмите от 1 до {rules[1]} конфет.\n')
                else:
                    cadies_count += move
            if players[i] == players[1]:
                move = bot_mind(rules, cadies_count)
                cadies_count += move
                print(f'Я взял {move} конфет. Осталось {cadies_count} конфет')
                print(f'Осталось {rules[0] - cadies_count} конфет.')
            i = 1 if i == 2 else 2
            print(f'{players[i]} выйграл.')

        if menu_data == 2 and rules[2] == 1:
            i = 1
            move = int(input(f'{players[i]}, возьмите от 1 до {rules[1]} конфет.\n'))
            if move > rules[1]:
                print(
                    f'Вы взяли {move} конфет, это больше, чем позволено. Возьмите от 1 до {rules[1]} конфет.\n')
            else:
                cadies_count += move
                print(f'Осталось {rules[0] - cadies_count} конфет.')
            i = 1 if i == 3 else 3
        if menu_data == 2 and rules[2] == 2:
            i = 2
            move = int(input(f'{players[i]}, возьмите от 1 до {rules[1]} конфет.\n'))
            if move > rules[1]:
                print(
                    f'Вы взяли {move} конфет, это больше, чем позволено. Возьмите от 1 до {rules[1]} конфет.\n')
            else:
                cadies_count += move
                print(f'Осталось {rules[0] - cadies_count} конфет.')  
            i = 1 if i == 3 else 3
            print(f'{players[i]} выйграл.')

        if cadies_count >= rules[0]:
            print('Все конфеты разобраны.')
    return players[i]



menu_data = main_menu()
players = introducing_players(menu_data)
rules = input_rules(players)
winer = game(players, rules, menu_data)
