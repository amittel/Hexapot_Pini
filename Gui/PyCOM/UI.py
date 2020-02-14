from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        # Create IP Input Textfield
        self.ipText = QtWidgets.QLineEdit(self.centralwidget)
        self.ipText.setGeometry(QtCore.QRect(20, 28, 191, 30))
        self.ipText.setObjectName("ipText")
        
        # Create Connection Button
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(220, 28, 100, 30))
        self.connectButton.setObjectName("connectButton")


        # Create Status Label
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(20, 80, 50, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        
        # Create Connection Label
        self.connectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.connectionLabel.setGeometry(QtCore.QRect(220, 80, 211, 30))
        self.connectionLabel.setAutoFillBackground(True)
        self.connectionLabel.setTextFormat(QtCore.Qt.AutoText)
        #self.connectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connectionLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.connectionLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.connectionLabel.setObjectName("connectionLabel")


        # Set the widget to be the main window's central widget
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Hexapod-Walking-Challenge", "Hexapod-Walking-Challenge"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.ipText.setText(_translate("MainWindow", "IP Adresse eingeben"))
        self.connectionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aa0000;\">disconnected</span></p></body></html>"))
        self.StatusLabel.setText(_translate("MainWindow", "Status"))
        


