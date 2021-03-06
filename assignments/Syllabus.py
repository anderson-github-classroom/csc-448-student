# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "slide"} hideCode=false hidePrompt=false
# # Name(s)
# Your name here

# + [markdown] slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false
# **Instructions:** This is an individual assignment. Complete the following code and push to officially get your score.

# + [markdown] slideshow={"slide_type": "subslide"} hideCode=false hidePrompt=false
# I am providing the autograder answers locally so you may test your code before pushing. I will be reviewing your submissions, and if I find you are circumventing the autograder in any manner, you will receive a 0 on this assignment and your case will be reported to the honor board for review. i.e., approach the assignment in a genuine manner and you have nothing to worry about.

# + hideCode=false hidePrompt=false
#########################
# DO NOT EDIT
#########################

import os
if os.path.isdir('../src/'):
    src_dir = '../src/'
elif os.path.isdir('../csc-448-student/'):
    src_dir = '../csc-448-student/src/'
    
exec(open('%s/header.py'%src_dir).read()) # instructor repo

# + [markdown] slideshow={"slide_type": "slide"} hideCode=false hidePrompt=false
# ## Questions

# + hideCode=false slideshow={"slide_type": "subslide"} hidePrompt=false
manual_answers["question_1"] = widgets.RadioButtons(
            options=[
                'Monday morning',
                'Shortly after they are recorded on Friday',
                'Wednesday evening'
            ],
            layout={'width': 'max-content'},
            value = None
        )

widgets.Box(
    [
        widgets.Label(value='Question 1: When will new material be available each week?'),
        manual_answers["question_1"]
    ]
)

# + tags=["hide-input"] hideCode=false slideshow={"slide_type": "subslide"} hidePrompt=false
manual_answers["question_2"] = widgets.RadioButtons(
            options=[
                'Yes',
                'No. It is online and available.',
                'Textbooks are not important.'
            ],
            layout={'width': 'max-content'},
            value = None
        )

widgets.Box(
    [
        widgets.Label(value='Question 2: Do I need to buy the textbook?'),
        manual_answers["question_2"]
    ]
)

# + hideCode=false slideshow={"slide_type": "subslide"} hidePrompt=false
manual_answers["question_3"] = widgets.RadioButtons(
            options=[
                'Yes. The exact times are scheduled for each student, but Friday is always synchronous',
                'Yes. The exact times are scheduled for each student including Friday.',
                'No.'
            ],
            layout={'width': 'max-content'},
            value = None
        )

widgets.Box(
    [
        widgets.Label(value='Question 3: Are there required times to be synchronous and online?'),
        manual_answers["question_3"]
    ]
)

# + hideCode=false slideshow={"slide_type": "subslide"} hidePrompt=false
manual_answers["question_4"] = widgets.RadioButtons(
            options=[
                'Netbeans',
                'Java',
                'JupyterHub and Python'
            ],
            layout={'width': 'max-content'},
            value = None
        )

widgets.Box(
    [
        widgets.Label(value='Question 4: What software will I use to complete the assignments'),
        manual_answers["question_4"]
    ]
)

# + hideCode=false slideshow={"slide_type": "subslide"} hidePrompt=false
manual_answers["question_5"] = widgets.RadioButtons(
            options=[
                'If you want to get anything higher than a D, you\'ll need to do more than the labs and assignments',
                'No'
            ],
            layout={'width': 'max-content'},
            value = None
        )

widgets.Box(
    [
        widgets.Label(value='Question 5: Do I need to participate in this class?'),
        manual_answers["question_5"]
    ]
)

# + hideCode=false slideshow={"slide_type": "slide"} hidePrompt=false
# SUBMISSION INSTRUCTIONS
print("""
1. If there are any manual answers in this notebook, scroll to the top and click the button labelled 'Update ...'.
2. Save your notebook and do the standard git add, git commit, git push.
3. Verify your score in GitHub classroom.
""")
