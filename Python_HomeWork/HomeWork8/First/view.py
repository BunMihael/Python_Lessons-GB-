def new_record() -> dict:
    """
    Entering data for a new entry in the system
    :return: record data in the form of a tuple
    """
    print("New record mode.")
    surname = input("Please enter last name:\n ")
    name = input("Please enter first name:\n ")
    grade = input("Please enter grade:\n")
    return surname, name, grade

def file_name() -> str:
    return input("Please enter name of file:\n")

def show_record(data: dict):
    """
    Displaying a single entry in the console
    :param data: record
    :return: None
    """
    for value in data.values():
        print(value, end= " ")
    print("")
    
def show_all_record(data: list):
    """
    Displaying all records in the system
    :param data: data in system
    :return: None
    """
    print("All entries in the system:")
    for record in data:
        show_record(record)
        
def show_menu() -> str:
    """
    Displaying the user's menu.
    :return:
    """
    print("Menu:")
    print("\t1-Create new record:")
    print("\t2-Read data:")
    print("\t3-Update data:")
    print("\t4-Import with ID:")
    print("\t5-Import without ID")
    print("\t6-Export data:")
    print("\t7-Delete data:")
    print("\t8-Exit")
    return input("Please choose the desired item:")