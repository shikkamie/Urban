


my_dict = {'Anna': 89931413320, 'Max': 89913393219}
print(my_dict)
print('Вытаскиваем значение по ключу:', my_dict['Anna'], '\n', 'По несуществующему ключу без ошибки:', my_dict.get('Nikolay'))

my_dict.update({'Elena': 88005551310, 'Valentin': 89604483222})
print('Значение удалённого элемента по ключу:', my_dict.pop('Anna'))
print('Словарь после удаления элемента:', my_dict, '\n')

print('Множества:')

my_set = {1, 2, 2, 3, True, True, 'Snow', 'Vechle', 4, 3, 'Vechle', 3}
print(my_set)

my_set.add((6,1,3))
my_set.add('New')

my_set.discard(9)
print('Измененное множество:',my_set)


