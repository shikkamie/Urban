immutable_var = ([1, 2], 3, "String", True)
print(immutable_var)
# immutable_var [1] = 33
print("Кортеж неизменяем. Думаю, будет полезно для создания констант, которые не изменятся.  При этом, в кортеж можно вложить список и изменять элементы внутри него. Мы не меняем сам элемент(список), а лишь значения, на которые ссылаются его элеметны", "Появится ошибка: TypeError: 'tuple' object does not support item assignment")
immutable_var[0][1] = "exchange" # Заменили элемент в списке.
print(immutable_var)



mutable_list = [12, 34, 56, "Integer"]
print("Default:", mutable_list)
mutable_list[1] = 78 # Меняем сам элемент списка
print("С измененным :", mutable_list)
mutable_list.pop(0) # Удаление элемента по индексу
print("С удалённым первым элементом:", mutable_list)

