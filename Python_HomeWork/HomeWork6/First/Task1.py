# lambda, filter

# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

# def uniq_num(nums):
#     new_nums = []
#     for i in nums:
#         if nums.count(i) == 1:
#             new_nums.append(i)
#     print(f'{nums} -> {new_nums}')


# nums = [4, 7, 7, 5, 6, 6, 8, 8, 3, 9, 9, 9, 4, 3]
# nums2 = [1, 1, 1, 3, 3, 8, 4, 4, 5, 5, 2, 2, 9]
# nums3 = [1, 1, 1, 5, 5, 6, 6, 7, 7, 3, 3, 2, 2]
# uniq_num(nums)
# uniq_num(nums2)
# uniq_num(nums3)


import random

numbers_list =[random.randrange(1, 25) for i in range(10)]
result_list = list(filter(lambda x: numbers_list.count(x) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \nсписок уникальных элементов => {result_list}')
