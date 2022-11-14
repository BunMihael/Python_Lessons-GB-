from random import randint

PATH_POL_1 = "equation1.txt"
PATH_POL_2 = "equation2.txt"

MODE_FILE_READ = 'r'
MODE_FILE_WRITE = 'w'


def coefficients_of_polynomial():
    factor = {}
    degree = int(input('Please enter the maximum degree: '))
    for i in range(degree, -1, -1):
        factor[i] = randint(-100, 100)
    return factor


def create_a_polynomial(coef: dict):
    equation = ''
    first = True
    for i in coef.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

    return equation + ' = 0'


def parse_equation(equation: str):
    equation = equation.replace(' + ', ' +').replace(' - ', ' -')
    equation = equation.split()
    equation = equation[:-2]

    dictEquation = {}
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x^')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation


def result_equation():
    result = {}
    for i in range(max(len(parEq1), len(parEq2)), -1, -1):
        first = parEq1.get(i)
        second = parEq2.get(i)
        if first is not None or second is not None:
            result[i] = (first if first is not None else 0) + \
                        (second if second is not None else 0)
    return result


def print_equation(equation: str):
    print(equation.replace(" 1x", "x").replace("x^1", 'x').replace("x^0", ''))


def write_pol_to_file(path_f1: str, path_f2: str, pol1: str, pol2: str) -> None:
    with open(path_f1, MODE_FILE_WRITE) as f1, open(path_f2, MODE_FILE_WRITE) as f2:
        f1.write(pol1)
        f2.write(pol2)


def main():
    equation1 = create_a_polynomial(coefficients_of_polynomial())
    equation2 = create_a_polynomial(coefficients_of_polynomial())

    write_pol_to_file(PATH_POL_1, PATH_POL_2, equation1, equation2)


if __name__ == '__main__':
    main()
