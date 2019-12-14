from vpython import *
from decimal import *
import numpy as np 
import math



def createScene():
    scene = canvas(title='Leg Visualisation', width=800, height=800, background=color.white, forward=vector(0,1,0), up=vector(0,0,1))

    #x red y green z blue
    ref_x = arrow(pos= vector(0,0,0), axis=vector(2,0,0), shaftwidth=0.1, color= color.red)
    text(text='x', pos=vec(2,0,0.4), color=color.red, height=0.5,billboard=True)
    ref_y = arrow(pos= vector(0,0,0), axis=vector(0,2,0), shaftwidth=0.1, color= color.green)
    text(text='y', pos=vec(0,2,0), color=color.green, height=0.5,billboard=True)
    ref_z = arrow(pos= vector(0,0,0), axis=vector(0,0,2), shaftwidth=0.1, color= color.blue)
    text(text='z', pos=vec(0,0,2), color=color.blue, height=0.5,billboard=True)
    print("Scene created.")



def drawLeg(angle, length, offsetx, offsetz, legColor):
    alpha = angle[0]
    beta = angle[1]
    gamma = angle[2]

    scalefactor= 100
    l_c = length[0] *scalefactor
    l_f = length[1]*scalefactor
    l_t = length[2]*scalefactor

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

    origin = vector(0,0,0)
    alphaP = vector(offsetx,0,offsetz)
    betaP = vector(l_c*cos(alpha) + offsetx, l_c*sin(alpha),offsetz)
    gammaP = vector(betaMatrix[0][3] + offsetx,betaMatrix[1][3],betaMatrix[2][3]+offsetz)
    footP= vector(footX+offsetx, footY, footZ+offsetz)


    length_lc = mag(betaP-alphaP)
    length_lf = mag(gammaP-betaP)
    length_lt = mag(gammaP-footP)
    '''
    print("Länge lc gemessen: ",l_c)
    print("Länge lc berechnet: ",length_lc)
    print("Länge lf gemessen: ",l_f)
    print("Länge lf berechnet: ",length_lf)
    print("Länge lt gemessen: ",l_t)
    print("Länge lt berechnet: ",length_lt)
    print("footP: ", footX,", ",footY,", ",footZ)
    '''

    box(pos=origin, color = color.red)
    sphere(pos=alphaP, color = color.green)
    sphere(pos=betaP, color = color.cyan)
    sphere(pos=gammaP, color = color.blue)
    sphere(pos=footP, color = color.magenta)

    curve(origin, alphaP, betaP, gammaP, footP,radius=0.3, color = legColor)


def testTraj():
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
    