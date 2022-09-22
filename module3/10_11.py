def factorial(n):
    sum = 1
    for i in range(1, n + 1):

        print(f'{i} * {sum} = {sum*i} i')
        sum *= i
        print("-------")


def number_of_groups(n, k):
    result = factorial(n) / (factorial(n-k) * factorial(k))
    return result


print(factorial(4))
