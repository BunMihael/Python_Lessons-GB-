# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:
# ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR



def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    res = ''
    for i in range(1, len(txt), 2):
        res += txt[i]*int(txt[i-1])
    return res



# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


s = 'ABCABCABCDDDFFFFFF'
print(f"Befor: {s}")
print(f"Text after encoding: {coding(s)}")
print(f"Text after decoding: {decoding(coding(s))}")