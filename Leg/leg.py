import math
import numpy as np


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
        print("h1: ", h1)
        print("h2: ", h2)
        print("pi: ", math.pi)
        print("pi-h2:" , math.pi-h2)
        if footPos[2] < 0:
            beta = (h1 + h2) - math.pi
        else:
            beta = (math.pi - h2) + h1

        return (alpha, beta, gamma)

    def forKinAlphaJoint(self, alpha, beta, gamma):
        pos = [0, 0, 0, 1]

        pos[0] = math.cos(alpha) * (self.lt * math.cos(beta + gamma) + self.lf * math.cos(beta) + self.lc)
        pos[1] = math.sin(alpha) * (self.lt * math.cos(beta + gamma) + self.lf * math.cos(beta) + self.lc)
        pos[2] = self.lt * math.sin(beta + gamma) + self.lf * math.sin(beta)

        return pos

    def calcJointAngles(self):
        ''' Leg hat u.a. eine Abfragemethode (calcJointAngles), der x,y und z-Koordinaten
            (kartesische Koordinaten) des Fußpunkts des Beins geschickt werden.
            Die Methode liefert die entsprechenden 3 Gelenkwinkel (a,b,g) zurück.
        '''
        pass

    def calcFootCoordinate(self):
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


def startFunction():
    a = [0.043,0.04,0.053,0.062,0.02,0.005,0.096]
    
    myLeg = Leg(a)

    #myLeg.testStraightLeg()
    
    #myLeg.testStraightLeg()
    #w = (0,0,math.pi/4)
    #myLeg.testTibia(w)
    wa=0
    wb=0
    wg=math.pi/2
    #pos=[0.214,0,0] #gestrecktes bein

    Llength = myLeg.getLegLength()
    #pos=[round(Llength[0]+Llength[1],4),round(-Llength[2],4),0]
    #pos=[0.05,0.05,0.05]

    pos = myLeg.forKinAlphaJoint(wa, wb, wg)

    print("Koord auf fKin:",[pos[0], pos[1], pos[2]])
    wa, wb, wg = myLeg.invKinAlphaJoint([pos[0], pos[1], pos[2], 1])
    
    print("Winkel  (deg): ", math.degrees(wa), ",", math.degrees(wb), ",", math.degrees(wg))
    print("Winkel  (rad): ", wa, ",", wb, ",", wg)

    
    print("Koord auf fKin:",[round(pos[0],4), round(pos[1],4), round(pos[2],4)])
    
    
    

    #print("Winkel aus iKin: " ,math.degrees(wa) ,",",math.degrees(wb),",", math.degrees(wg)) #math.radians()

    


    



if __name__ == "__main__":
    startFunction()