import sys
sys.path.append(".")

import Syllabus
import answers

def test_answer_question_1():
    assert Syllabus.answer_question_1() == ANSWERS['csc-448-instructor/tests/test_Syllabus.py::test_answer_question_1']
    
def test_answer_question_2():
    assert Syllabus.answer_question_2() == ANSWER['csc-448-instructor/tests/test_Syllabus.py::test_answer_question_2']