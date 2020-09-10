# e.g., exec(open('../src/header.py').read())

########################################
# DO NOT EDIT
########################################
import joblib
 
try:
    from IPython.display import display
    display('Verifying you can use display')
except:
    display = print
    
import json
from ipywidgets import Button, Layout
import ipywidgets as widgets
from varname import nameof

manual_answers = {} # keeps track of the answers that are not in the form of code

button = widgets.Button(description="Update your manually entered answers (this is not done automatically)!",
                        layout=Layout(width='100%'))
#output = widgets.Output()

#display(button, output)

text_area = widgets.HTML(
    value='',
    placeholder='Nothing saved in this session',
    description=''
)

def on_button_clicked(b):
    #with output:
    manual_answers_saved = {}
    for question in manual_answers.keys():
        manual_answers_saved[question] = manual_answers[question].value

    joblib.dump(manual_answers_saved,"manual_answers_Syllabus.joblib");
    lines = ['Successfully saved your answers. You must still submit them.']
    lines.append('You answers were')
    lines.append(json.dumps(manual_answers_saved, indent=4, sort_keys=True).replace("\n","<br>"))
    text_area.value = "<br>".join(lines)

button.on_click(on_button_clicked)

def save_answer(widget):
    with output:
        manual_answers[nameof(widget)] = widget.value
    
try:
    import pygraphviz
    graphviz_installed = True # Set this to False if you don't have graphviz
except:
    graphviz_installed = False
    
display(button)
display(text_area)
