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

# **Question 1.**
# When will new material be available each week?

## Do not modify this cell
def question_1(answer):
    answers = {
        "A": "Monday morning",
        "B": "Sunday night",
        "C": "Monday evening",
        "D": "I don't know"
    }
    return answers[answer]
## Do not modify this cell


# You can answer the question by defining an anonymous function. This creates a function that I can test using pytest. You don't have to worry about the details. You just need to answer the question by changing the string argument that is currently set to "D".

answer_question_1 = lambda: question_1("D") 


