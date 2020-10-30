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

def to_edge_list(T):
    return list(T.edges())

def fix_edge_list(edge_list):
    for i in range(len(edge_list)):
        edge_list[i] = tuple(np.sort(edge_list[i]))
    return edge_list

def test_exercise_1():
    answer = Lab6.trie_construction(Lab6.patterns2)
    assert set(fix_edge_list(to_edge_list(answer))) == set(fix_edge_list(to_edge_list(answers['answer_exercise_1'])))
    
def test_exercise_2():
    answer = Lab6.trie_matching("bananablahblahantennanabnablkjdf",Lab6.trie2)
    assert np.all(tuple(answer) == tuple(answers['answer_exercise_2']))
    
def test_exercise_3():
    answer = Lab6.suffix_trie("panamabananas$")
    assert set(fix_edge_list(to_edge_list(answer))) == set(fix_edge_list(to_edge_list(answers['answer_exercise_3'])))
    
def test_exercise_4():
    answer,discard = Lab6.modified_suffix_trie("panamabananas$")
    assert set(fix_edge_list(to_edge_list(answer))) == set(fix_edge_list(to_edge_list(answers['answer_exercise_4'])))
    
def test_exercise_5():
    answer = Lab6.to_adj(Lab6.suffix_tree_construction("panamabananas$"))
    instructor_answer = answers['answer_exercise_5']
    answer_order = list(instructor_answer.index)
    answer = answer.loc[answer_order,answer_order]
    assert np.all(answer.values == instructor_answer.values)
