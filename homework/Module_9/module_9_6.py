from itertools import permutations, product


def all_variants(text):
    res = []
    for i in range(len(text)):
        yield text[i]
    for i in range(len(text)):
        for j in range(i + 2,len(text) + 1):
            yield text[i:j]


a = all_variants("abc")

for i in a:

    print(i)

