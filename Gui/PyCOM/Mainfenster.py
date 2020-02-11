from UI import Ui_MainWindow
from Com import Com
from Controller import Controller
from threading import Thread
from time import time

from PyQt5 import QtCore, QtGui ,QtWidgets, uic
import sys
import msgpack
import math
import time

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):

        # Controller Thread Variable (z.B. um den Thread zu beenden)
        self.con_Thread_var = True

        # Client
        self.client = None

        # Connected Thread Variable
        self.connected = False

        # initialise controller
        self.controller1 = Controller()

        # Data to be packed and processed
        self.direction = 0
        self.leghight = 0
        self.velocity = 0
        self.initPos = 0

        # Create window
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button
        self.ui.connectButton.clicked.connect(self.connect)

        # Threads
        self.con_thread = Thread(target=self.conReact, args=())
        self.con_thread.start()
        self.data_thread = Thread(target=self.dataReact, args=())
        self.data_thread.start()
        self.send_thread = Thread(target=self.sendReact, args=())

    # Set direction to 0
    def setDirection0(self):
        self.direction = 0

    # Set initial position
    def setInitPos(self):
        if(self.initPos == 0):
            self.initPos = 1

    # Set initial position
    def setInitPosR(self):
        if (self.initPos == 1):
            self.initPos = 0

    # Elevate hexapod
    def setAnheben(self):
        self.leghight = 1

    # Delevate hexapod
    def setAbsenken(self):
        self.leghight = 0

    # Set velocity
    def setSpeed(self):

        if(self.controller1.getVelocity()<0.01):
            self.velocity = 0
        else:
            self.velocity = self.controller1.getVelocity() * 100

    # Connect to server
    def connect(self):
        # ip = textinput in QtDesigner implementieren
        #self.client = Com(ip="192.168.137.61", server=False)
        #self.send_thread.start()
        self.ui.connectionLabel.setText("<font color='green'>Connected</font>")

        self.client = Com(ip=self.ui.ipText.text(), server=False)
        self.send_thread.start()

    # Set direction
    def setDirection(self):

        """if(-self.controller1.getAngleDirection() > -(1/2 * math.pi) and -self.controller1.getAngleDirection() < 0):
            self.direction = math.degrees(-self.controller1.getAngleDirection() + 2 * math.pi)
        else:
            self.direction = math.degrees(-self.controller1.getAngleDirection())
            """
        self.direction = math.degrees(-self.controller1.getAngleDirection())

    # Controller Thread
    def conReact(self):

        while True:
            if (self.controller1.getVelocity() != 0 and self.con_Thread_var):
                self.setSpeed()
            if(self.controller1.getAngleDirection() != 0 and self.con_Thread_var):
                self.setDirection()
            if (self.controller1.getButtonLeghight() == 1 and self.con_Thread_var):
                 self.setAnheben()
            if (self.controller1.getButtonLeghight() == 0 and self.con_Thread_var):
                 self.setAbsenken()
            if(self.controller1.getButtonInit() == 1 and self.con_Thread_var):
                self.setInitPos()
            if (self.controller1.getButtonInit() == 0 and self.con_Thread_var):
                self.setInitPosR()

    # Data Thread
    def dataReact(self):

        while True:
            # Pack data
            self.data = {'Winkelrichtung': self.direction, 'Geschwindigkeit': self.velocity, 'Angehoben': self.leghight, 'InitPosition': self.initPos}
            # print(self.data)

    # Send data Thread
    def sendReact(self):

        while True:
            self.client.send(self.data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()

    w.show()
    sys.exit(app.exec_())



