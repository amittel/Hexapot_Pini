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

    def invKinAlphaJoint(self, pos):
        alpha = math.atan2(pos[1] , pos[0]) # y x

        footPos = np.array(pos)
        A1 = np.array([
            [math.cos(alpha), 0, math.sin(alpha), self.lc * math.cos(alpha)],
            [math.sin(alpha), 0, -math.cos(alpha), self.lc * math.sin(alpha)],
            [0, 1, 0, 0],
            [0, 0, 0, 1]])
        betaPos = np.dot(A1, np.transpose(pos))
        lct = np.linalg.norm(footPos[0:3] - betaPos[0:3])
        lctSquare = math.pow(lct, 2)
        print("acos: " ,(self.ltSquare + self.lfSquare - lctSquare) / (2 * self.lt * self.lf))
        gamma = math.acos((self.ltSquare + self.lfSquare - lctSquare) / (2 * self.lt * self.lf)) - math.pi
        h1 = math.acos((self.lfSquare + lctSquare - self.ltSquare) / (2 * self.lf * lct))
        h2 = math.acos((lctSquare + self.lcSquare - math.pow(np.linalg.norm(footPos[0:3]), 2))/(2 * self.lc * lct))
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


def startFunction():
    myLeg = Leg([0.043,0.04,0.053,0.062,0.02,0.005,0.096])
    #myLeg = Leg([1,1,1,1,1,1,1])
    #x = 0.10
    #y= 0
    #z= 0.1
    wa = wb = wg = math.pi / 2;
    print("Koord (G): ", math.degrees(wa), ",", math.degrees(wb), ",", math.degrees(wg))
    pos = myLeg.forKinAlphaJoint(wa, wb, wg)
    wa, wb, wg = myLeg.invKinAlphaJoint([pos[0], pos[1], pos[2], 1])

    #print("Koord (G): ", x, ",", y, ",", z)

    print("Koord (W): " ,math.degrees(wa) ,",",math.degrees(wb),",", math.degrees(wg)) #math.radians()
    print("Koord (B): ",pos[0] ,",",pos[1],",", pos[2])




if __name__ == "__main__":
    startFunction()