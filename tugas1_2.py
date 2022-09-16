from functools import reduce

def triangular(x):
    i = x
    while x > 0:
        yield x 
        x -= 1
        i = x

def get_sum(acc, x):
    return acc + x

triangular = list(triangular(6))
sum = reduce(get_sum, triangular)

print(sum)