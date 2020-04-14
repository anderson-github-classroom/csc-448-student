import sys
sys.path.append(".")

# Import the student solutions
import Lab2

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Lab2.joblib")

import networkx as nx

def test_exercise_1():
    assert (Lab2.compute_d(Lab2.G) == answers['answer_exercise_1']).all()

def test_exercise_2():
    assert Lab2.limb(Lab2.Dorig,"v4") == answers['answer_exercise_2']

def test_exercise_3a():
    assert Lab2.find(Lab2.Dorig,"v4") == answers['answer_exercise_3a']
    
def test_exercise_3b():
    assert nx.adjacency_matrix(Lab2.base_case(Lab2.Dorig.iloc[:2,:].iloc[:,:2])).todense() == answers['answer_exercise_3b']
    
def test_exercise_3c():
    assert nx.adjacency_matrix(Lab2.additive_phylogeny(Lab2.Dorig,len(Lab2.Dorig)+1)).todense() == answers['answer_exercise_3c']