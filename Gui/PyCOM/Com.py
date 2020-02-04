import zmq
import msgpack
from threading import Thread
import time


class Com:
   # vm ip:            172.16.137.133
   # server ip:        172.16.137.1
   # localhost ip:     127.0.0.1
   # ip Marko NB       192.168.137.1
   # ip TMR - Marko NB 192.168.137.61
   
    def __init__(self, ip="172.16.137.133", port="5556", server=True):

        self.data = {"Winkelrichtung": 0, "Geschwindigkeit": 1, "Angehoben": 0, 'InitPosition': 0}
        context = zmq.Context()
        self.socket = context.socket(zmq.PAIR)

        # Create a Server or Client
        if server == True:
            self.socket.bind("tcp://*:"+port)
        else:
            self.socket.connect("tcp://"+ip+":"+port)

        listen_thread = Thread(target=self.listen, args=(self.socket,))
        listen_thread.start()

    # Send data
    def send(self, data):
        self.socket.send(msgpack.packb(data))
        
        # TODO: Tweek this, for performance
        #  Do some 'work'
        time.sleep(0.1)

    # "listen" / receive data
    def listen(self, socket):
        while True:
            try:
                self.data = msgpack.unpackb(socket.recv(), encoding="utf-8")
                #print(self.data)

            except:
                print("Listen Error")


    # access data
    def getData(self):
            return self.data


if __name__ == "__main__":
    ser = Com()
