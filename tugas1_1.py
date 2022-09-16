from functools import reduce

numbers = [1, 2, 3, 4]

def squared(x):
    return x**2

def get_sum(acc, x):
    return acc + x

squared = list(map(squared, numbers))
sum = reduce(get_sum, squared)

print(sum)