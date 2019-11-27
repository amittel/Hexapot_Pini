import serial
from Servo import serialPorts

# Classdefinition to implement dynamixel protocol
# ===============================================================================
# Implements the dynamixel protocol 1.0
# ------------------------------------------------------------------------------
# Assigns the class object to a dedicated servo by the servo id
# Initializes the serial connection to the servo bus
# Handles the transfer of all required packet types with 1..n data bytes or -words
class Dynamixel:
    # Definition of protected class attributes
    # Accessible only within own and derived classes
    # ---------------------------------------------------------------------------
    _ID_BROADCAST = 0xFE

    # Definition of private class attributes, accessible only within own class
    # ---------------------------------------------------------------------------
    # Define dynamixel constants
    __DYNAMIXEL_PORT_NR         = 0         # Index of dynamixel line in list
    __BAUDRATE                  = 1000000   # Baud rate of dynamixel serial line
    __TIME_OUT_DEFAULT          = 2         # Default time out
    __DIRECT_ACTION             = 3         # Direct action command
    __TRIGGER_ACTION            = 4         # Triggered action command
    __STATUS_PACKET_BASE_LENGTH = 6         # Base length of status packet
    __lines                     = serialPorts.serialPortList()  # Contains all available serial lines
    __serial_port               = serial.Serial(__lines[__DYNAMIXEL_PORT_NR],
                                                __BAUDRATE, timeout=__TIME_OUT_DEFAULT)  # Serial line object
    # Create templates of command packets
    __pktAction     = [255, 255, 0, 2, 5, 0]            # Packet to invoke action
    __pktReadData   = [255, 255, 0, 4, 2, 0, 0, 0]      # Packet to request date
    __pktWriteByte  = [255, 255, 0, 4, 3, 0, 0, 0]      # Packet to write byte
    __pktWriteNByte = [255, 255, 0, 0, 3, 0]            # Base-packet to write n-bytes
    __pktWriteWord  = [255, 255, 0, 5, 3, 0, 0, 0, 0]   # Packet to write word

    # byte position for package
    PKT_ID          = 2 # byte position for package id
    PKT_LEN         = 3 # byte position for package length
    PKT_INS         = 4 # byte position for package instruction
    PKT_ERR         = 4 # byte position for package error
    PKT_PARAM_FIRST = 5 # byte position for package param first
    PKT_REG         = 5 # byte position for package register
    PKT_DATA_LEN    = 6 # byte position for package read data's length
    PKT_CSUM        =-1 # byte position for package check sum

    # byte value for instruction
    INS_PING        = 1
    INS_READ_DATA   = 2
    INS_WRITE_DATA  = 3
    INS_REG_WRITE   = 4
    INS_ACTION      = 5
    INS_RESET       = 6
    INS_SYNC_WRITE  = 83

    # bit value for error
    ERR_INPUT_VOLTAGE   = 2 ** 0
    ERR_ANGLE_LIMIT     = 2 ** 1
    ERR_OVERHEATING     = 2 ** 2
    ERR_RANGE           = 2 ** 3
    ERR_CHECKSUM        = 2 ** 4
    ERR_OVERLOAD        = 2 ** 5
    ERR_INSTRUCTION     = 2 ** 6
    ERR_DEFAULT         = 0

    portList = serialPorts.serialPortList()
    port = serial.Serial(port=str(portList[0]), baudrate=1000000)

    # ---------------------------------------------------------------------------
    # Definition of private methods with implicit servo-id
    # Accessible only within own class
    # ---------------------------------------------------------------------------
    # Constructor, sets id and defines error variable
    # id -> id of attached servo
    """
        Constructor sets ID and error
    """
    def __init__(self, servoId):
        self.id = servoId
        self.error = self.ERR_DEFAULT

    """
        Trigger the action if the data was written via REG_WRITE
    """
    # Start predefined action on servo
    # id -> id of servo, without id -> broadcast action
    def __doAction(self, servoId = _ID_BROADCAST):
        command                 = [255, 255, 0, 0, 0, 0]
        command[self.PKT_ID]    = servoId
        command[self.PKT_LEN]   = 2
        command[self.PKT_INS]   = self.INS_ACTION
        command[self.PKT_CSUM]  = self.__checkSum(command)

        self.__sendCommand(command)

    def __doPing(self, servoId):
        command                 = [255, 255, 0, 0, 0, 0]
        command[self.PKT_ID]    = servoId
        command[self.PKT_LEN]   = 2
        command[self.PKT_INS]   = self.INS_PING
        command[self.PKT_CSUM]  = self.__checkSum(command)

        self.__sendCommand(command)

    """
        Read data from the control table of an actuator
    """
    # Prepares and sends packet to servo in order to read data from servo memory
    # register -> register address of servo
    # nByte    -> number of bytes to read
    def __writeReadDataPkt(self, register, nByte):
        command                     = [255, 255, 0, 0, 0, 0, 0, 0]
        command[self.PKT_ID]        = self.id
        command[self.PKT_LEN]       = 4
        command[self.PKT_INS]       = self.INS_READ_DATA
        command[self.PKT_REG]       = register
        command[self.PKT_DATA_LEN]  = nByte
        command[self.PKT_CSUM]      = self.__checkSum(command)

        self.__sendCommand(command)

    """
        Same as __doReadStatusPkt ??
    """
    # Read status packet, set error value and get return values from servo
    # nByte    -> number of bytes to read
    def __readStatusPkt(self, nByte):
        parameter, self.error = self.__doReadStatusPkt(nByte)
        return parameter

    """
        Read the status packet and return parameter values
    """
    # Read status packet, set error value and get return values from servo
    # nByte -> number of bytes to read
    def __doReadStatusPkt(self, nByte):
        statusPkt = list(self.__serial_port.read(self.__STATUS_PACKET_BASE_LENGTH + nByte))

        if statusPkt[self.PKT_CSUM] == self.__checkSum(statusPkt):
            if statusPkt[self.PKT_LEN] == (self.__STATUS_PACKET_BASE_LENGTH + nByte):
                return statusPkt[self.PKT_PARAM_FIRST : self.PKT_CSUM], self.ERR_DEFAULT
            else:
                return None, statusPkt[self.PKT_ERR]
        else:
            return None, self.ERR_CHECKSUM

    """
        Checks the sum of the parameters to check for Errors
    """
    # Calculates check sum of packet list
    def __checkSum(self, pkt):
        s = sum(pkt[2:-1])
        return (~s) & 0xFF

    # Send command to servo
    def __sendCommand(self, command):
        self.__serial_port.write(command)
        print("send:", command)

    # Definition of protected methods
    # Accessible within own and derived classes
    # ---------------------------------------------------------------------------
    """
        Requests NBytes (8 bits) from parameters n+1 to m
    """
    # Read data byte from servo memory
    # register -> register address of servo
    # nByte    -> number of data bytes to read
    """
    Requests NBytes from parameters n+1 to m
    """
    def _requestNByte(self, register, nByte = 1):
        self.__writeReadDataPkt(register, nByte)
        return self.__readStatusPkt(nByte)

    """
        Requests NWords (16 bits) from parameters n+1 to m
    """
    # Read data word from servo memory
    # register -> register address of servo
    # nWord   -> number of data words to read
    def _requestNWord(self, register, nWord=1):
        self.__writeReadDataPkt(register, nWord * 2)
        return self.__doReadStatusPkt(nWord * 2)

    """
    WRITE_DATA Write data bytes (8 bits) into the control table of the Dynamixel actuator
    """
    # Sends packet to servo in order to write n data bytes into servo memory
    # register -> register address of servo
    # data     -> list of bytes to write
    # trigger  -> False -> command is directly executed, True -> command is delayed until action command
    def _writeNBytePkt(self, register, byteData, trigger):
        command                 = [255, 255, 0, 0, 0, 0]
        command[self.PKT_ID]    = self.id
        command[self.PKT_LEN]   = len(byteData) + 3
        command[self.PKT_INS]   = self.INS_REG_WRITE if trigger else self.INS_WRITE_DATA
        command[self.PKT_REG]   = register
        command.extend(byteData.append(0))
        command[self.PKT_CSUM]  = self.__checkSum(command)

        self.__sendCommand(command)
        # Dynamixel.__serial_port.write(pktWriteNByte)

    """
    WRITE_DATA Write data words (16 bits) into the control table of the Dynamixel actuator
    """
    # Sends packet to servo in order to write data dword into servo memory
    # register -> register address of servo
    # data     -> list of words to write
    # trigger  -> False -> command is directly executed, True -> command is delayed until action command
    def _writeNWordPkt(self, register, wordData, trigger):
        byteData = []
        for word in wordData:
            byteData.append(word & 0xFF)        # append fst. byte
            byteData.append(word >> 8 & 0xFF)   # append snd. byte

        self._writeNBytePkt(register, byteData, trigger)

    # Definition of public methods with implicit servo-id
    # Accessible from everywhere
    # ---------------------------------------------------------------------------
    # Show available serial lines
    def showSerialLines(self):
        print(Dynamixel.__lines)

    # Start predefined action on servo with assigned id
    def action(self):
        return self.__doAction(self.id)

    # Ping servo
    def ping(self):
        return self.__doPing(self.id)

    # Get last error
    def getLastError(self):
        return self.error