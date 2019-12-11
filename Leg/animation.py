from vpython import *
import numpy as np 
import math



scene = canvas(title='Leg Animation', width=800, height=800, background=color.white, forward=vector(0,1,0), up=vector(0,0,1))

#x red y green z blue
ref_x = arrow(pos= vector(0,0,0), axis=vector(2,0,0), shaftwidth=0.1, color= color.red)
text(text='x', pos=vec(2,0,0), color=color.red, height=0.5,billboard=True)
ref_y = arrow(pos= vector(0,0,0), axis=vector(0,2,0), shaftwidth=0.1, color= color.green)
text(text='y', pos=vec(0,2,0), color=color.green, height=0.5,billboard=True)
ref_z = arrow(pos= vector(0,0,0), axis=vector(0,0,2), shaftwidth=0.1, color= color.blue)
text(text='z', pos=vec(0,0,2), color=color.blue, height=0.5,billboard=True)






#0,45,-90 deg
alpha= 0.0 
beta=0.7854
gamma= -1.5707963267948966



scalefactor= 100
l_c = 0.035 * scalefactor
l_f = 0.065 * scalefactor
l_t = 0.096 * scalefactor



def trajectory(x_,y_,z_):
    stepSize = 0.1
    stepHeight = 1
    accuracy = 4  # Amount of decimals

    trajectory = []

    for i in np.arange(-1, 1, stepSize):
        x = x_
        y = round(i, accuracy)
        z = round(stepHeight * math.cos((math.pi / 2) * i), accuracy) +z_

        trajectory.append([x,y,z])
        

    for i in np.arange(1, -1, -stepSize):
        x = x_ #round(i, accuracy)
        y = round(i, accuracy)
        z = z_ #round(stepHeight * math.cos((math.pi / 2) * i), accuracy)

        trajectory.append([x,y,z])

    return trajectory


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

A3 = np.array([
    [math.cos(gamma), -math.sin(gamma), 0, l_t * math.cos(gamma)],
    [math.sin(gamma), math.cos(gamma), 0, l_t * math.sin(gamma)],
    [0, 1, 0, 0],
    [0, 0, 0, 1]])

betaMatrix = np.matmul(A1, A2)

#ToDo: Selbe wie fKin -> aufrufen
footX = math.cos(alpha) * (l_t * math.cos(beta + gamma) + l_f * math.cos(beta) + l_c)
footY = math.sin(alpha) * (l_t * math.cos(beta + gamma) + l_f * math.cos(beta) + l_c)
footZ = l_t * math.sin(beta + gamma) + l_f * math.sin(beta)


alphaP = vector(0,0,0)
betaP = vector(l_c*cos(alpha), l_c*sin(alpha),0)
gammaP = vector(betaMatrix[0][3],betaMatrix[1][3],betaMatrix[2][3])
footP= vector(footX, footY, footZ)


length_lc = mag(betaP-alphaP)
length_lf = mag(gammaP-betaP)
length_lt = mag(gammaP-footP)
print("Länge lc gemessen: ",l_c)
print("Länge lc berechnet: ",length_lc)
print("Länge lf gemessen: ",l_f)
print("Länge lf berechnet: ",length_lf)
print("Länge lt gemessen: ",l_t)
print("Länge lt berechnet: ",length_lt)
print("footP: ", footX,", ",footY,", ",footZ)


curve(alphaP, betaP, gammaP, footP,radius=0.3)



# Testsuite Trajectory
testF = sphere(pos=vector(14.88,0,-2.192),radius=0.3, color = color.yellow)
traj = trajectory(14.88,0,-2.19)

rounds = 0

while (rounds <= 13):
    i =0

    while (i in range(0,len(traj),1)):
        rate(10)
  
        testF.pos = vector(traj[i][0], traj[i][1], traj[i][2])
        i = i+1
    rounds = rounds + 1
    