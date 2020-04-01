# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Name(s)
# **PUT YOUR FULL NAME(S) HERE**

# **Instructions:** This is an individual assignment. Complete the following code and push to get your score.

# I am providing the autograder answers locally so you may test your code before pushing. I will be reviewing your submissions, and if I find you are circumventing the autograder in any manner, you will receive a 0 on this assignment and your case will be reported to the honor board for review. i.e., approach the assignment in a genuine manner and you have nothing to worry about.


# **Question 1.**
# When will new material be available each week?

# You can answer the question by defining an anonymous function. This creates a function that I can test using pytest. You don't have to worry about the details. You just need to answer the question by changing the string argument that is currently set to "D". I know this is a bit weird, but I want you to get used to submitting code as early as possible.

# Nothing to modify in this cell
def question_1(answer):
    answers = {
        "A": "Monday morning",
        "B": "Sunday night",
        "C": "Monday evening",
        "D": "I don't know"
    }
    try:
        return answers[answer]
    except:
        return "Not a valid answer"


# YOUR SOLUTION HERE
# Sample incorrect answer
answer_question_1 = lambda: question_1("Z")


# **Question 2.**
# Do I need to buy the textbook?

# Nothing to modify in this cell
def question_2(answer):
    answers = {
        "A": "No",
        "B": "Maybe",
        "C": "Yes. You will struggle with some of the chapters without the textbook",
    }
    try:
        return answers[answer]
    except:
        return "Not a valid answer"


# YOUR SOLUTION HERE
# Sample incorrect answer
answer_question_2 = lambda: question_2("Z")

# Don't forget to push!


