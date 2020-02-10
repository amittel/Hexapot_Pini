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
        self.data = self.server.getData()
        return self.data

if __name__ == "__main__":
    test = testCom(port="5555")
    test.readData()
    



