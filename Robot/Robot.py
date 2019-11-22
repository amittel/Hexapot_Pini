import time
import copy
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import mpl_toolkits.mplot3d.art3d as art3d


class Robot:

    def __init__(self, isReal):
        self.isReal = isReal  # Flag if the robot is simulated (animation) or real (no animation)
        self.stepSize = 0.1  # Spacing of trajectory points
        self.stepHeight = 0.5  # Working area from 0 to 1
        self.accuracy = 4  # Amount of decimals
        self.trajectory = self.createTrajectory()
        self.cycleTime = 0.1  # Time for each step size
        self.walkingAngle = 0  # Current movement angle
        self.legs = []
        self.legsGroup1 = [0, 2, 4]  # Group 1 starts swinging
        self.legsGroup2 = [1, 3, 5]  # Group 2 starts stemming

        if not self.isReal:  # Only for animation
            self.fig = plt.figure()
            self.ax1 = p3.Axes3D(self.fig)
            self.init_plotting()
            # Translation matrix for displacement of foot points in animation
            self.translationMatrix = np.array([
                np.array([
                    [1, 0, 0, 3],
                    [0, 1, 0, -1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, 3],
                    [0, 1, 0, 1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, 0],
                    [0, 1, 0, 2],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, -3],
                    [0, 1, 0, 1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, -3],
                    [0, 1, 0, -1],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]),
                np.array([
                    [1, 0, 0, 0],
                    [0, 1, 0, -2],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])])

    def iterate(self):
        os.system("cls")  # Supposed to clear console
        indexLegs1 = -1  # Index in trajectory of three legs that start swinging (-1 cuz it starts to count up in loop)
        indexLegs2 = int(len(
            self.trajectory) / 2 - 1)  # Index in trajectory of three legs that start stemming  (-1 cuz it starts to count up in loop)
        # Temporary variables for checking of read in values
        angle = self.walkingAngle
        height = self.stepHeight
        while 1:
            start_time = time.perf_counter()

            #############
            #     E     #
            #############
            indexLegs1 += 1
            indexLegs2 += 1
            # Indices iterate spaced by half trajectory length through trajectory.
            if indexLegs1 == len(self.trajectory):
                indexLegs1 = 0
            if indexLegs2 == len(self.trajectory):
                indexLegs2 = 0
            # For animation. Changes only apply when three legs are at their highest position
            # TODO: COM OBJEKT AUSLESEN
            if (indexLegs1 == 0 or indexLegs2 == 0) and not self.isReal:
                # Angle & Step height
                try:
                    input_data = open('Steuer.txt', 'r').read()
                    lines = input_data.split('\n')
                    angle = lines[0]
                    height = lines[1]
                except:
                    print('File error!')
                # Angle
                if is_number(angle):
                    self.walkingAngle = np.radians(float(angle))
                # Step height
                if is_number(height):
                    if float(height) <= 1:
                        self.stepHeight = float(height)
                        self.trajectory = self.createTrajectory()

            #############
            #     V     #
            #############
            # Copy of current positions to not change them
            curPos1 = copy.deepcopy(self.trajectory[indexLegs1])
            curPos2 = copy.deepcopy(self.trajectory[indexLegs2])
            rotationMatrix = self.rotationMatrixZ(self.walkingAngle)
            self.legs = []  # Clear legs for new positions
            # Append current coordinates for each leg
            if self.isReal:
                for i in range(0, 6):
                    if i in self.legsGroup1:
                        self.legs.append(np.dot(rotationMatrix, curPos1))
                    elif i in self.legsGroup2:
                        self.legs.append(np.dot(rotationMatrix, curPos2))
            else:
                for i in range(0, 6):
                    if i in self.legsGroup1:
                        self.legs.append(np.dot(np.dot(self.translationMatrix[i], rotationMatrix), curPos1))
                    elif i in self.legsGroup2:
                        self.legs.append(np.dot(np.dot(self.translationMatrix[i], rotationMatrix), curPos2))

            #############
            #     A     #
            #############

            if self.isReal:
                end_time = time.perf_counter()
                print("\nTime: %f" % (end_time - start_time))
                time.sleep(self.cycleTime - (end_time - start_time))
            else:
                self.animate()
                end_time = time.perf_counter()
                print("\nTime: %f" % (end_time - start_time))

    def createTrajectory(self):
        """
        Returns a List with variable length depending on predefined stepSize
        Starting with the topmost point of the swing phase for easy determination of the point for direction switching
        """
        trajectory = []
        for i in np.arange(0, 1, (self.stepSize)):
            trajectory.append([round(i, self.accuracy), 0, round(self.swingFunctionCalculation(i), self.accuracy), 1])
        for i in np.arange(1, -1, -(self.stepSize)):
            trajectory.append([round(i, self.accuracy), 0, 0, 1])
        for i in np.arange(-1, 0, (self.stepSize)):
            trajectory.append([round(i, self.accuracy), 0, round(self.swingFunctionCalculation(i), self.accuracy), 1])
        return trajectory

    def swingFunctionCalculation(self, x):
        """
        Returns a value depending on x. The function defines the movement of the legs during swing phase
        """
        return np.abs(self.stepHeight * math.cos((math.pi / 2) * x))

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
        for l in self.legs:
            if l[2] > 0:  # Z-coordinate > 0 (swing phase)
                c = 'red'
            else:
                c = 'black'
            dots.append(self.ax1.scatter(l[0], l[1], l[2], c=c))
        plt.pause(0.0000001)
        for d in dots:
            d.remove()

    def init_plotting(self):
        """
        Initializes the coordinate system for the animation
        """
        # Plotting
        self.ax1.set_xlabel('X', fontsize=14, fontweight='bold', color='b')
        self.ax1.set_ylabel('Y', fontsize=14, fontweight='bold', color='r')
        self.ax1.set_zlabel('Z', fontsize=14, fontweight='bold', color='g')
        self.ax1.set_title("Bewegungssimulation")
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
    myRobot = Robot(False)
    myRobot.iterate()


if __name__ == "__main__":
    testFunction()
