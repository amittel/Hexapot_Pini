# Used for animation only
#import animation
#import servoDummy as sD
#from vpython import color
import time

import math
import numpy as np
import time

# Getting the imports right.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import Servo.jointdrive as servo
import Servo.servo_ax12a

class Leg:
    def __init__(self, legID, legServos, rotation):
        self.legID = legID
        self.servoID = legServos
        self.rotation = rotation

        self.initAngle = 0.0
        self.oldAngles = (0,0,0)

        # Offset from base to leg [m]
        self.leg_X = (0.033, 0.033, 0, -0.033,-0.033,0)
        self.leg_Y = (-0.033, 0.033, 0.044, 0.033, -0.033, -0.044)

        # Length of legs
        if self.legID == 3 or self.legID == 6:
            print("Länge Bein 3 or 6")
            self.dims = [0.030,0.04,0.053,0.062,0.02,0.005,0.096]
        else:
            print("Länge Bein 1, 2, 4 or 5")
            self.dims = [0.043,0.04,0.053,0.062,0.02,0.005,0.096]
        
        self.lc = self.dims[2]
        self.lcSquare = math.pow(self.lc,2)
        self.lf = math.sqrt(math.pow(self.dims[3], 2) + math.pow(self.dims[4],2))
        self.lfSquare = math.pow(self.lf,2)
        self.lt = math.sqrt(math.pow(self.dims[5], 2) + math.pow(self.dims[6],2))
        self.ltSquare = math.pow(self.lt, 2)



        #Setting rotation of servos for joints (cw, ccw)
        self.rotAlpha = rotation[0]
        self.rotBeta = rotation[1]
        self.rotGamma = rotation[2]

        

        self.servoAlpha = servo.JointDrive(self.servoID[0])
        self.servoBeta = servo.JointDrive(self.servoID[1])
        self.servoGamma = servo.JointDrive(self.servoID[2])

        Servo.servo_ax12a.setReturnDelay(2, True)

        print("--- Leg ", self.legID )
        #Move leg into init Position
        print("Moving A")
        #print("Current angle: ", self.servoAlpha.getCurrentJointAngle())
        self.servoAlpha.setDesiredAngleAndMotorLoad(self.initAngle, 100.0, False)
        #self.servoAlpha.setDesiredAngleAndMotorLoad(self.initAngle, 50.0, True)
        #time.sleep(2)
        print("Moving B")
        #print("Current angle: ", self.servoBeta.getCurrentJointAngle())
        #self.servoBeta.setMovingSpeed(50,True)
        #self.servoBeta.setDesiredJointAngle(self.initAngle)
        self.servoBeta.setDesiredAngleAndMotorLoad(self.initAngle, 100.0, False)
        #time.sleep(2)
        print("Moving G")
        #self.servoGamma.setMovingSpeed(50,True)
        #self.servoGamma.setDesiredJointAngle(self.initAngle)
        self.servoGamma.setDesiredAngleAndMotorLoad(self.initAngle, 100.0, False)
        #time.sleep(2)

        
        #Robots has to do it.
        print("Sending Cmds...")
        servo.JointDrive.doActionAllServo()
        time.sleep(1)

        if legID == 4:
            time.sleep(2)
        print("--- End Init ---")
        # Used to define which leg and if it's coordinates need to be rotated
        #self.bodyLoc = bodyLoc_

        # Servo init position
        #self.startPos = startPos_

        # Vector of 3 ints, servos from body to tibia
        #self.cox = sD.servo(servoIds_[0])
        #self.fem = sD.servo(servoIds_[1])
        #self.tib = sD.servo(servoIds_[2])

        # Set servo speeds


        # moves to init position
        #self.moveTo(startPos_)


    def getLegLength(self):
        return (self.lc, self.lf, self.lt)

    def invKinAlphaJoint(self, pos):
        try:
            alpha = math.atan2(pos[1] , pos[0]) # y x

            footPos = np.array(pos)

            A1 = np.array([
                [math.cos(alpha), 0, math.sin(alpha), self.lc * math.cos(alpha)],
                [math.sin(alpha), 0, -math.cos(alpha), self.lc * math.sin(alpha)],
                [0, 1, 0, 0],
                [0, 0, 0, 1]])

            betaPos = np.dot(A1, np.transpose([0,0,0,1]))

            lct = np.linalg.norm(footPos[0:3] - betaPos[0:3])
            lctSquare = math.pow(lct, 2)

            gamma = math.acos(round((self.ltSquare + self.lfSquare - lctSquare) / (2 * self.lt * self.lf), 15)) - math.pi

            h1 = math.acos(round((self.lfSquare + lctSquare - self.ltSquare) / (2 * self.lf * lct), 15))
            h2 = math.acos((lctSquare + self.lcSquare - math.pow(np.linalg.norm(footPos[0:3]), 2))/(2 * self.lc * lct))

            if footPos[2] < 0:
                beta = (h1 + h2) - math.pi
            else:
                beta = (math.pi - h2) + h1

            return (alpha, beta, gamma)

        except Exception as e:
            print("FEHLER: Punkt nicht im Arbeitsbereich. Description: " + str(e))
            return (0, 0, 0)

    def forKinAlphaJoint(self, alpha, beta, gamma):
        try:
            return [math.cos(alpha) * (self.lt * math.cos(beta + gamma) + self.lf * math.cos(beta) + self.lc),
                   math.sin(alpha) * (self.lt * math.cos(beta + gamma) + self.lf * math.cos(beta) + self.lc),
                   self.lt * math.sin(beta + gamma) + self.lf * math.sin(beta),
                    1]
        except Exception as e:
            print("Error forward kinematics: " + str(e))

    def moveTo(self, angles, speeds):

        #Copying angles for next step to calc velocity
        self.oldAngles = angles

        alphaAngle = angles[0]
        betaAngle = angles[1]
        gammaAngle = angles[2]

        alphaSpeed = speeds[0]
        betaSpeed = speeds[1]
        gammaSpeed = speeds[2]

        self.servoAlpha.setDesiredAngleAndMotorLoad(alphaAngle, alphaSpeed, True)
        self.servoBeta.setDesiredAngleAndMotorLoad(betaAngle, betaSpeed, True)
        self.servoGamma.setDesiredAngleAndMotorLoad(gammaAngle, gammaSpeed, True)



    def calcJointAngles(self, pos):
        ''' Leg hat u.a. eine Abfragemethode (calcJointAngles), der x,y und z-Koordinaten
            (kartesische Koordinaten) des Fußpunkts des Beins geschickt werden.
            Die Methode liefert die entsprechenden 3 Gelenkwinkel (a,b,g) zurück.
        '''
        alpha, beta, gamma = self.invKinAlphaJoint(pos)

        return (alpha, beta, gamma)

        # Send angles to servos
        #servo.JointDrive.setDesiredJointAngle()
        #self.servoAlpha.setDesiredJointAngle(alpha)
        #self.servoBeta.setDesiredJointAngle(beta)
        #self.servoGamma.setDesiredJointAngle(gamma)


    def calcFootCoordinate(self, alpha, beta, gamma):
        ''' Leg hat u.a. eine Abfragemethode (calcFootCoordinate), der 3 Gelenkwinkel
            (Winkelkoordinaten) geschickt werden. Die Methode liefert die kartesischen
            Koordinaten des Fußpunkts im Basiskoordinatensystem (x 0 ,y 0 ,z 0 ) des Beins zurück
            (siehe nächste Folien).
        '''
        pass

    def setFootCoordinate(self, pos):
        ''' Leg hat u.a. eine Setzmethode (setFootCoordinate), der die im nächsten Zeitschritt
            anzufahrende Fußposition (x,y,z) übergeben wird. Diese wird mit Hilfe der anderen
            Methoden der Klassen in entsprechende Gelenkwinkel umgewandelt und an die drei
            Instanzen der Gelenkantriebe (Klasse JointDrive, Gruppe Antriebskommunikation)
            übergeben.
        '''

        # Setting offset for leg from origin B
        if self.legID == 3 or self.legID == 6:
            pos[1] = pos[1] + self.leg_Y[self.legID-1] + self.dims[0] # Y
            pos[2] = pos[2] - self.dims[1] # Z
        else:
            pos[0] = pos[0] + self.leg_X[self.legID-1] + self.dims[0] # X
            pos[2] = pos[2] - self.dims[1] # Z

        # Rotating local coordinates, so X is equal to our origin B
        self.rotateLegKoord(pos)

        # calc angles from pos
        curAngles= self.calcJointAngles(pos)

        speeds = self.setVelocity(self.oldAngles, curAngles)

        self.moveTo(curAngles, speeds)


    #def printId(self):
    #    print("Coxa/Femur/Tibia: "+ str(self.cox.gievId()) + "/" +str(self.fem.gievId())+ "/" + str(self.tib.gievId()))


    def setVelocity(self, oldAngle, newAngle, velocity = 100):
        
        # Calc'ing the diff between new and old angle
        a = abs(newAngle[0] - oldAngle[0])
        b = abs(newAngle[1] - oldAngle[1])
        c = abs(newAngle[2] - oldAngle[2])
        
        # Checking for the largest angle and then setting speed relations accordingly
        if a >= b and a >= c and a!=0:
            servoSpeedAlpha = velocity
            servoSpeedBeta = math.ceil((b / a) * velocity)
            servoSpeedGamma = math.ceil((c / a) * velocity)
        elif b >= a and b >= c and b!=0:
            servoSpeedBeta = velocity
            servoSpeedAlpha = math.ceil((a / b) * velocity)
            servoSpeedGamma = math.ceil((c / b) * velocity)
        elif c >= a and c >= b and c!=0:
            servoSpeedGamma = velocity
            servoSpeedAlpha = math.ceil((a / c) * velocity)
            servoSpeedBeta = math.ceil((b / c) * velocity)
        else:
            servoSpeedAlpha = velocity
            servoSpeedBeta = velocity
            servoSpeedGamma = velocity

        return (servoSpeedAlpha, servoSpeedBeta, servoSpeedGamma)

    def rotateLegKoord(self, pos):
        
        if self.legID == 1:
            pass
        elif self.legID == 2:
            pass
        elif self.legID == 3: # Rotate -90 deg (cw)
            cos = 0
            sin = -1
        elif self.legID == 4 or self.legID == 5: # Rotate -180 deg (cw)
            cos = -1
            sin = 0
        elif self.legID == 6: # Rotate 90 deg (ccw)
            cos = 0
            sin = 1
        
        pos[0] = cos * pos[0] - sin * pos[1] # rotated X
        pos[1] = sin * pos[0] + cos * pos[1] # rotated Y 

        return pos





