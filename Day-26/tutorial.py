# How to iterate over a Pandas Dataframe
student_dict = {
    "student": ["Amy", "Sheldon", "lenard", "Penny"],
    "score": [75, 84, 79, 42]
}

# Remember looping through a list
# for (key, value) in student_dict:
#     print(key)

# Using Pandas DataFrame
import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# looping through a data frame
# for (key, value) in student_dataframe.items():
#     print(key)

# looping through a row in a data frame
for (index, row) in student_dataframe.iterrows():
    # print(row)
    if row.student == "Amy":
        print(row.score)
