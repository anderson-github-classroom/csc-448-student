import sys
sys.path.append(".")

# Import the student solutions
#import Syllabus # fix jupytext

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Syllabus.joblib")

manual_answers = joblib.load("manual_answers_Syllabus.joblib")

def test_question_1():
    assert manual_answers['question_1'] == answers['question_1']
    
def test_question_2():
    assert manual_answers['question_2'] == answers['question_2']
    
def test_question_3():
    assert manual_answers['question_3'] == answers['question_3']
    
def test_question_4():
    assert manual_answers['question_4'] == answers['question_4']
    
def test_question_5():
    assert manual_answers['question_5'] == answers['question_5']