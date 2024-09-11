import pandas
with open("file1.txt", mode="r") as file1:
    content_1 = [int(num.strip()) for num in file1.readlines()]
with open("file2.txt", mode="r") as file2:
    content_2 = [int(num.strip()) for num in file2.readlines()]

# file1_stripped = []
# for num in content_1:
#     stripped = num.strip()
#     file1_stripped.append(int(stripped))
#
# file2_stripped = []
# for num in content_2:
#     stripped = num.strip()
#     file2_stripped.append(int(stripped))

result = [n for n in content_1 if n in content_2]
print(result)

