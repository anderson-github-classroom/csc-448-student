import sys
sys.path.append(".")

# Import the student solutions
import Lab8

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab8.joblib")
print("Keys",answers.keys())

import numpy as np
answer_tol = 1e-10

def test_exercise_1():
    num_blocks = len(Lab8.lens)
    assert num_blocks == answers['exercise_1_num_blocks']
    lower = np.all(Lab8.counts > answers['exercise_1_means'] - 3*answers['exercise_1_stdevs'])
    assert lower
    upper = np.all(Lab8.counts < answers['exercise_1_means'] + 3*answers['exercise_1_stdevs'])
    assert upper
