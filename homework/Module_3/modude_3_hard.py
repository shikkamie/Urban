# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-isinstance/


def sum_num_and_count(*el):
    end_sum = 0


    def recursive_sum(item):
        nonlocal end_sum
        if isinstance(item, int | float):
            end_sum += item
        elif isinstance(item, str):
            end_sum += len(item)
        elif isinstance(item, list) or isinstance(item, tuple):
            for i in item:
                recursive_sum(i)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)
        elif isinstance(item, set):
            for elem in item:
                recursive_sum(elem)
    recursive_sum(el)
    return end_sum

data_structure = [
    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])
]



result = sum_num_and_count(data_structure)

print(result)