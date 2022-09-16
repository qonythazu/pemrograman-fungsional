def squared(x,y):
    if y > 1:
        return x * squared(x, y-1)

    return x

print(squared(3,2))