'''
Just used for animation with vpython
------------------------------------
def drawRobot():
    #ToDo: Two leg groups: L1,2,4,5 with a0=0.043m and L3,6 with a0= 0.030
    #ToDo: Do other values change too?

    legDimsA = [0.043,0.04,0.053,0.062,0.02,0.005,0.096]
    legDimsB = [0.030,0.04,0.053,0.062,0.02,0.005,0.096]

    #ToDo: Insert Offsets from origin
    
    hexaLegA = Leg(1, 1, [0, 1, 2])
    hexaLegB = Leg(1, 1, [0, 1, 2]) #not used

    colors = [color.red, color.green, color.blue]

    pos = [(0.18,0.10,-0.05), (0,0.10,-0.05)]
    animation.createScene()

    for i in range(len(pos)):
        print("-------------------------------Position " + str(i) + "----------------------------------")
        print(hexaLegA.printId())
        print("Koord gegeben: ",[pos[i][0], pos[i][1], pos[i][2]])
        try:
            alpha, beta, gamma = hexaLegA.invKinAlphaJoint([pos[i][0], pos[i][1], pos[i][2], 1])
            print("Winkel  (deg): ", math.degrees(alpha), ",", math.degrees(beta), ",", math.degrees(gamma))
            print("Winkel  (rad): ", alpha, ",", beta, ",", gamma)
            pos2= hexaLegA.forKinAlphaJoint(alpha,beta,gamma)
            print("Koord auf fKin: ",[pos2[0], pos2[1], pos2[2]])


            angles = (alpha,beta,gamma)
            offsetL1x = 0.043*100
            offsetL1z = -0.040*100

            animation.drawLeg(angles, hexaLegA.getLegLength(), offsetL1x, offsetL1z, colors[i%3])

        except Exception as e:
            print(e)
'''

'''
if __name__ == "__main__":
    #drawRobot()
    tableLeg = Leg(1, [1, 3, 5], [True, True, True])
'''