import time
import serialPorts
import serial

# create serial port connection
l = serialPorts.serialPortList()
print("serialPorts", l)
port = serial.Serial(port=str(l[0]), baudrate=1000000)

# auxiliary methods
def calcCheckSum(pkt):
    s = sum(pkt[2:-1])                              # add all values from servo-id to last parameter
    return (~s) & 0xFF                              # invert sum bit-wise and limit to byte range

def sendCommand(command):
    command[-1] = calcCheckSum(command)             # calculate check sum and store it into last command entry
    port.write(bytearray(command))                  # send command to serial line
    print("send:", command)


# main programm
servoId = 8                                         # Id of Servo
servoId2 = 13

# ID 8
command = [255, 255, servoId, 5, 4, 30, 0, 0, 0]    # command list

# Set to position x ID 8
position = 1023                                    # define position
command[6] = position & 255                         # set data low byte in command list
command[7] = position >> 8                          # set data high byte in command list
sendCommand(command)                                # send command

# ID 13
command = [255, 255, servoId2, 5, 4, 30, 0, 0, 0]    # command list

# Set to position x ID 13
position = 1023                                         # define position
command[6] = position & 255                         # set data low byte in command list
command[7] = position >> 8                          # set data high byte in command list
sendCommand(command)

command = [255, 255, 254, 2, 5, 250]
sendCommand(command)

# ------------------------
# Set the position back to 0

# ID 8
commandBack = [255, 255, servoId, 5, 4, 30, 0, 0, 0]

# Set to position 0
position = 0
commandBack[6] = position & 255                         # set data low byte in command list
commandBack[7] = position >> 8                          # set data high byte in command list
sendCommand(commandBack)

time.sleep(2)

# ID 13
commandBack = [255, 255, servoId2, 5, 4, 30, 0, 0, 0]

# Set to position 0
position = 0
commandBack[6] = position & 255                         # set data low byte in command list
commandBack[7] = position >> 8                          # set data high byte in command list
sendCommand(commandBack)

# Execute reg written actions
commandBack = [255, 255, 254, 2, 5, 250]
sendCommand(commandBack)

command = [255, 255, 1, 4, 2, 30, 0, 0, 204]
sendCommand(command)