import math
import numpy as np
from vpython import *

import leg


vStart=vector(0, 0, 0)
vCoordAxes = vector(40, 0.4, 0.4)

leg = []


def trajectory(x_, y_, z_):
    stepSize = 0.1
    stepHeight = 1
    accuracy = 4  # Amount of decimals

    trajectory = []

    # TODO: insert Start and Stop Points according to given x_
    for i in np.arange(-1, 1, stepSize):
        x = x_
        y = round(i, accuracy)
        z = round(stepHeight * math.cos((math.pi / 2) * i), accuracy) + z_

        trajectory.append([x, y, z])

    for i in np.arange(1, -1, -stepSize):
        x = x_  # round(i, accuracy)
        y = round(i, accuracy)
        z = z_  # round(stepHeight * math.cos((math.pi / 2) * i), accuracy)

        trajectory.append([x, y, z])

    return trajectory


def draw_coordinates():
    cylinder(
            pos = vStart,
            axis = vector(1, 0, 0),
            size = vCoordAxes,
            color = color.blue,
            opacity = 0.5
    )
    cylinder(
            pos = vStart,
            axis = vector(0, 1, 0),
            size = vCoordAxes,
            color = color.green,
            opacity = 0.5
    )
    cylinder(
            pos = vStart,
            axis = vector(0, 0, 1),
            size = vCoordAxes,
            color = color.red,
            opacity = 0.5
    )

def populate_leg(pos_ax3_):
    global leg
    # ToDo: Calculate Position with current trajectory item
    ax1.pos = vector(4, 4, 4)
    ax2.pos = vector(10, 4, 6)
    ax3.pos = pos_ax3_
    leg = [vStart, ax1.pos,ax2.pos,pos_ax3_]


trac = trajectory(14.88,0,-2.19)
draw_coordinates()
scene.camera.pos = vector(10, 10, 0)
ax1 =  sphere(pos=vStart,size=vector(1, 1, 1))
ax2 = sphere(pos=vStart,size=vector(1, 1, 1))
ax3 = sphere(pos=vStart, size=vector(1, 1, 1))
connections = curve(pos=[vStart,vStart,vStart,vStart])

while(1):
    rate(1)
    for i in range(0, len(trac), 1):
        rate(10)
        pos_ax3 = vector(trac[i][0], trac[i][1], trac[i][2])
        populate_leg(pos_ax3)
        connections.modify(N=1, pos=ax1.pos)
        connections.modify(N=2, pos=ax2.pos)
        connections.modify(N=3, pos=ax3.pos)


