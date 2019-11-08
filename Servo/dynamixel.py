import serial
from Servo import serialPorts
import copy


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
    __DYNAMIXEL_PORT_NR = 0  # Index of dynamixel line in list
    __BAUDRATE = 1000000  # Baudrate of dynamixel serial line
    __TIME_OUT_DEFAULT = 2  # Default time out
    __DIRECT_ACTION = 3  # Direct action command
    __TRIGGERT_ACTION = 4  # Triggered action command
    __STATUS_PACKET_BASE_LENGTH = 6  # Base length of status packet
    __lines = serialPorts.serialPortList()  # Contains all available serial lines
    __serial_port = serial.Serial(__lines[__DYNAMIXEL_PORT_NR], \
                                  __BAUDRATE, timeout=__TIME_OUT_DEFAULT)  # Serial line object
    # Create templates of command packets
    __pktAction = [255, 255, 0, 2, 5, 0]  # Packet to invoke action
    __pktReadData = [255, 255, 0, 4, 2, 0, 0, 0]  # Packet to request date
    __pktWriteByte = [255, 255, 0, 4, 3, 0, 0, 0]  # Packet to write byte
    __pktWriteNByte = [255, 255, 0, 0, 3, 0]  # Base-packet to write n-bytes
    __pktWriteWord = [255, 255, 0, 5, 3, 0, 0, 0, 0]  # Packet to write word

    # ---------------------------------------------------------------------------
    # Definition of private methods with implicit servo-id
    # Accessible only within own class
    # ---------------------------------------------------------------------------
    # Constructor, sets id and defines error variable
    # id -> id of attached servo
    def __init__(self, id):
        self.id = id
    # Start predefined action on servo
    # id -> id of servo to ping, without id -> broadcast action
    def __doAction(self, id=_ID_BROADCAST):
        command = [255, 255, id, 2, 5, 250]
    # Prepares and sends packet to servo in order to read data from servo memory
    # register -> register address of servo
    # nByte    -> number of bytes to read
    def __writeReadDataPkt(self, register, nByte):

    # Read status packet, set error value and get return values from servo
    # nByte    -> number of bytes to read
    def __readStatusPkt(self, nByte):

    # Calculates check sum of packet list
    def __checkSum(self, pkt):

    # Read status packet, set error value and get return values from servo
    # nByte -> number of bytes to read
    def __doReadStatusPkt(self, nByte):

    # Definition of protected methods
    # Accessible within own and derived classes
    # ---------------------------------------------------------------------------
    # Read data byte from servo memory
    # register -> register address of servo
    # dtLen    -> number of data bytes to read
    def _requestNByte(self, register, dtLen=1):

    # Read data word from servo memory
    # register -> register address of servo
    # dtWLen   -> number of data words to read
    def _requestNWord(self, register, dtWlen=1):

    # Sends packet to servo in order to write n data bytes into servo memory
    # register -> register address of servo
    # data     -> list of bytes to write
    # trigger  -> False -> command is directly executed, True -> command is delayed until action command
    def _writeNBytePkt(self, register, data, trigger):

    # Sends packet to servo in order to write data dword into servo memory
    # register -> register address of servo
    # data     -> list of words to write
    # trigger  -> False -> command is directly executed, True -> command is delayed until action command
    def _writeNWordPkt(self, register, data, trigger):

    # Definition of public methods with implicit servo-id
    # Accessible from everywere
    # ---------------------------------------------------------------------------
    # Show available serial lines
    def showSerialLines(self):
        print(Dynamixel.__lines)

    # Start predefined action on servo with assigned id
    def action(self):
        return self.__doAction(self.id)

    # Get last error
    def getLastError(self):
        return self.error

