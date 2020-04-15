import sys
sys.path.append(".")

# Import the student solutions
import Lab2

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab2.joblib")

import networkx as nx
import numpy as np
import copy

D = copy.copy(Lab2.Dorig)
limbLength = Lab2.limb(D,D.index[-1]) # our algorithm will choose the last node
n = D.index[-1]
Dtrimmed = D.drop(n).drop(n,axis=1)
for j in Dtrimmed.index:
    D.loc[j,n] = D.loc[j,n] - limbLength
    D.loc[n,j] = D.loc[j,n]

def test_exercise_1():
    assert (Lab2.compute_d(Lab2.G) == answers['answer_exercise_1']).all().all()

def test_exercise_2():
    assert Lab2.limb(Lab2.Dorig,"v4") == answers['answer_exercise_2']

def test_exercise_3a():
    assert Lab2.find(D,"v4") == answers['answer_exercise_3a']
    
def test_exercise_3b():
    assert np.all(nx.adjacency_matrix(Lab2.base_case(Lab2.Dorig.iloc[:2,:].iloc[:,:2])).todense() == answers['answer_exercise_3b'])
    
def test_exercise_4():
    assert np.all(nx.adjacency_matrix(Lab2.additive_phylogeny(Lab2.D_sars,len(Lab2.D_sars)+1)).todense() == answers['answer_exercise_4'])
    
# git clone https://github.com/anderson-github-classroom/csc-448-student ../csc-448-student && sudo -H pip3 install -r ../csc-448-student/requirements.txt

# pytest ../csc-448-student/tests/test_Lab1.py::test_exercise_1