import sys
sys.path.append(".")

# Import the student solutions
import Proteomics 

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

def test_question_1():
    assert len(Proteomics.answer.strip()) >= 150 
    
