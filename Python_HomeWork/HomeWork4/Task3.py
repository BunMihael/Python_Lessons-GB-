# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def uniq_num(nums):
    new_nums = []
    for i in nums:
        if nums.count(i) == 1:
            new_nums.append(i)
    print(f'{nums} -> {new_nums}')


nums = [4, 7, 7, 5, 6, 6, 8, 8, 3, 9, 9, 9, 4, 3]
nums2 = [1, 1, 1, 3, 3, 8, 4, 4, 5, 5, 2, 2, 9]
nums3 = [1, 1, 1, 5, 5, 6, 6, 7, 7, 3, 3, 2, 2]
uniq_num(nums)
uniq_num(nums2)
uniq_num(nums3)


# from random import randint as rI

# unique = {}

# my_list = ''.join(list(map(str, [rI(0,9) for i in range(20)])))
# print(my_list)

# for c in my_list:
#     if unique.get(c):
#         unique[c] = unique.get(c) + 1
#     else:
#         unique[c] = 1

# u_list = []

# for i in unique.items():
#     if i[1] == 1:
#         u_list.append(i[0])

# print(*u_list)
