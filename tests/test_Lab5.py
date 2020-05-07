import sys
sys.path.append(".")

# Import the student solutions
import Lab5

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab5.joblib")
print("Keys",answers.keys())

import numpy as np
answer_tol = 1e-10

def test_exercise_1():
    pi = "FFFFBBBBFBFBBB"
    answer = Lab5.prob_path(pi,Lab5.coin_hmm)
    assert np.abs(answer - answers['answer_exercise_1']) <= answer_tol

def test_exercise_2():
    x = "HHHHTTHTTTHHHH"
    pi = "FFFFBBBBFBFBBB"
    assert np.abs(Lab5.prob_outcome_path(x,pi,Lab5.coin_hmm) - answers['answer_exercise_2']) <= answer_tol

def test_exercise_3():
    x = "HTHTHTHTHHHHHHHTTTTTT"
    answer = Lab5.decode_path(x,Lab5.coin_hmm2)
    assert answer == answers['answer_exercise_3']

def test_exercise_4():
    x = "HTHTHTHTHHHHHHHTTTTTT"
    answer = Lab5.likelihood_x(x,Lab5.coin_hmm2)
    assert np.abs(answer - answers['answer_exercise_4']) <= answer_tol