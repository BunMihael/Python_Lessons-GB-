# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

def quarter_range(x):
    if x == 1:
        print('x > 0 && y > 0')
    elif x == 2:
        print('x < 0 && y > 0')
    elif  x == 3:
        print('x < 0 && y < 0')
    elif x == 4:
        print('x > 0 && y < 0')
    else:
        print('Error')
    
x = int(input('Please write number of quarter:'))
quarter_range(x)


# double Distance(double x1, double y1, double z1, double x2, double y2, double z2)
# {
#     return Math.Round(Math.Sqrt(Math.Pow(x1 - x2, 2) + Math.Pow(y1 - y2, 2)+ Math.Pow(z1 - z2, 2)), 4);
# }

# Console.WriteLine(Distance(3, 6, 8, 2, 1,-7));