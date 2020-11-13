import sys
sys.path.append(".")

# Import the student solutions
import Lab9

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab9.joblib")
print("Keys",answers.keys())

import numpy as np
answer_tol = 1e-10

def test_exercise_1():
    pi = "FFFFBBBBFBFBBB"
    answer = Lab9.prob_path(pi,Lab9.coin_hmm)
    assert np.abs(answer - answers['answer_exercise_1']) <= answer_tol

def test_exercise_2():
    x = "HHHHTTHTTTHHHH"
    pi = "FFFFBBBBFBFBBB"
    assert np.abs(Lab9.prob_outcome_path(x,pi,Lab9.coin_hmm) - answers['answer_exercise_2']) <= answer_tol

def test_exercise_3():
    x = "HTHTHTHTHHHHHHHTTTTTT"
    answer = Lab9.decode_path(x,Lab9.coin_hmm2)
    assert answer == answers['answer_exercise_3']

def test_exercise_4():
    x = "HTHTHTHTHHHHHHHTTTTTT"
    answer = Lab9.likelihood_x(x,Lab9.coin_hmm2)
    assert np.abs(answer - answers['answer_exercise_4']) <= answer_tol
