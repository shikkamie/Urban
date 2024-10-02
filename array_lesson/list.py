# Несколько вариантов создания кортежей.
# tuple_ = 1, 2, 3, True, "String"
# list = [1, 2, 3, True, "String"]
# print(tuple_.__sizeof__())
# print(list.__sizeof__())

tuple_ = ([1, 2], 0) + (1, 2)
print(tuple_)
tuple_[0][0] = 2
print(tuple_)
