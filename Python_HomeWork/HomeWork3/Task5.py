# Задайте число. Составьте список чисел Фибоначчи, в
# том числе для отрицательных индексов.
# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]




def form_fibo_list(nums):
    nums = abs(nums)
    fibo_list = [1,0,1]

    for i in range(3, nums+2):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    
    for i in range(2, nums+1):
        fibo_list.insert(0, fibo_list[1] - fibo_list[0])

    return fibo_list

print(form_fibo_list(8))