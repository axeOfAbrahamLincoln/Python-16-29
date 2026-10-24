import random, pandas

# list = [1, 2, 3]

# new_list = [n + 1 for n in list]

# print(new_list)

# name = "Angela"

# new_list = [letter for letter in name]
# print(new_list)

# double_list = [n*2 for n in range(1,5)]
# print(double_list)

names = ["Adam", "Csaba", "Valeria", "Karoly", "Bob", "Agi", "Adri", "Peter"]
scores = [11,22,33,44,55,66,77,88]

student_scores = {"Students": names,
                  "Scores": scores
                  }

print(student_scores)

# student_passed = {name:score for name, score in student_scores.items() if score > 60}

# print(student_passed)

dataset = pandas.DataFrame(student_scores)
print(dataset)

for row in dataset.itertuples():
    if row.Index == 4:
        print(row)
