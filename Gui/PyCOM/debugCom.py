from Com import Com
from threading import Thread
import msgpack
import time


class testCom:

    def __init__(self, port="5555"):
        # vm ip:            172.16.137.137
        # server ip:        172.16.137.1
        # localhost ip:     127.0.0.1
        self.server = Com(port=port, server=True)
        self.data = {'Winkelrichtung': 0, 'Geschwindigkeit': 0, 'Angehoben': 0, 'InitPosition': 0}
        
        #self.server.bind("tcp://*:"+port)
        
        self.direction = 0
        self.velocity = 0
        self.leghight = 0
        self.initPos = 0

        #self.data_thread = Thread(target=self.readData, args=())
        #self.data_thread.start()

 # "listen" / receive data
    def readData(self):
        while True:
            self.data = self.server.getData()

            # TODO: change reduntant variable creation, use (direction; velocity; leghight; initPos) directly
            #if self.data != None:
            self.direction = self.data['Winkelrichtung']
            self.velocity = self.data['Geschwindigkeit']
            self.leghight = self.data['Angehoben']
            self.initPos = self.data['InitPosition']
            #print("Init:", self.initPos)
            
            # TODO: Change print to return for the walking group
            #print("Winkel:", self.direction ,"," , "Geschwindigkeit: ", self.velocity, ",", "Angehoben: ", self.leghight, ",", "Init-Position: ", self.initPos)
            # TESTEN!!!
            print("Winkel:", self.direction ,"," , "Geschwindigkeit: ", self.velocity, ",", "Angehoben: ", self.leghight, ",", "Init-Position: ", self.initPos)
            
            # TODO: Tweek this, for performance
            #  Do some 'work'
            time.sleep(0.1)

if __name__ == "__main__":
    test = testCom(port="5555")
    test.readData()
    



