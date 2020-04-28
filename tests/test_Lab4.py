import sys
sys.path.append(".")

# Import the student solutions
import Lab4

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab4.joblib")
print("Keys",answers.keys())

def test_exercise_1():
    assert Lab4.greedy_lcs("AACCTTGG","ACACTGTGA",seed=1000) == answers['answer_exercise_1']
    
def test_exercise_2():
    assert Lab4.greedy_alignment("AACCTTGG","ACACTGTGA",seed=1000) == answers['answer_exercise_2']
    
def test_exercise_3():
    assert Lab4.min_num_coins(27,[6,5,1]) == answers['answer_exercise_3']
    
def test_exercise_4():
    assert Lab4.min_num_coins_dynamic(27,[6,5,1]) == answers['answer_exercise_4']
    
def test_exercise_5():
    assert Lab4.align("AACCT","ACACTG") == answers['answer_exercise_5']
    
def test_exercise_6():
    assert Lab4.align_dynamic("AACCT","ACACTG") == answers['answer_exercise_6']
    
def test_exercise_7():
    assert Lab4.align_dynamic2("AACCT","ACACTG") == answers['answer_exercise_7']


