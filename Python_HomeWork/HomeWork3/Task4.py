# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

result = ""
your_num = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while your_num != 0:
    result += str(your_num%2)
    your_num //=2
print(result)