# Размерность матрицы вводится с клавиатуры, заполнить матрицу случайными числами
# от 10 до 50.
# Найти наибольшую сумму элементов в столбцах матрицы.
# Вывести индекс столбца с максимальной суммой элементов на экран
# from random import randint
# n = int(input())
# m = int(input())
#
# d = [[randint(1,10) for j in range(m)] for i in range(n)]
# print(d)
# l_d = []
# for i in d:
#     s = 0
#     for j in i:
#          s += j
#     l_d.append(s)
# print('наибольшя сумма элементов в столбцах матрицы =',max(l_d), l_d,
#       'индекс столбца с максимальной суммой элементов', l_d.index(max(l_d)))

# Дан списко кортежей. Написать программу, которая меняет последнее значение элемента кортежей.

# list_1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# l2=[]
# for i in list_1:
#     l = list(i)
#     l[-1] = 0
#     l1 = tuple(l)
#     l2.append(l1)
# print(l2)

#Написать программу для вывода уникальных значений из списка словарей

# list_1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#           {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# a = []
# for i in list_1:
#     for j in i.values():
#         a.append(j)
#
#
# print(set(a))

# Есть файл text.txt. Вывести слово, имеющее минимальную длину. Обработать исключения.
# try:
#     with open('task3.txt', 'r', encoding='utf-8') as a:
#
#         al = a.split(' ')
#         all = []
#         for i in al:
#             all.append(len(i))
#
#             # print(i)
#         print(al[all.index(max(all))])
# except FileNotFoundError:
#     print('File could not be open')

#1 Написать программу для получения списка словарей из списков.

# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
#
# a = [(dict.fromkeys('color_name'),"Black"), (dict.fromkeys('color_code'),"#000000")]
# b = [(dict.fromkeys('color_name'),"Red"), (dict.fromkeys('color_code'),"#FF0000")]
# c = [(dict.fromkeys('color_name'),"Maroon"), (dict.fromkeys('color_code'),"#800000")]
# d = [(dict.fromkeys('color_name'),"Yellow"), (dict.fromkeys('color_code'),"#FFFF00")]