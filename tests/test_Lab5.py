import sys
sys.path.append(".")

# Import the student solutions
import Lab5

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab5.joblib")
print("Keys",answers.keys())

def test_exercise_1():
    pi = "FFFFBBBBFBFBBB"
    answer = prob_path(pi,Lab5.coin_hmm)
    assert answer == answers['answer_exercise_1']

def test_exercise_2():
    x = "HHHHTTHTTTHHHH"
    pi = "FFFFBBBBFBFBBB"
    assert Lab5.prob_outcome_path(x,pi,Lab5.coin_hmm) == answers['answer_exercise_2']

def test_exercise_3():
    x = "HHHHHHTTTTTT"
    answer = Lab5.decode_path(x,Lab5.coin_hmm2)
    assert answer == answers['answer_exercise_3']

def test_exercise_4():
    x = "HHHHHHTTTTTT"
    answer = Lab5.likelihood_x(x,Lab5.coin_hmm2)
    assert answer == answers['answer_exercise_4']