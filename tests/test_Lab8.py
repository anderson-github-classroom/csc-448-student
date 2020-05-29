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
import pandas as pd
answer_tol = 1e-10

def test_exercise_1():
    num_blocks = len(Lab8.lens)
    assert num_blocks == answers['exercise_1_num_blocks']
    lower = np.all(Lab8.counts > answers['exercise_1_means'] - 3*answers['exercise_1_stdevs'])
    assert lower
    upper = np.all(Lab8.counts < answers['exercise_1_means'] + 3*answers['exercise_1_stdevs'])
    assert upper

def test_exercise_2():
    answer = Lab8.greedy_sorting(Lab8.P)
    assert answers["exercise_2"] == answer
    
def test_exercise_3():
    P_list2 = [3,4,5,-12,-8,-7,-6,1,2,10,9,-11,13,14]
    P2 = pd.Series(P_list2,index=list(range(1,len(P_list2)+1)))
    nbreakpoints_P2 = Lab8.count_breakpoints(P2)
    P_list3 = [3,4,5,-12,-8,-7,-6,1,2,10,9,-11,14,13]
    P3 = pd.Series(P_list3,index=list(range(1,len(P_list2)+1)))
    nbreakpoints_P3 = Lab8.count_breakpoints(P3)
    assert answers["exercise_3_nbreakpoints_P2"] == nbreakpoints_P2
    assert answers["exercise_3_nbreakpoints_P3"] == nbreakpoints_P3
    
def test_exercise_4():
    P_list2 = [3,4,5,-12,-8,-7,-6,1,2,10,9,-11,13,14]
    P2 = pd.Series(P_list2,index=list(range(1,len(P_list2)+1)))
    nbreakpoints_P2 = Lab8.count_breakpoints(P2)
    P_list3 = [3,4,5,-12,-8,-7,-6,1,2,10,9,-11,14,13]
    P3 = pd.Series(P_list3,index=list(range(1,len(P_list2)+1)))
    nbreakpoints_P3 = Lab8.count_breakpoints(P3)
    assert answers["exercise_3_nbreakpoints_P2"] == nbreakpoints_P2
    assert answers["exercise_3_nbreakpoints_P3"] == nbreakpoints_P3
    
def test_exercise_5():
    G = Lab8.genome_to_graph([pd.Series([1,-2,-3,4]),pd.Series([5,6,7,8,9,10])])
    assert set(answers['exercise4_edge_list']) == set(Lab8.to_edge_list(G))

def test_exercise_6():
    P4_list = [1,-2,-3,4]
    P4 = pd.Series(P4_list)
    P5_list = [1,3,2,-4]
    P5 = pd.Series(P5_list)

    G_P4_P5 = Lab8.combine(Lab8.genome_to_graph([P4]),Lab8.genome_to_graph([P5]))
    assert answers['exercise5_edge_list'] == Lab8.to_edge_list(G_P4_P5)

def test_exercise_7():
    P4_list = [1,-2,-3,4]
    P4 = pd.Series(P4_list)
    P5_list = [1,3,2,-4]
    P5 = pd.Series(P5_list)
    ncycles = Lab8.cycles(Lab8.genome_to_graph([P4]),Lab8.genome_to_graph([P5]))
    assert answers['exercise6_ncycles'] == ncycles
    
def test_exercise_8():
    test_edge_cycle = [[1, -3], [-3, -4], [-4, -1], [-1, 4], [4, 2], [2, 1]]
    checked_cycle, colors = Lab8.red_blue_cycle_check(Lab8.G_P4_P5,test_edge_cycle)
    assert np.all(answers['exercise8_colors'] == colors)
    
def test_exercise_9():
    steps = Lab8.shortest_rearrangement_scenario([pd.Series([1,-2,-3,4])],[pd.Series([1,2,-4,-3])])
    assert answers['exercise9_last_step'] == steps[-1]
