# Getting the imports right.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import time
import copy
import os
import math
import numpy as np
#import matplotlib.pyplot as plt
#import mpl_toolkits.mplot3d.axes3d as p3
#import mpl_toolkits.mplot3d.art3d as art3d
import enum

from Leg.leg import Leg
import Servo.jointdrive
from Gui.PyCOM import testCom
#Enum to change walking modes
class WalkingMode(enum.Enum):
    COSINE = 0
    TRAPEZOID = 1


class Robot:

    def __init__(self, isReal):
        self.isReal = isReal  # Flag if the robot is simulated (animation) or real (no animation)
        self.stepSize = 0.1  # Spacing of trajectory points
        self.stepHeight = 0.5  # Working area from 0 to 1
        self.MINSTEPHEIGHT = 0.3 #Defines minimum Stepheight
        self.accuracy = 4  # Amount of decimals
        self.walkingMode = WalkingMode.COSINE # Default Walkingmode
        self.trajectory = self.createTrajectory()
        self.cycleTime = 1  # Time for each move (Simulation)
        self.CYCLETIMEMIN = 0.05 # Highest possible speed # TODO Testen was geht
        self.CYCLETIMEMAX = 1 # Lowest desired speed
        self.walkingAngle = 0  # Current movement angle
        self.legs = []
        self.Homepositions= [(0.15,-0.08,-0.08),(0.15,0.08,-0.08),(0,0.18,-0.08),
                             (-0.075,+0.08,-0.08),(-0.075,+0.08,-0.08),(0,-0.16,-0.08)]
        # Group 1 starts swinging
        # Consists of front right, middle left and back right
        self.legsGroup1 = [0, 2, 4]
        # Group 2 starts stemming
        # Consists of front left, middle right and back left
        self.legsGroup2 = [1, 3, 5]

        if self.isReal:
            # COM-Object for input from GUI
            self.com = testCom.testCom(port="5555")
            print(self.com.readData())
            #Legs
            self.legs.append(Leg( 1, [1,3,5], [True,False,True]))
            self.legs.append(Leg( 2, [2,4,6], [True,True,False]))
            self.legs.append(Leg( 3, [8,10,12], [True,False,True]))
            self.legs.append(Leg( 4, [14,16,18], [True,False,True]))
            self.legs.append(Leg( 5, [13,15,17], [False,True,False]))
            self.legs.append(Leg( 6, [7,9,11], [True,True,False]))

        if not self.isReal:  #Animation
            self.fig = plt.figure()
            self.ax1 = p3.Axes3D(self.fig)
            self.init_plotting()
            # Translation matrix for displacement of foot points in animation
            self.translationMatrix = np.array([
                np.array([
                    [1, 0, 0, 3],  # Leg front right
                    [0, 1, 0, -1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, 3],  # Leg front left
                    [0, 1, 0, 1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, 0],  # Leg middle left
                    [0, 1, 0, 2],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, -3],  # Leg back left
                    [0, 1, 0, 1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, -3],  # Leg back right
                    [0, 1, 0, -1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, 0],  # Leg middle right
                    [0, 1, 0, -2],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])])

    def iterate(self):
        #os.system("cls")  # Supposed to clear console
        percentValue = 0
        indexLegs1 = 0 # Index in trajectory of three legs that start swinging (-1 cuz it starts to count up in loop)
        indexLegs2 = int(len(self.trajectory) / 2)  # Index in trajectory of three legs that start stemming  (-1
        # cuz it starts to count up in loop)
        # Temporary variables for checking of read in values
        angle = self.walkingAngle
        height = self.stepHeight
        while 1:
            start_time = time.perf_counter()

            #############
            #     E     #
            #############
            if percentValue != 0:
                indexLegs1 += 1
                indexLegs2 += 1
            # Indices iterate spaced by half trajectory length through trajectory.
            if indexLegs1 == len(self.trajectory):
                indexLegs1 = 0
            if indexLegs2 == len(self.trajectory):
                indexLegs2 = 0
            # For animation. Changes only apply when three legs are at their highest position
            
            if not self.isReal:
                if (indexLegs1 == 0 or indexLegs2 == 0):
                    # Angle & Step height
                    try:
                        input_data = open('Steuer.txt', 'r').read()
                        lines = input_data.split('\n')
                        angle = lines[0]
                        height = lines[1]
                    except IOError:
                        print('File error!')
                    # Angle
                    if is_number(angle):
                        self.walkingAngle = np.radians(float(angle))
                    # Step height
                    if is_number(height):
                        if float(height) <= 1:
                            self.stepHeight = float(height)
                            self.trajectory = self.createTrajectory()  # Recalculate trajectory
            else:
                # Read COM Data
                comData = self.com.readData()
                percentValue = comData["Geschwindigkeit"]
                print(percentValue)
                # {'Winkelrichtung': 0, 'Geschwindigkeit': 0, 'Angehoben': 0, 'InitPosition': 0}
                if (indexLegs1 == 0 or indexLegs2 == 0):
                    if is_number(comData["Winkelrichtung"]):
                        self.walkingAngle = comData["Winkelrichtung"]
                        print("Winkel", self.walkingAngle)
                    if is_number(comData["Angehoben"]):
                        if float(comData["Angehoben"]) <= 1:
                            self.stepHeight = float(comData["Angehoben"])
                            if float(comData["Angehoben"]) <= self.MINSTEPHEIGHT:
                                self.stepHeight = self.MINSTEPHEIGHT
                            self.trajectory = self.createTrajectory()  # Recalculate trajectory
                            print("StepHeight", self.stepHeight)
                if is_number(comData["Geschwindigkeit"]):
                    self.cycleTime = self.CYCLETIMEMIN + (1-percentValue) * (self.CYCLETIMEMAX - self.CYCLETIMEMIN)
                    print("Geschw.", self.cycleTime)


            #############
            #     V     #
            #############
            # Copy of current positions to not change them
            curPos1 = copy.deepcopy(self.trajectory[indexLegs1])
            curPos2 = copy.deepcopy(self.trajectory[indexLegs2])
            rotationMatrix = self.rotationMatrixZ(self.walkingAngle)
            # Append current coordinates for each leg
            if self.isReal:
                if percentValue != 0:
                    for i in range(0, 6):
                        m1 = 0.05*np.dot(rotationMatrix, curPos1)
                        m2 = 0.05*np.dot(rotationMatrix, curPos2)

                        if i in self.legsGroup1:
                            m1[0] += self.Homepositions[i][0]
                            m1[1] += self.Homepositions[i][1]
                            m1[2] += self.Homepositions[i][2]
                            self.legs[i].setFootCoordinate(m1)

                        elif i in self.legsGroup2:
                            m2[0] += self.Homepositions[i][0]
                            m2[1] += self.Homepositions[i][1]
                            m2[2] += self.Homepositions[i][2]
                            self.legs[i].setFootCoordinate(m2)

                    Servo.jointdrive.JointDrive.doActionAllServo()

            else:
                self.legs = []  # Clear legs for new positions
                for i in range(0, 6):
                    if i in self.legsGroup1:
                        self.legs.append(np.dot(np.dot(self.translationMatrix[i], rotationMatrix), curPos1))
                    elif i in self.legsGroup2:
                        self.legs.append(np.dot(np.dot(self.translationMatrix[i], rotationMatrix), curPos2))

            #############
            #     A     #
            #############
            try:
                if self.isReal:
                    end_time = time.perf_counter()
                    print("\nTime: %f" % (end_time - start_time))
                    time.sleep(self.cycleTime - (end_time - start_time))
                else:
                    self.animate()
                    end_time = time.perf_counter()
                    print("\nTime: %f" % (end_time - start_time))
            except:
                pass

    def createTrajectory(self):
        """
        Returns a List with variable length depending on predefined stepSize
        Starting with the topmost point of the swing phase for easy determination of the point for direction switching
        """
        trajectory = []
        for i in np.arange(0, 1, self.stepSize):
            trajectory.append([round(i, self.accuracy), 0, round(self.swingFunctionCalculation(i), self.accuracy), 1])
        for i in np.arange(1, -1, -self.stepSize):
            trajectory.append([round(i, self.accuracy), 0, 0, 1])
        for i in np.arange(-1, 0, self.stepSize):
            trajectory.append([round(i, self.accuracy), 0, round(self.swingFunctionCalculation(i), self.accuracy), 1])
        return trajectory

    def swingFunctionCalculation(self, x):
        """
        Returns a value depending on x. The function defines the movement of the legs during swing phase
        """
        if self.walkingMode == WalkingMode.COSINE:
            return np.abs(self.stepHeight * math.cos((math.pi / 2) * x))
        elif self.walkingMode == WalkingMode.TRAPEZOID:
            if -1 <= x < -0.5:
                return self.stepHeight * (2 * x + 2)
            elif -0.5 <= x < 0.5:
                return self.stepHeight
            elif 0.5 <= x <= 1:
                return self.stepHeight * (-2 * x + 2)

    def rotationMatrixZ(self, angle):
        """
        Return a matrix for the rotation of movement around the Z-axis
        """
        rotationMatrix = np.array([
            [round(np.cos(angle), self.accuracy), round(-np.sin(angle), self.accuracy), 0, 0],
            [round(np.sin(angle), self.accuracy), round(np.cos(angle), self.accuracy), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        return rotationMatrix

    # PLOTTING

    def animate(self):
        """
        Reads the coordinates in self.legs, prints them and clears them afterwards
        """
        dots = []
        for lg in self.legs:
            if lg[2] > 0:  # Z-coordinate > 0 (swing phase)
                c = 'red'
            else:
                c = 'black'
            dots.append(self.ax1.scatter(lg[0], lg[1], lg[2], c=c))
        plt.pause(0.0000001)
        for d in dots:
            d.remove()

    def init_plotting(self):
        """
        Initializes the coordinate system for the animation
        """
        # Plotting
        # Axes labels
        self.ax1.set_xlabel('X', fontsize=14, fontweight='bold', color='b')
        self.ax1.set_ylabel('Y', fontsize=14, fontweight='bold', color='r')
        self.ax1.set_zlabel('Z', fontsize=14, fontweight='bold', color='g')
        self.ax1.set_title("Bewegungssimulation")
        # Presentation area of axes
        self.ax1.set_xlim(-4.25, 4.25)
        self.ax1.set_ylim(-4.25, 4.25)
        self.ax1.set_zlim(0, 4.25)
        circles = []
        circles.append(plt.Circle((3, -1), 1, fill=False))
        circles.append(plt.Circle((3, 1), 1, fill=False))
        circles.append(plt.Circle((0, 2), 1, fill=False))
        circles.append(plt.Circle((0, -2), 1, fill=False))
        circles.append(plt.Circle((-3, -1), 1, fill=False))
        circles.append(plt.Circle((-3, 1), 1, fill=False))
        for c in circles:
            self.ax1.add_patch(c)
            art3d.pathpatch_2d_to_3d(c)
        plt.ion()  # Turn the interactive mode on.


# Outside of Robot

def is_number(s):
    """
    Checks value s if it is a number
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


############################
#           TEST           #
############################
def testFunction():
    myRobot = Robot(True)
    time.sleep(1)
    myRobot.iterate()

if __name__ == "__main__":
    testFunction()
