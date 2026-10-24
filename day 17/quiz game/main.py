from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def creating_data(data):
    """
    Create a list of Question objects from raw data.

    Args:
        data (iterable): An iterable of dictionaries, each containing
            the keys "text" and "answer".

    Returns:
        list: A list of Question objects created from the input data.
    """
    data_bank = []
    for item in data:
        data_bank.append(Question(item["text"],item["answer"]))
    return data_bank





question_bank = creating_data(question_data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


