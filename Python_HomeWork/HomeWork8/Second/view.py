def show_menu():
    """
    Displaying the user's menu.
    :return:
    """
    print("Menu:")
    print('\t1 - Read data:')
    print('\t2 - Create new record:')
    print('\t3 - Delete data:')
    print('\t4 - Change telephon')
    print('\t5 - Change grade')
    print('\t6 - Change status:')
    print('\t7 - import data in txt-file')
    print("\t8 - Exit")
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