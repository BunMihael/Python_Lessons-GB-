# Задайте строку из набора чисел. Напишите программу которая покажет большее и меньшее число. 
# Символом разделителем будет пробел.


numbers = []
read:str
while True:
    open_file = input("Введите название файла: ")
    try:
        with open(open_file) as file:
            read = file.readline()
        break
    except:
        print('Ощибка чтения файла.')

list = read.split(' ')
for i in list:
    numbers.append(int(i))

print(numbers)
maximum = max(numbers)
minimum = min(numbers)

with open('3file.txt', 'w') as file:
    m = file.write(f'Maximum num: {maximum}, minimum num: {minimum}' )
    print(f'Maximum num: {maximum}, minimum num: {minimum}')