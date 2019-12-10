from vpython import *
import numpy as np 
import math
scene = canvas(title='Leg Animation', background=color.white, forward=vector(0,1,0), up=vector(0,0,1))

#x red y green z blue

stepSize = 0.1
stepHeight = 1
accuracy = 4  # Amount of decimals

alpha = -0.683
beta= 1.185
gamma= -1.865

scalefactor= 100
l_c = 0.035 * scalefactor
l_f = 0.065* scalefactor
l_t = 0.096* scalefactor


trajectory = []

for i in np.arange(-1, 1, stepSize):
    #print(round(i, accuracy))
    x = round(i, accuracy)
    y = 0
    z = round(stepHeight * math.cos((math.pi / 2) * i), accuracy)

    trajectory.append([x,y,z])
    #                 [--------------x------- , y, -------------z----------------------------------------, 1] 
    #trajectory.append([round(i, accuracy), 0, np.abs(stepHeight * math.cos((math.pi / 2) * i), accuracy), 1])

for i in np.arange(1, -1, -stepSize):
    #print(round(i, accuracy))
    x = round(i, accuracy)
    y = 0
    z = 0 #round(stepHeight * math.cos((math.pi / 2) * i), accuracy)

    trajectory.append([x,y,z])


A1 = np.array([
            [math.cos(alpha), 0, math.sin(alpha), l_c * math.cos(alpha)],
            [math.sin(alpha), 0, -math.cos(alpha), l_c * math.sin(alpha)],
            [0, 1, 0, 0],
            [0, 0, 0, 1]])

A2 = np.array([
            [math.cos(beta), -math.sin(beta), 0,  l_f * math.cos(beta)],
            [math.sin(beta), math.cos(beta), 0,  l_f * math.sin(beta)],
            [0, 1, 0, 0],
            [0, 0, 0, 1]])

betaMatrix = np.matmul(A1, A2)

print("Matrix Beta: ", betaMatrix)

gammaP = vector(betaMatrix[0][3],betaMatrix[1][3],betaMatrix[2][3])
#print("BetaP: ", betaP)

#print("Tra :", trajectory)

ref_x = arrow(pos= vector(0,0,0), axis=vector(2,0,0), color= color.red)
text(text='x', pos=vec(2,0,0), color=color.red, height=0.5,billboard=True)
ref_y = arrow(pos= vector(0,0,0), axis=vector(0,2,0), color= color.green)
text(text='y', pos=vec(0,2,0), color=color.green, height=0.5,billboard=True)
ref_z = arrow(pos= vector(0,0,0), axis=vector(0,0,2), color= color.blue)
text(text='z', pos=vec(0,0,2), color=color.blue, height=0.5,billboard=True)

jointColor = color.red

#alphaJoint = sphere(pos= vector(0,0,0), radius= 0.5, color=color.red)
#betaJoint = sphere(pos=vector(-3,4,0), radius=0.5, color = color.orange)
#gammaJoint = sphere(pos=vector(-6,6,0), radius=0.5, color= color.green)







#rod_lc=cylinder(pos=vector(0,0,0),axis=vector(l_c,0,0), radius=0.2, color=color.blue)
#rod_lf=cylinder(pos=vector(l_c,0,0),axis=vector(l_f,0,0), radius=0.2, color=color.cyan)
#rod_lt=cylinder(pos=vector(l_f,0,0),axis=vector(l_t,0,0), radius=0.2, color=color.green)




alphaP = vector(0,0,0)
#rod_lc.rotate(angle=alpha,axis=vector(0,0,1))


betaP = vector(l_c*cos(alpha), l_c*sin(alpha),0)


#betaJoint=sphere(pos=betaP, radius=0.3, color= color.green)
#rod_lf.pos=betaP
#rod_lf.rotate(angle=alpha,axis=vector(0,0,1))
#rod_lf.rotate(angle=-beta,axis=vector(1,0,0))
#gammaP = vector(l_t*cos(gamma), -l_t*sin(gamma),0)
#gammaJoint=sphere(pos=gammaP, radius=0.3, color= color.yellow)
#rod_lt.pos=gammaP
#rod_lt.rotate(angle=alpha,axis=vector(0,0,1))
#rod_lt.rotate(angle=beta,axis=vector(0,1,0))
#rod_lt.rotate(angle=gamma,axis=vector(1,0,0))
footP=vector(0.1181*scalefactor,-0.0961*scalefactor,0)

length_lc = mag(betaP-alphaP)
length_lf = mag(gammaP-betaP)
print("Länge lc gemessen: ",l_c)
print("Länge lc berechnet: ",length_lc)
print("Länge lf gemessen: ",l_f)
print("Länge lf berechnet: ",length_lf)
curve(alphaP, betaP, gammaP, footP,radius=0.5)

sphere(pos=vector(0.1181*scalefactor,-0.0961*scalefactor,0), radius=0.8, color= color.green)


testF= sphere(radius=0.3, color = color.yellow)
#p1 = dict(pos=v1, color=color.red,  radius=0.1)
#p2 = dict(pos=v2, color=color.blue, radius=0.1)
#p3 = dict(pos=v3, color=color.blue, radius=0.1)

#c = curve(visible=True, radius=0.1)
#c.append(alphaP, betaP, gammaP, footP)


#alphaJoint=sphere(pos=alphaP, radius=0.3)
#betaJoint=sphere(pos=betaP, radius=0.3)
#gammaJoint=sphere(pos=gammaP, radius=0.3)
#foot=sphere(pos=footP, radius=0.3)




z=vector(0,0,1)
angle = 0.1
rounds = 0

while (rounds <= 3):
    i =0

    while (i in range(0,len(trajectory),1)):
        rate(10)
  
        testF.pos = vector(trajectory[i][0], trajectory[i][1], trajectory[i][2])


        #c.modify(4, vector())
        #c.rotate(angle=angle, axis = z)
    
        #print("Angle: ", angle)
        i = i+1
    rounds = rounds + 1
    