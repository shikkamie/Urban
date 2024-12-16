

def is_prime(func):
    def wrapper(*args):
        is_prime = 'Число простое'
        not_prime = 'Число не простое'
        res = func(*args)
        if res < 2:
            print(not_prime)
            return res
        for i in range(2, int(res **0.5) + 1):
            if res % i == 0:
                print(not_prime)
                return res
        print(is_prime)
        return res
    return wrapper

@is_prime
def sum_three(*args):
    res = sum(args)
    return res
result = sum_three(2, 3, 6)

print(result)

