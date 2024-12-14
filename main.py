my_num = [3, 1, 5, 5, 4]


def is_odd(num):
    return num % 2
result = filter(is_odd, my_num)
print(list(result))
