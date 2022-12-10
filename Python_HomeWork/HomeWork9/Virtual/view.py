import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def show_menu():
    """
    Displaying the user's menu.
    :return:
    """
    print(f"{Fore.YELLOW}{Back.RED}M{Fore.YELLOW}{Back.BLUE}e{Fore.GREEN}{Back.CYAN}n{Fore.CYAN}{Back.GREEN}u:")
    print(f'\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}1 - {Fore.GREEN}{Back.YELLOW}Read data:')
    print(f'\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}2 - {Fore.GREEN}{Back.RED}Create new record:')
    print(f'\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}3 - {Fore.GREEN}{Back.CYAN}Delete data:')
    print(f'\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}4 - {Fore.GREEN}{Back.BLUE}Change telephon')
    print(f'\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}5 - {Fore.GREEN}{Back.MAGENTA}Change grade')
    print(f'\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}6 - {Fore.GREEN}{Back.WHITE}Change status:')
    print(f'\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}7 - {Fore.GREEN}{Back.LIGHTBLUE_EX}import data in txt-file')
    print(f"\t{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}8 - {Fore.GREEN}{Back.LIGHTMAGENTA_EX}Exit")
    return int(input('Please choose the desired item: '))

def delete():
    print('Enter ID to delete:\n')
    return int(input())

def change_tel():
    id = int(input('Enter ID to change: \n'))
    tel = input('Enter new telephon: \n')
    return id, tel

def change_grade():
    id = int(input('Enter ID to change: \n'))
    grade = input('Enter new grade:\n')
    return id, grade

def change_status():
    id = int(input('Enter ID to change: \n'))
    status = input('Enter new status:\n')
    return id, status

def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))

def add_info():
    print('Enter full name(ФИО), phone number, grade, status separated by a space')
    in_info = input().split()
    return in_info

def add_info_again():
    print('Do you need to add new information?')
    print('Enter 1 - no or 2 - yes:\n')
    new_info = int(input())
    return new_info

def show_export_txt():
    print('The file has been exported to txt format.')