import time
import copy
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import mpl_toolkits.mplot3d.art3d as art3d


class Robot:

    def __init__(self, isReal):
        self.isReal = isReal
        self.stepSize = 0.1  # Distance of trajectory points
        self.stepHeight = 0.5  # Bereich von 0 bis 1
        self.accuracy = 4  # Amount of decimals
        self.swing = self.createSwingTrajectory()
        self.stem = self.createStemTrajectory()
        self.cycleTime = 0.1
        self.walkingAngle = 0
        self.legs = []
        self.swingLegs = [0, 2, 4]  # Werte sind indizes von legs
        self.stemLegs = [1, 3, 5]

        if not self.isReal:
            self.fig = plt.figure()
            self.ax1 = p3.Axes3D(self.fig)
            self.init_plotting()
            # Matrizen in array für Animation der Beinpunkte
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
        os.system("cls")
        # Aktuelle Position in Trajektorie init
        n = -1
        cycle = 0
        angle = self.walkingAngle
        height = self.stepHeight
        while 1:
            start_time = time.perf_counter()

            #############
            #     E     #
            #############
            # Index der aktuellen Trajektionsposition
            n += 1
            if n == len(self.swing):
                n = 0
                cycle += 1
                if cycle == 2:
                    cycle = 0
            if cycle == 0:
                if n == 0:
                    self.swingLegs = [0, 2, 4]
                    self.stemLegs = [1, 3, 5]
                elif n == len(self.swing) / 2:
                    self.swingLegs = [1, 3, 5]
                    self.stemLegs = [0, 2, 4]
            else:
                if n == 0:
                    self.swingLegs = [1, 3, 5]
                    self.stemLegs = [0, 2, 4]
                elif n == len(self.swing) / 2:
                    self.swingLegs = [0, 2, 4]
                    self.stemLegs = [1, 3, 5]
            if n == 0 and not self.isReal:  # Nur für animation und bei Position 0 auslesen
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
                        self.swing = self.createSwingTrajectory()

            #############
            #     V     #
            #############
            # Kopie der aktuellen Position um trajectory nicht zu verändern
            curPosSwing = copy.deepcopy(self.swing[n])
            curPosStem = copy.deepcopy(self.stem[n])
            # Rotationsmatrix für Verarbeitung vom Winkel
            rotationMatrix = self.rotationMatrixZ(self.walkingAngle)
            self.legs = []
            # Koordinaten für jedes Bein anhängen
            if self.isReal:
                for i in range(0, 6):
                    if i in self.stemLegs:
                        self.legs.append(np.dot(rotationMatrix, curPosStem))
                    elif i in self.swingLegs:
                        self.legs.append(np.dot(rotationMatrix, curPosSwing))
            else:
                for i in range(0, 6):
                    if i in self.stemLegs:
                        self.legs.append(np.dot(np.dot(self.translationMatrix[i], rotationMatrix), curPosStem))
                    elif i in self.swingLegs:
                        self.legs.append(np.dot(np.dot(self.translationMatrix[i], rotationMatrix), curPosSwing))

            #############
            #     A     #
            #############

            if self.isReal:
                end_time = time.perf_counter()
                print("\nTime: %f" % (end_time - start_time))
                time.sleep(self.cycleTime - (end_time - start_time))
            else:
                # animation.FuncAnimation(self.fig, self.refreshData(), interval=10)
                self.animate()
                end_time = time.perf_counter()
                print("\nTime: %f" % (end_time - start_time))

    def createSwingTrajectory(self):
        """
        Hier wird die Trajektorie der Schwingbewegung generiert
        :return: Liste mit Koordinaten 
        """
        swingList = []
        for i in np.arange(0, 1, (self.stepSize)):
            swingList.append([round(i, self.accuracy), 0, round(self.swingFunctionCalculation(i), self.accuracy), 1])
        for i in np.arange(-1, 0, (self.stepSize)):
            swingList.append([round(i, self.accuracy), 0, round(self.swingFunctionCalculation(i), self.accuracy), 1])
        return swingList

    def createStemTrajectory(self):
        """
        Hier wird die Trajektorie der Stemmbewegung generiert
        :return:
        """
        stemList = []
        for i in np.arange(0, -1, -(self.stepSize)):
            stemList.append([round(i, self.accuracy), 0, 0, 1])
        for i in np.arange(1, 0, -(self.stepSize)):
            stemList.append([round(i, self.accuracy), 0, 0, 1])
        return stemList

    def swingFunctionCalculation(self, x):
        # Kosinus für variable Höhe
        return np.abs(self.stepHeight * math.cos((math.pi / 2) * x))

    def rotationMatrixZ(self, angle):
        rotationMatrix = np.array([
            [round(np.cos(angle), self.accuracy), round(-np.sin(angle), self.accuracy), 0, 0],
            [round(np.sin(angle), self.accuracy), round(np.cos(angle), self.accuracy), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        return rotationMatrix

    # PLOTTING

    def animate(self):
        dots = []
        for i, l in enumerate(self.legs):
            if i in self.swingLegs:
                c = 'red'
            else:
                c = 'black'
            dots.append(self.ax1.scatter(l[0], l[1], l[2], c=c))
        plt.pause(0.0000000000000000000000000000001)
        for d in dots:
            d.remove()

    def init_plotting(self):
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
        plt.ion()  # Turn the interactive mode on


# Outside of Robot

def is_number(s):
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
