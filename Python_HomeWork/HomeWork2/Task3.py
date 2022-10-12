# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

lenght = int(input("Please write a number: "))

sequence = []
suma = 0

for i in range(1, lenght + 1):
    number = round((1+(1/i))**i)
    sequence.append(number)
    suma += number
    
print(f'{sequence} => {suma}')
