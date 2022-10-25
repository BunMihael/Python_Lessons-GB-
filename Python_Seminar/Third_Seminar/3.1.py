# Задайте список. Напишите программу, которая определит, присутствует в ли в заданном
# списке строк некое число.

# lst = ['gs;sdw34','dvj030761fs','jspf 8392js','hdspa354']

# def find_num(lst, some_num):
#     for i in lst:
#         for j in i:
#             if str(some_num) == j:
#                 print(f'The given list {i} contains a number {some_num}')

# some_num = int(input('Please, write a number you want to find in list: '))
# print(find_num(lst,some_num))

    
lst = ['gs;sdw34','dvj030761fs','jspf 8392js','hdspa354']

def find_num(lst, some_num):
    for i in range(len(lst)):
        if str(some_num) in lst[i]:
            print(f'The given list {i+1} contains a number {some_num}')
        else:
            print(f'The given list {i+1} have no number {some_num}')

some_num = int(input('Please, write a number you want to find in list: '))
print(find_num(lst,some_num))


# str="Hello, World!"
# if str.find("World")!=-1:
#     print("Found the string")
# else:
#     print("Not found!!!")

