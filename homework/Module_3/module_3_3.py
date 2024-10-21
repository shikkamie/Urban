def print_params(a = 1, b = 'строка', c = True):
   print(a, b, c)

print_params()

print_params(2, 'новая строка', False)

print_params(c = False, a = 3)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [3, 'test1', False]

values_dict = {
   'a': 1,
   'b': 'тест',
   'c': True
}

print_params(**values_dict)
print_params(*values_list)

values_list_2 = [3, True]

print_params(*values_list_2, 42)