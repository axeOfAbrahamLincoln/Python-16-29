import pandas


dataset = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(dataset)

code_alphabet = {row.letter: row.code for (index, row) in dataset.iterrows()}
# print(code_alphabet)


# SOLUTION WITH WHILE LOOP

# while True:
#     user_input = input("What is your name?: ").upper()
#     try:
#         code_list = [code_alphabet[word] for word in user_input]
#     except KeyError:
#         print("You have to type letters.")
#     else:
#         break

# print(code_list)


# SOLUTION WITH FUNCTION Recursion (function into the same function)
# not the best solution because:
# Each recursive call stays in memory (stack grows)
# If the user keeps entering invalid input → could eventually crash (stack overflow)


def generate_nato_phonetic():
    user_input = input("What is your name?: ").upper()
    try:
        code_list = [code_alphabet[word] for word in user_input]
    except KeyError:
        print("You have to type letters.")
        generate_nato_phonetic()
    else:
        print(code_list)


generate_nato_phonetic()
