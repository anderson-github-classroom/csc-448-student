import sys
sys.path.append(".")

# Import the student solutions
import Lab1

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab1.joblib")

def test_exercise_1():
    assert Lab1.count("ACAACTATGCATACTATCGGGAACTATCCT","ACTAT") == answers['answer_exercise_1a']
    
def test_exercise_2():
    assert Lab1.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT",4) == answers['answer_exercise_2a']

def test_question_1():
    assert Lab1.answer_question_1() == answers['answer_question_1']

def test_exercise_3():
    assert Lab1.reverse_complement("cagt") == answers['answer_exercise_3']
    
def test_exercise_4():
    assert Lab1.frequency_table(Lab1.text,3) == answers["answer_exercise_4"]

def test_exercise_5():
    assert Lab1.better_frequent_words(Lab1.text,9) == answers["answer_exercise_5"]
    
def test_exercise_6():
    assert Lab1.skew(Lab1.genome) == answers["answer_exercise_6"]

# Manual answers
manual_answers = joblib.load("manual_answers_Syllabus.joblib")

def test_question_1():
    assert manual_answers['question_1'] == answers['question_1']
