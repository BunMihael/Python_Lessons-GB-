equations = []
with open('equation.txt', 'r') as file:
    equations = file.readline()
with open('result.txt', 'w') as file:
    pass
print(equations)

for eq in equations:
    equation= eq.replace('\n', '')
    transformed = equation.replace(
        '*x**2', ' ').replace('*x', ' ').replace('- ', '-').replace('+ ', ' ')
    lst = transformed.split(' ')
    abc = []
    for item in lst:
        try:
            num = float(item)
            abc.append(num)
        except:
            continue
    a, b, c =0, 0, 0

    if equation.find('*x**2') > 0:
        a = abc.pop(0)
    if equation.replace('*x**2', '').find('*x') > 0:
        b = abc.pop(0)
    if len(abc) > 0:
        c = abc.pop(0)

    print('A = ', a, 'B = ',b, 'C = ', c)
    
    discr = b**2 - 4*a*c*c
    sqrtdisc = discr**0,5

    print('Дискриминант = ', discr)

    x1 = (-b + sqrtdisc)/(2*a)
    x2 = (-b - sqrtdisc)/(2*a)

    result = f'Корни квадратного уравнения {equation}:\nx1 = {x1:.3f}\nx2 = {x2:3f}\n\n'
    print(result)

    with open('result.txt', 'a') as file:
        file.write(result)