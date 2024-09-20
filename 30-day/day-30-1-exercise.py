fruits = ["apple", "pear", "orange"]

# TODO: catch the exception and make sure the code works without crashing


def make_pie(index):
    try:
        fruit = fruits[index]

    except IndexError:
        print("fruit pie")

    else:
        print(fruit + " pie")


make_pie(3)
