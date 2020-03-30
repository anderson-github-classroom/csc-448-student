import sys
sys.path.append(".")

import Syllabus

def test_answer_question_1():
    assert Syllabus.answer_question_1() == Syllabus.question_1("B")
    
def test_answer_question_2():
    assert Syllabus.answer_question_2() == Syllabus.question_2("A")