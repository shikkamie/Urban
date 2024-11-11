# phone_book = {'Denis': 88005553535, 'Max': 88005553434} # Ключем может быть неизменяемый объект
# # Если ключем сделать список, то будет ошибка
# phone_book['Denis'] = 12333111
# phone_book['Anton'] = [1233311, 322, 488]
# # print(phone_book)
# # del phone_book['Max']
# # print(phone_book)
# #
# # phone_book.update({'Alex': 4431331,
# #                    'Lena': 99487})
# # print(phone_book)
# #
# # # print(phone_book.get('Deniss', 'Такого ключа нет'))
# #
# # phone_book.pop('Anton') # Метод вытаскивает значение ключа и убирает его из списка
# # print(phone_book)
#
# print(phone_book.items()) # value, keys

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
# print(set_)

# print(set_.discard(1)) # Не выдаст ошибку, если элемент не был найден во множестве
# # revode Можно использовать, но выдаст ошибку если не найдёт элемент
# print(set_)

# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# average_value = []
# a = []
# for i in range(0, len(grades)):
#     a = [sum(grades[i]) / len(grades[i])]
#     average_value.append(a)
# # print(average_value)

#
# dict_student = dict(zip(sorted(students), average_value))
# print(dict_student)
# dict_student = {}
# set_students = sorted(students)
#
# for i in range(0, len(grades)):
#     dict_student[set_students[i]] = average_value[i]

# print(dict_student)
s = 'lol'
print(s[5])