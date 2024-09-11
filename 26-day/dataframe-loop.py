student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 78, 98]
}

# for (key, value) in student_dict.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# using iterrows

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)