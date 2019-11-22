"""
pip install vpython
"""

from vpython import *


scene2 = canvas(title='Examples of Tetrahedrons',
     width=600, height=200,
     center=vector(5,0,0), background=color.cyan) 

points(canvas= scene2,pos=[vector(-1,0,0), vector(1,0,0)], radius=50,           color=color.red)