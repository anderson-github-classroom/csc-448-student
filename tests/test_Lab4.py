import sys
sys.path.append(".")

# Import the student solutions
import Lab4

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab4.joblib")
print("Keys",answers.keys())

import numpy as np
answer_tol = 1e-10

def test_exercise_1():
    answer = Lab4.spectrum_graph_construction(Lab4.spectrum1)
    assert np.all(Lab4.to_adj(answer).values == answers['answer_exercise_1'].values)

def test_exercise_2():
    answer = Lab4.ideal_spectrum("REDCA")
    assert np.all(answer == answers['answer_exercise_2'])

def test_exercise_3():
    answer = Lab4.decoding_ideal_spectrum(Lab4.spectrum5)
    assert len(set(answer).difference(set(answers['answer_exercise_3']))) == 0

def test_exercise_4():
    answer = Lab4.construct_peptide_vector("XZZXX")
    assert np.all(answer == answers['answer_exercise_4'])

def test_exercise_5():
    p = np.array([0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1])
    answer = Lab4.construct_peptide_from_vector(p)
    assert np.all(answer == answers['answer_exercise_5'])
    
def test_exercise_6():
    p2 = [0,0,0,4,-2,-3,-1,-7,6,5,3,2,1,9,3,-8,0,3,1,2,1,0]
    answer = Lab4.max_peptide(p2,debug=False)
    assert answer == answers['answer_exercise_6']
