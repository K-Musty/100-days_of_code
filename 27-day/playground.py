def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 5, 7, 8))
