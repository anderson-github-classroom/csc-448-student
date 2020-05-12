import sys
sys.path.append(".")

# Import the student solutions
import Lab6

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab6.joblib")
print("Keys",answers.keys())

import numpy as np
answer_tol = 1e-10

def test_exercise_1():
    answer = Lab6.trie_construction(Lab6.patterns2)
    assert np.all(Lab6.to_adj(answer).values == answers['answer_exercise_1'].values)
    
def test_exercise_2():
    answer = Lab6.trie_matching("bananablahblahantennanabnablkjdf",Lab6.trie2)
    assert np.all(tuple(answer) == tuple(answers['answer_exercise_2']))
    
def test_exercise_3():
    answer = Lab6.suffix_trie("panamabananas$")
    assert np.all(Lab6.to_adj(answer).values == answers['answer_exercise_3'].values)
    
def test_exercise_4():
    answer,discard = Lab6.modified_suffix_trie("panamabananas$")
    assert np.all(Lab6.to_adj(answer).values == answers['answer_exercise_4'].values)
    
def test_exercise_5():
    answer = Lab6.suffix_tree_construction("panamabananas$")
    assert np.all(Lab6.to_adj(answer).values == answers['answer_exercise_5'].values)
