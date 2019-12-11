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






#0,0,-90 deg
alpha= 0.0 
beta=0.7854
gamma= -1.5707963267948966



scalefactor= 100
l_c = 0.035 * scalefactor
l_f = 0.065 * scalefactor
l_t = 0.096 * scalefactor


stepSize = 0.1
stepHeight = 1
accuracy = 4  # Amount of decimals

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

A3 = np.array([
    [math.cos(gamma), -math.sin(gamma), 0, l_t * math.cos(gamma)],
    [math.sin(gamma), math.cos(gamma), 0, l_t * math.sin(gamma)],
    [0, 1, 0, 0],
    [0, 0, 0, 1]])

betaMatrix = np.matmul(A1, A2)



gammaP = vector(betaMatrix[0][3],betaMatrix[1][3],betaMatrix[2][3])
#print("BetaP: ", betaP)

#print("Tra :", trajectory)


footX = math.cos(alpha) * (l_t * math.cos(beta + gamma) + l_f * math.cos(beta) + l_c)
footY = math.sin(alpha) * (l_t * math.cos(beta + gamma) + l_f * math.cos(beta) + l_c)
footZ = l_t * math.sin(beta + gamma) + l_f * math.sin(beta)

footP= vector(footX, footY, footZ)



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



#footP=vector(0.1181*scalefactor,-0.0961*scalefactor,0)

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




testF= sphere(radius=0.3, color = color.yellow)

z=vector(0,0,1)
angle = 0.1
rounds = 0

while (rounds <= 3):
    i =0

    while (i in range(0,len(trajectory),1)):
        rate(10)
  
        testF.pos = vector(trajectory[i][0], trajectory[i][1], trajectory[i][2])
        i = i+1
    rounds = rounds + 1
    