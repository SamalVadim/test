# n = 3
# m = 2
# a = 0
# #a = [[0]*m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         a[i][j] = 2
#         print(a)
# print(a, end=' ')
# print()

# try:
#     k = 1/0
# except ZeroDivisionError:
#     k = 'На ноль делить нельзя'
# print(k)

''' Создать матрицу M x N, где M и N вводятся с клавиатуры.
Элементы матрицы заполнить случайными числами. Сделать читабельный вывод матрицы.
'''
# from random import randint
# n = 5
# m = 5
#
# a = [[randint(1,10) for i in range(n)] for j in range(m)]
# print(a)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()
# for i in range(n):
#     for j in range(m):
#         a[i][j] = randint(1,10)
#         print(a[i][j])



'''Введите два числа с клавиатуры. Поделите одно на другое. 
Обработайте ошибку деления на ноль, если ошибок нет, то результат деления возвести в квадрат. 
Также используйте оператор finally.

'''
# a,b = map(int,input().split())
# # c= a/b
# try:
#     c= a/b
# except ZeroDivisionError:
#     c = 'На ноль делить нельзя'
# finally:
#     print('Программа завершина')
# print(c**2)

''' Матрица N x M, можно задать статически. 
Элементы заполняются случайными числами. 
Вводить с клавиатуры число и если оно есть в матрице, 
то вывести индекс строки и колонки в которой оно находится. 
'''
# from random import randint
# n = 3
# m = 3
# d = 5
# a = [[randint(1,10) for i in range(n)]for j in range(m)]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#
#           print(a[i][j], end= ' ')
#     print()

    # if a[i][j] == d:
    #     print(f"Индекс числа {d}-{i, j}")
    # else:
    #     print('Такого числа в матрице нет')

'''Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.  
'''
# from random import randint
#
# a = [[randint(1,10) for i in range(5)]for j in range(5)] # составили матрицу
# ls_a = []
# for i in a:
#     s = 0
#     for j in i:
#         s += j       # нашли суммы строк
#         print(j, end=' ')
#     print()
#     ls_a.append(s)  #создать список из суммы строк s
#     #print(s)
#
# print(f'В данной матрице максимальная сумма элементов строки явдяется {max(ls_a)}, '
#       f'строка находится на {ls_a.index(max(ls_a))+1} строке в матрице')


''' Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, 
то поделить первое на второе. Обработать ошибку деления на ноль. 
Если второе число 0, то программа запрашивает ввод чисел заново. 
Также если были введены буквы, то обработать исключение. '''


while True:
    try:
        a = input('Введите число')
        if a == 'end':
            break
        a_ls = a.split(',')
        c = int(a_ls[0])/int(a_ls[1])
    except ZeroDivisionError:

        print('На ноль делить нельзя, введите новое число,')
        continue

    except ValueError:
        print('Введите правильный символ')
        continue
    else:
        print(c)







