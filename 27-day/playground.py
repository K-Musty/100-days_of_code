# Playing around with arguments
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(2, 5, 7, 8))


def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=6)
