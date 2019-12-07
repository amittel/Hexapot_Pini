from vpython import *
import numpy as np 
import math
scene = canvas(title='Leg Animation', background=color.white, forward=vector(0,1,0), up=vector(0,0,1))

#x red y green z blue

stepSize = 0.1
stepHeight = 1
accuracy = 4  # Amount of decimals


trajectory = []

for i in np.arange(-1, 1, stepSize):
    print(round(i, accuracy))
    x = round(i, accuracy)
    y = 0
    z = round(stepHeight * math.cos((math.pi / 2) * i), accuracy)

    trajectory.append([x,y,z])
    #                 [--------------x------- , y, -------------z----------------------------------------, 1] 
    #trajectory.append([round(i, accuracy), 0, np.abs(stepHeight * math.cos((math.pi / 2) * i), accuracy), 1])

for i in np.arange(1, -1, -stepSize):
    print(round(i, accuracy))
    x = round(i, accuracy)
    y = 0
    z = 0 #round(stepHeight * math.cos((math.pi / 2) * i), accuracy)

    trajectory.append([x,y,z])

print("Tra :", trajectory)

ref_x = arrow(pos= vector(0,0,0), axis=vector(2,0,0), color= color.red)
text(text='x', pos=vec(2,0,0), color=color.red, height=0.5,billboard=True)
ref_y = arrow(pos= vector(0,0,0), axis=vector(0,2,0), color= color.green)
text(text='y', pos=vec(0,2,0), color=color.green, height=0.5,billboard=True)
ref_z = arrow(pos= vector(0,0,0), axis=vector(0,0,2), color= color.blue)
text(text='z', pos=vec(0,0,2), color=color.blue, height=0.5,billboard=True)

#alphaJoint = sphere(pos= vector(0,0,0), radius= 0.5, color=color.red)
#betaJoint = sphere(pos=vector(-3,4,0), radius=0.5, color = color.orange)
#gammaJoint = sphere(pos=vector(-6,6,0), radius=0.5, color= color.green)
scalefactor= 100
l_c = 0.035 * scalefactor
l_f = 0.065* scalefactor
l_t = 0.096* scalefactor

alphaP = vector(0,0,0)
betaP = vector(l_c,0,0)
gammaP = vector(l_f,0,0)
footP = vector(l_t,0,0)

testF= sphere(radius=0.3, color = color.yellow)
#p1 = dict(pos=v1, color=color.red,  radius=0.1)
#p2 = dict(pos=v2, color=color.blue, radius=0.1)
#p3 = dict(pos=v3, color=color.blue, radius=0.1)

c = curve(visible=True, radius=0.1)
c.append(alphaP, betaP, gammaP, footP)
z=vector(0,0,1)
angle = 0.1
rounds = 0

while (rounds <= 3):
    i =0

    while (i in range(0,len(trajectory),1)):
        rate(10)
  
        testF.pos = vector(trajectory[i][0], trajectory[i][1], trajectory[i][2])
    
        #c.rotate(angle=angle, axis = z)
    
        #print("Angle: ", angle)
        i = i+1
    rounds = rounds + 1
    