from Servo.dynamixel import Dynamixel

# Definition of Servo-Ax12a-controller class, defines control and status methods
# ===============================================================================
# Implements communication commands to servo AX12A
# ------------------------------------------------------------------------------
# Uses the commands of Dynamixel class to send and receive the reqiered servo values

class ServoAx12a(Dynamixel):
    # Definition of private class attributes
    # ----------------------------------------------------------------------
    # EEPROM communication registers addresses
    __RETURN_DELAY_TIME = 0x05  # time of return delay (n * 2 in [uS]), 1 byte, read/write
    __RETURN_LEVEL      = 0x10  # status return level, 1 byte, read/write
    # RAM communication registers addresses
    __GOAL_POSITION     = 0x1E  # goal position, 2 byte, read/write
    __MOVING_SPEED      = 0x20  # moving speed, 2 byte, read/write
    __PRESENT_POSITION  = 0x24  # current position, 2 byte, read only
    __PRESENT_SPEED     = 0x26  # current speed, 2 byte, read only

    # Definition of protected class attributes
    # ----------------------------------------------------------------------
    # Servo constants
    _ANGLE_MAX_TICKS    = 1023          # ticks at highest position (330 degree)
    _ANGLE_MIN_TICKS    = 0             # ticks at lowest position (30 degree)
    _ANGLE_MAX_DEGREE   = 300           # highest angle reachable is 330 degree
    _ANGLE_MIN_DEGREE   = 0             # lowest angle reachable is 30 degree
    _SPEED_UNIT         = 0.111         # 0.111 rpm per tick
    _SPEED_MAX_TICKS    = 1023          # 1023
    _SPEED_MAX_RPM      = 1023 * 0.111  # 1023 * 0.111 = 113.5 rpm

    # Definition of public class attributes
    # ----------------------------------------------------------------------
    # Definition of valid return levels
    RETURN_LEVEL_PING_COMMAND   = 0  # Status packet is only returned for ping
    RETURN_LEVEL_READ_COMMANDS  = 1  # Status packet is returned for ping and read requests
    RETURN_LEVEL_ALL_COMMANDS   = 2  # Status packet is returned for ping, read requests and writes
    # Defines the wait time the servo switches from receive to send mode
    # when a read request packet was received
    RETURN_DELAY_VALUE          = 10  # Definition of return delay time, value * 2 -> [uS]

    # Definition of private methods
    # ----------------------------------------------------------------------
    # Constructor, return level and return delay are set
    def __init__(self, servoId):
        super().__init__(servoId)
        self.setReturnLevel(self.RETURN_LEVEL_ALL_COMMANDS)
        self.setReturnDelay(self.RETURN_DELAY_VALUE)

    # Getter methods for servo Ax12a
    # ----------------------------------------------------------------------
    # Get time of return delay
    # returns: 0 to 254 (0xFE) can be used, and the delay time per data value is 2 usec.
    def getReturnDelay(self)-> int:
        nByte = self._requestNByte(self.__RETURN_DELAY_TIME)
        return self.__convertByteToInt(nByte)

    # Get status return level
    # returns:  0->No return against all commands (Except PING Command),
    #           1->Return only for the READ command,
    #           2->Return for all commands
    def getReturnLevel(self)-> int:
        nByte = self._requestNByte(self.__RETURN_LEVEL)
        return self.__convertByteToInt(nByte)

    # Get goal position
    # returns: value of 0 to 1023, the unit is 0.29 degree.
    def getGoalPosition(self)-> int:
        nByte = self._requestNWord(self.__GOAL_POSITION)
        return self.__convertByteToInt(nByte)

    # Get moving speed
    # returns: 0 to 1023, the unit is about 0.111rpm.
    #          If it is set to 0, it means the maximum rpm of the motor is used without controlling the speed.
    #          If it is 1023, it is about 114rpm.
    def getMovingSpeed(self):
        nByte = self._requestNWord(self.__MOVING_SPEED)
        return self.__convertByteToInt(nByte)

    # Get present position
    # returns: value of 0 to 1023, the unit is 0.29 degree.
    def getPresentPosition(self)-> int:
        nByte = self._requestNWord(self.__PRESENT_POSITION)
        return self.__convertByteToInt(nByte)

    # Get present speed
    # returns: 0 to 1023, the unit is about 0.111rpm.
    #          If it is set to 0, it means the maximum rpm of the motor is used without controlling the speed.
    #          If it is 1023, it is about 114rpm.
    def getPresentSpeed(self)-> int:
        nByte = self._requestNWord(self.__PRESENT_SPEED)
        return self.__convertByteToInt(nByte)

    # Get goal position and speed, returns: [position, speed]
    # position: 0 ~ 1023,
    # speed:    0 to 1023, the unit is about 0.111rpm.
    #           If it is 0, it means the maximum rpm of the motor is used without controlling the speed.
    #           If it is 1023, it is about 114rpm.
    def getGoalPosSpeed(self)-> [int, int]:
        nByte_pos = self._requestNWord(self.__GOAL_POSITION)
        nByte_spd = self._requestNWord(self.__MOVING_SPEED)
        return [self.__convertByteToInt(nByte_pos), self.__convertByteToInt(nByte_spd)]

    # Get present position and speed, returns: [position, speed]
    # position: 0 ~ 1023,
    # speed:    0 to 1023, the unit is about 0.111rpm.
    #           If it 0, it means the maximum rpm of the motor is used without controlling the speed.
    #           If it is 1023, it is about 114rpm.
    def getPresPosSpeed(self)-> [int, int]:
        nByte_pos = self._requestNWord(self.__PRESENT_POSITION)
        nByte_spd = self._requestNWord(self.__PRESENT_SPEED)
        return [self.__convertByteToInt(nByte_pos), self.__convertByteToInt(nByte_spd)]

    # Setter methods for servo Ax12a
    # ----------------------------------------------------------------------

    # Set time of return delay
    # delay: 0 to 254 (0xFE) can be used, and the delay time per data value is 2 usec.
    def setReturnDelay(self, delay: int, trigger: bool = False)-> bool:
        self._writeNBytePkt(self.__RETURN_DELAY_TIME, [delay], trigger)
        return True if self.getLastError() == self.ERR_DEFAULT else False

    # Set status return level
    # 0->No return against all commands (Except PING Command),
    # 1->Return only for the READ command, 2->Return for all commands
    def setReturnLevel(self, level: int, trigger: bool = False)-> bool:
        self._writeNBytePkt(self.__RETURN_LEVEL, [level], trigger)
        return True if self.getLastError() == self.ERR_DEFAULT else False

    # Set goal position
    # position: 0 to 1023 is available. The unit is 0.29 degree.
    def setGoalPosition(self, position: int, trigger: bool = False)-> bool:
        self._writeNWordPkt(self.__GOAL_POSITION, [position], trigger)
        return True if self.getLastError() == self.ERR_DEFAULT else False

    # Set moving speed
    # speed: 0~1023 can be used, and the unit is about 0.111rpm.
    #        If it is set to 0, it means the maximum rpm of the motor is used without controlling the speed.
    #        If it is 1023, it is about 114rpm.
    def setMovingSpeed(self, speed: int, trigger: bool =False)-> bool:
        self._writeNWordPkt(self.__MOVING_SPEED, [speed], trigger)
        return True if self.getLastError() == self.ERR_DEFAULT else False

    # Set goal position and speed
    # position: 0 to 1023 is available. The unit is 0.29 degree.
    # speed:    0~1023 can be used, and the unit is about 0.111rpm.
    #           If it is set to 0, it means the maximum rpm of the motor is used without controlling the speed.
    #           If it is 1023, it is about 114rpm.
    def setGoalPosSpeed(self, position: int, speed: int, trigger: bool = False)-> bool:
        self._writeNWordPkt(self.__GOAL_POSITION, [position], trigger)
        self._writeNWordPkt(self.__MOVING_SPEED, [speed], trigger)
        return True if self.getLastError() == self.ERR_DEFAULT else False

    # ---------------------------------------------------------------------------
    # Definition of private methods with implicit servo-id
    # Accessible only within own class
    # ---------------------------------------------------------------------------

    # Convert byte array to integer
    # nByte:    -> number of bytes to convert
    # return    integer
    @staticmethod
    def __convertByteToInt(nByte: list) -> int:
        if nByte is not None and isinstance(nByte, list):
            nByte.reverse()
            n = len(nByte)
            res = 0
            for byte in nByte:
                res += byte << (8 * (n - 1))
                n -= 1

            return res
        else:
            return -1
