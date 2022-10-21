# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

result = ""
your_num = int(input("Please, enter a number to convert decimal to binary:\n"))
while your_num != 0:
    result += str(your_num%2)
    your_num //=2
print(result)