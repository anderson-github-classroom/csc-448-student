import sys
sys.path.append(".")

# Import the student solutions
import Lab3

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab3.joblib")
print("Keys",answers.keys())

import numpy as np
import networkx as nx

def test_exercise_1():
    assert tuple(Lab3.composition(3,"TATGGGGTGC")) == answers['answer_exercise_1']

def test_exercise_2():
    assert np.all(nx.adjacency_matrix(Lab3.de_bruijn(["AAT","ATG","ATG","ATG","CAT","CCA","GAT","GCC","GGA","GGG","GTT","TAA","TGC","TGG","TGT"])) == answers['answer_exercise_2'])

def test_exercise_3():
    assert tuple(Lab3.eulerian_cycle(Lab3.G,start=6)) == answers['answer_exercise_3']

def test_exercise_4():
    assert tuple(Lab3.eulerian_path(Lab3.G2)) == answers['answer_exercise_4']

def test_exercise_5():
    assert Lab3.reconstruct(Lab3.kmers) == answers['answer_exercise_5']

# git clone https://github.com/anderson-github-classroom/csc-448-student ../csc-448-student && sudo -H pip3 install -r ../csc-448-student/requirements.txt

# pytest ../csc-448-student/tests/test_Lab1.py::test_exercise_1
