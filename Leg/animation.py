from vpython import *

scene = canvas(title='Leg Animation', background=color.white)

#x red y green z blue


ref_x = arrow(pos= vector(0,0,0), axis=vector(2,0,0), color= color.red)
text(text='x', pos=vec(2,0,0), color=color.red, height=0.5,billboard=True)
ref_y = arrow(pos= vector(0,0,0), axis=vector(0,2,0), color= color.green)
text(text='y', pos=vec(0,2,0), color=color.green, height=0.5,billboard=True)
ref_z = arrow(pos= vector(0,0,0), axis=vector(0,0,2), color= color.blue)
text(text='z', pos=vec(0,0,2), color=color.blue, height=0.5,billboard=True)

alphaJoint = sphere(pos= vector(0,0,0), radius= 0.5, color=color.red)
betaJoint = sphere(pos=vector(-3,4,0), radius=0.5, color = color.orange)
gammaJoint = sphere(pos=vector(-6,6,0), radius=0.5, color= color.green)
