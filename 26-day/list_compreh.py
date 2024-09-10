numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_n = n + 1
#     new_list.append(add_n)
# print(new_list)
# new_list = [new_item for item in list]

new_list = [n % 2 for n in numbers]
print(new_list)
