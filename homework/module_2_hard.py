
# def password_key(n):
#     res = ''
#     if 3 <= n <= 20:
#         for i in range(1, n // 2 + 1):
#             j = n - 1
#             if i < j:
#                 dual = i + j
#                 if n % dual == 0:
#                     res += str(i) + str(j)
#         return res

# g = int(input('Введите число от 3 до 20: '))
#
# print(password_key(g))

def password_key(n):
    resu = ""
    if 3 <= n <= 20:
        for i in range(1, n // 2 + 1):
            j = n - i
            if i < j:  # Убедимся, что i и j разные
                dual = i + j
                if n % dual == 0:  # Проверка кратности
                    resu += str(i) + str(j)  # Добавляем пару в результат

    else:
        print('Введенное число не попадает в заданный диапазон')

    return resu
g = int(input('Введите число от 3 до 20: '))
print(password_key(g))