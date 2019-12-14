import math
import numpy as np
import animation
from vpython import color

class Leg:
    def __init__(self, a):
        self.a = [a[0], a[1], a[2], a[3], a[4], a[5], a[6]]
        self.lc = self.a[2]
        self.lcSquare = math.pow(self.lc,2)
        self.lf = math.sqrt(math.pow(self.a[3], 2) + math.pow(self.a[4],2))
        self.lfSquare = math.pow(self.lf,2)
        self.lt = math.sqrt(math.pow(self.a[5], 2) + math.pow(self.a[6],2))
        self.ltSquare = math.pow(self.lt, 2)

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
            #print("lctSquare ", lctSquare)
            #print("Zähler ",round((self.ltSquare + self.lfSquare - lctSquare)))
            #print("Nenner ",round(2 * self.lt * self.lf, 15))
            gamma = math.acos(round((self.ltSquare + self.lfSquare - lctSquare) / (2 * self.lt * self.lf), 15)) - math.pi
            
            h1 = math.acos(round((self.lfSquare + lctSquare - self.ltSquare) / (2 * self.lf * lct), 15))
            h2 = math.acos((lctSquare + self.lcSquare - math.pow(np.linalg.norm(footPos[0:3]), 2))/(2 * self.lc * lct))
            #print("h1: ", h1)
            #print("h2: ", h2)
            #print("pi: ", math.pi)
            #print("pi-h2:" , math.pi-h2)
            if footPos[2] < 0:
                beta = (h1 + h2) - math.pi
            else:
                beta = (math.pi - h2) + h1
            #print("beta", (h1 + h2) - math.pi, (math.pi - h2) + h1)
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

    def testStraightLeg(self):
        '''Testing for a straight leg. All joints have zero degree'''
        wa = wb = wg = 0
        length = self.lc + self.lf + self.lt

        print("\nTest gerades Bein")
        print("Winkel (gegeben): a,b,g ", math.degrees(wa), ",", math.degrees(wb), ",", math.degrees(wg))
        pos = self.forKinAlphaJoint(wa, wb, wg)
        print("Koord (fKin): x,y,z     ",pos[0] ,",",pos[1],",", pos[2])
        print("Länge (gerechnet):      ",length)

    def testTibia(self,w):
        '''Testing for a angled leg. All joints have x degree'''
        wa = w[0]
        wb = w[1]
        wg = w[2]

        if wg == math.pi/2:
            length = self.lc + self.lf + math.sin(0)*self.lt
        else:
            length = self.lc + self.lf + math.sin(wg)*self.lt

        print("\nTest für Tibia")
        print("Zwischenergebnis lc:",self.lc)
        print("Zwischenergebnis lf:",self.lf)
        print("Zwischenergebnis lt:",self.lt)
        print("Zwischenergebnis:",math.sin(wg)*self.lt)
     
        
        print("Winkel (gegeben): a,b,g ", math.degrees(wa), ",", math.degrees(wb), ",", math.degrees(wg))
        pos = self.forKinAlphaJoint(wa, wb, wg)
        print("Koord (fKin): x,y,z     ",pos[0] ,",",pos[1],",", pos[2])
        print("Länge (gerechnet):      ",length)





def drawRobot():
    #ToDo: Two leg groups: L1,2,4,5 with a0=0.043m and L3,6 with a0= 0.030
    #ToDo: Do other values change too?

    legDimsA = [0.043,0.04,0.053,0.062,0.02,0.005,0.096]
    legDimsB = [0.030,0.04,0.053,0.062,0.02,0.005,0.096]

    #ToDo: Insert Offsets from origin
    
    hexaLegA = Leg(legDimsA)
    hexaLegB = Leg(legDimsB) #not used

    colors = [color.red, color.green, color.blue]

    pos = [(0.18,0.10,-0.05), (0,0.10,-0.05)]
    animation.createScene()

    for i in range(len(pos)):
        print("-------------------------------Bein " + str(i) + "----------------------------------")
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