import math
from Servo.servo_ax12a import *

import time


# Class definition of ax12a-controller class, defines interface to the robot
# ===============================================================================
# Implements the interface between leg- and servo class
# ------------------------------------------------------------------------------
# Provides all required methods that allow the leg class to control the servo
# Implements all necessary co-domain conversion between leg- and servo values
# Limits values too valid servo values
# Servo uses ticks from 0 to 1023 for angle and speed
# Leg uses angles in radian and rotation per minute for speed
# Defines zero angle as average of min- and max value -> positive and negative angles are allowed
class JointDrive(ServoAx12a):
    # Definition of public class attributes
    # ----------------------------------------------------------------------
    _ANGLE_RADIAN_ZERO = (ServoAx12a._ANGLE_MAX_DEGREE - ServoAx12a._ANGLE_MIN_DEGREE) * math.pi / 360  # Zero angle offset of servo in radian
    _ANGLE_UNIT = ServoAx12a._ANGLE_MAX_TICKS / ((ServoAx12a._ANGLE_MAX_DEGREE - ServoAx12a._ANGLE_MIN_DEGREE) * math.pi * 2 / 360)  # Ticks per rad

    _CONST_ANGLE_TO_TICKS = 1023 / (5 * math.pi / 3)
    _CONST_SPEED_TO_TICKS = 1023 / 114

    # Private methods
    # ----------------------------------------------------------------------
    # Constructor, defines the following variables: counterClockWise, angleOffset, angleMax, angleMin
    # id -> id of servo, cw -> rotating direction, aOffset -> angle offset,
    # aMax -> maximum angle allowed, aMin -> minimum angle allowed
    def __init__(self, servoId, ccw = False, aOffset = 0.0, aMax = math.pi * 2, aMin = -math.pi * 2):
        self.id = servoId
        self.counterClockWise = ccw
        self.angleMax = aMax if (aMax > aMin or aMax < self._ANGLE_RADIAN_ZERO) else self._ANGLE_RADIAN_ZERO
        self.angleMin = aMin if (aMin > aMax or aMin < (-1)*self._ANGLE_RADIAN_ZERO) else self._ANGLE_RADIAN_ZERO
        self.aOffset = aOffset
        self.curAngle = 0
        super().__init__(servoId)

    # Converts angle in radian to servo ticks
    # angle -> in radian, returns angle in servo ticks
    def __convertAngleToTicks(self, angle):
        angle += self.aOffset
        if self.counterClockWise:
            angle += self._ANGLE_RADIAN_ZERO
        else:
            angle = self._ANGLE_RADIAN_ZERO - angle
        return self._CONST_ANGLE_TO_TICKS * angle

    # Converts servo ticks to angle in radian
    # ticks -> servo ticks, returns angle in radian
    def __convertTicksToAngle(self, ticks):
        return ticks / self._CONST_ANGLE_TO_TICKS

    # Converts speed in rpm to servo ticks
    # speed -> value in rpm
    def __convertSpeedToTicks(self, speed):
        return self._CONST_SPEED_TO_TICKS * speed

    # Converts ticks to speed in rpm
    # ticks -> servo ticks
    def __convertTicksToSpeed(self, ticks):
        return ticks / self._CONST_SPEED_TO_TICKS

    # Public methods
    # ----------------------------------------------------------------------
    # Get current angle of servo
    # returns angle in radian
    def getCurrentJointAngle(self):
        self.curAngle = self.__convertTicksToAngle(self.getPresentPosition())
        return self.curAngle

    # Set servo to desired angle
    # angle -> in radian,
    def setDesiredJointAngle(self, angle: float, trigger: bool = False):
        success = self.setGoalPosition(self.__convertAngleToTicks(angle), trigger)
        if success:
            self.curAngle -= angle

        return success

    # Set servo to desired angle speed
    # angle -> in radian,
    # speed -> speed of movement in rpm, speed = 0 -> maximum speed
    def setDesiredAngleSpeed(self, angle: float, speed: int = 0, trigger: bool = False):
        speed_in_ticks = self.__convertSpeedToTicks(speed)
        angle_in_ticks = self.__convertAngleToTicks(angle)

        success = self.setGoalPosSpeed(angle_in_ticks, speed_in_ticks, trigger)
        if success :
            self.curAngle -= angle

        return success

    # Set speed value of servo
    # speed -> angle speed in rpm
    def setSpeedValue(self, speed, trigger=False):
        speed_in_ticks = self.__convertSpeedToTicks(speed)
        success = self.setMovingSpeed(speed_in_ticks, trigger)

        return success
