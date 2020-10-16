import sys
sys.path.append(".")

# Import the student solutions
import Lab5

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab5.joblib")
print("Keys",answers.keys())

import networkx as nx
import numpy as np
import copy

D = copy.copy(Lab5.Dorig)
limbLength = Lab5.limb(D,D.index[-1]) # our algorithm will choose the last node
n = D.index[-1]
Dtrimmed = D.drop(n).drop(n,axis=1)
for j in Dtrimmed.index:
    D.loc[j,n] = D.loc[j,n] - limbLength
    D.loc[n,j] = D.loc[j,n]

def test_exercise_1():
    assert (Lab5.compute_d(Lab5.G) == answers['answer_exercise_1']).all().all()

def test_exercise_2():
    assert Lab5.limb(Lab5.Dorig,"v4") == answers['answer_exercise_2']

def test_exercise_3a():
    assert Lab5.find(D,"v4") == answers['answer_exercise_3a']
    
def test_exercise_3b():
    assert np.all(nx.adjacency_matrix(Lab5.base_case(Lab5.Dorig.iloc[:2,:].iloc[:,:2])).todense() == answers['answer_exercise_3b'])
    
def test_exercise_3c():
    assert np.all(nx.adjacency_matrix(Lab5.additive_phylogeny(Lab5.Dorig,len(Lab5.Dorig)+1)).todense() == answers['answer_exercise_3c'])

def test_exercise_4():
    assert np.all(nx.adjacency_matrix(Lab5.additive_phylogeny(Lab5.D_sars,len(Lab5.D_sars)+1)).todense() == answers['answer_exercise_4'])
    
# git clone https://github.com/anderson-github-classroom/csc-448-student ../csc-448-student && sudo -H pip3 install -r ../csc-448-student/requirements.txt

# pytest ../csc-448-student/tests/test_Lab1.py::test_exercise_1
