def is_prime(func):
    def wrapper(*args):
        isprime = True
        result = func(*args)
        for i in range(2, result):
            if result % i == 0:
                isprime = False
                break
        if isprime:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result1 = sum_three(2, 3, 6)
print(result1)
result2 = sum_three(2, 14, 5)
print(result2)
