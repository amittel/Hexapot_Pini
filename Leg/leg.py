import math
import numpy as np
#import animation
#import servoDummy as sD
#from vpython import color

from Servo import jointdrive

class Leg:
    #def __init__(self, startPos_, bodyLoc_ , servoIds_):
    def __init__(self, legID, legServos):
        self.legID = legID
        self.servoID = legServos

        #Init Pos is zero deg for all servos!

        if self.legID == 3 or self.legID == 6:
            print("Bein 3 or 6")
            self.dims = [0.030,0.04,0.053,0.062,0.02,0.005,0.096]
        else:
            print("Bein 1, 2, 4 or 5")
            self.dims = [0.043,0.04,0.053,0.062,0.02,0.005,0.096]
        
        self.lc = self.dims[2]
        self.lcSquare = math.pow(self.lc,2)
        self.lf = math.sqrt(math.pow(self.dims[3], 2) + math.pow(self.dims[4],2))
        self.lfSquare = math.pow(self.lf,2)
        self.lt = math.sqrt(math.pow(self.dims[5], 2) + math.pow(self.dims[6],2))
        self.ltSquare = math.pow(self.lt, 2)

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

    def moveTo(self, pos_):
        pass

    def calcJointAngles(self):
        ''' Leg hat u.a. eine Abfragemethode (calcJointAngles), der x,y und z-Koordinaten
            (kartesische Koordinaten) des Fußpunkts des Beins geschickt werden.
            Die Methode liefert die entsprechenden 3 Gelenkwinkel (a,b,g) zurück.
        '''
        pass

    def calcFootCoordinate(self, alpha, beta, gamma):
        ''' Leg hat u.a. eine Abfragemethode (calcFootCoordinate), der 3 Gelenkwinkel
            (Winkelkoordinaten) geschickt werden. Die Methode liefert die kartesischen
            Koordinaten des Fußpunkts im Basiskoordinatensystem (x 0 ,y 0 ,z 0 ) des Beins zurück
            (siehe nächste Folien).
        '''
        pass

    def setFootCoordinate(self):
        ''' Leg hat u.a. eine Setzmethode (setFootCoordinate), der die im nächsten Zeitschritt
            anzufahrende Fußposition (x,y,z) übergeben wird. Diese wird mit Hilfe der anderen
            Methoden der Klassen in entsprechende Gelenkwinkel umgewandelt und an die drei
            Instanzen der Gelenkantriebe (Klasse JointDrive, Gruppe Antriebskommunikation)
            übergeben.
        '''

        pass
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
        #dims are our offsets?! 
        # Are they already in?!

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



if __name__ == "__main__":
    drawRobot()
'''