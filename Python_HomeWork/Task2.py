# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x,y,z = 3

print('Please, enter x, y, z to verify the truth of the expression ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z.')
x = int(input(' Write a number for x: '))
y = int(input(' Write a number for y: '))
z = int(input(' Write a number for z: '))

if (not(x or y or z)) == (not(x) and not(y) and not(z)):
    print("The statement is true.")
else:
    print('The statement is not true.')

# statement1 = not(x or y or z)
# statement2 = not(x) and not(y) and not(z)
# final_statement  = statement1 == statement2
# print(final_statement)

