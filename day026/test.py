import random

import pandas

# List comprehension
#     new_item      item                 test
list = [num * 2 for num in range(1, 5) if num != 3]
# print(list)

# Dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {item: random.randint(1, 100) for item in names}
# print(students_scores)

passed_students = {
    student: score for (student, score) in students_scores.items() if score > 50
}
# print(passed_students)

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 73, 98]}
# for key, value in student_dict.items():
# print(value)

stud_data_frame = pandas.DataFrame(student_dict)
for index, row in stud_data_frame.iterrows():
    if row.student == "Angela":
        print(f"Angela's score is: {row.score}")
