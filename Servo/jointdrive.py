from Servo.dynamixel import Dynamixel
from Servo.servo_ax12a import ServoAx12a
import math


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
    _ANGLE_RADIAN_ZERO = (ServoAx12a._ANGLE_MAX_DEGREE
                          - ServoAx12a._ANGLE_MIN_DEGREE) * math.pi / 360   # Zero angle offset of servo in radian
    _ANGLE_RADIAN_MAX  = ServoAx12a._ANGLE_MAX_DEGREE * math.pi / 360       # Max angle offset of servo in radian
    _ANGLE_RADIAN_MIN  = ServoAx12a._ANGLE_MIN_DEGREE * math.pi / 360       # Min angle offset of servo in radian
    _ANGLE_UNIT = ServoAx12a._ANGLE_MAX_TICKS / \
                  ((ServoAx12a._ANGLE_MAX_DEGREE - ServoAx12a._ANGLE_MIN_DEGREE) * math.pi * 2 / 360)  # Ticks per rad

    _CONST_ANGLE_TO_TICKS = ServoAx12a._SPEED_MAX_TICKS / (5 * math.pi / 3)
    _CONST_SPEED_TO_TICKS = ServoAx12a._SPEED_MAX_TICKS / ServoAx12a._SPEED_MAX_RPM

    # Private methods
    # ----------------------------------------------------------------------
    # Constructor, defines the following variables: counterClockWise, angleOffset, angleMax, angleMin
    # servoId -> id of servo, ccw -> rotating direction, aOffset -> angle offset,
    # aMax -> maximum angle allowed, aMin -> minimum angle allowed
    def __init__(self, servoId, ccw=False, aOffset=0.0, aMax=math.pi * 2, aMin=-math.pi * 2):
        self.id = servoId
        self.counterClockWise = ccw
        self.angleMax = aMax if (
                aMin < aMax <= self._ANGLE_RADIAN_MAX and aMax >= self._ANGLE_RADIAN_MIN) else self._ANGLE_RADIAN_MAX
        self.angleMin = aMin if (
                aMax > aMin >= self._ANGLE_RADIAN_MIN and aMin <= self._ANGLE_RADIAN_MAX) else self._ANGLE_RADIAN_MIN
        self.angleOffset = aOffset
        self.curAngle = 0
        super().__init__(servoId)

    # Converts angle in radian to servo ticks
    # angle -> in radian, returns angle in servo ticks
    def __convertAngleToTicks(self, angle: float) -> int:
        if self.counterClockWise:
            angle = self._ANGLE_RADIAN_ZERO + self.angleOffset + angle
        else:
            angle = self._ANGLE_RADIAN_ZERO - self.angleOffset - angle

        return int(round(abs(self._CONST_ANGLE_TO_TICKS * angle)))

    # Converts servo ticks to angle in radian
    # ticks -> servo ticks, returns angle in radian
    def __convertTicksToAngle(self, ticks: int) -> float:
        if self.counterClockWise:
            ticks += self.__convertAngleToTicks(self._ANGLE_RADIAN_ZERO + self.angleOffset)
        else:
            ticks += self.__convertAngleToTicks(self._ANGLE_RADIAN_ZERO - self.angleOffset)

        return ticks / self._CONST_ANGLE_TO_TICKS

    # Converts speed in rpm to servo ticks
    # speed -> value in rpm
    def __convertSpeedToTicks(self, speed: float) -> int:
        ticks = int(
            round(self._SPEED_MAX_TICKS if (speed == self._SPEED_MAX_RPM) else self._CONST_SPEED_TO_TICKS * speed))
        return ticks

    # Converts ticks to speed in rpm
    # ticks -> servo ticks
    def __convertTicksToSpeed(self, ticks: int) -> float:
        speed = (ticks * self._SPEED_MAX_RPM) / self._CONST_SPEED_TO_TICKS
        return speed

    # Public methods
    # ----------------------------------------------------------------------
    # Get current angle of servo
    # returns angle in radian
    def getCurrentJointAngle(self) -> float:
        self.curAngle = self.__convertTicksToAngle(self.getPresentPosition())
        return self.curAngle

    # Set servo to desired angle
    # angle -> in radian,
    def setDesiredJointAngle(self, angle: float, trigger: bool = False) -> bool:
        # convert angle to positive if needed
        if angle < 0:
            angle += 2 * math.pi

        if angle > self.angleMax:
            angle = self.angleMax
        if angle < self.angleMin:
            angle = self.angleMin

        success = self.setGoalPosition(self.__convertAngleToTicks(angle), trigger)
        if success:
            self.curAngle -= angle

        return success

    # Set servo to desired angle and speed
    # angle -> in radian
    # speed -> speed of movement in rpm, speed = 0 -> maximum speed
    def setDesiredAngleSpeed(self, angle: float, speed: float = 0, trigger: bool = False) -> bool:
        # convert angle to positive if needed
        if angle < 0:
            angle += 2 * math.pi

        if angle > self.angleMax:
            angle = self.angleMax
        if angle < self.angleMin:
            angle = self.angleMin

        speed_in_ticks = self.__convertSpeedToTicks(speed)
        angle_in_ticks = self.__convertAngleToTicks(angle)

        success = self.setGoalPosSpeed(angle_in_ticks, speed_in_ticks, trigger)
        if success:
            self.curAngle -= angle

        return success

    # Set servo to desired angle and speed
    # angle -> in radian
    # motor_load -> in radian
    def setDesiredAngleAndMotorLoad(self, angle: float, motor_load: float = 0, trigger: bool = False) -> bool:
        # convert angle to positive if needed
        if angle < 0:
            angle += 2 * math.pi

        if angle > self.angleMax:
            angle = self.angleMax
        if angle < self.angleMin:
            angle = self.angleMin

        if 0 < motor_load <= 100:
            speed_in_ticks = int(round(motor_load * self._SPEED_MAX_TICKS))
            angle_in_ticks = self.__convertAngleToTicks(angle)

            success = self.setGoalPosSpeed(angle_in_ticks, speed_in_ticks, trigger)
            if success:
                self.curAngle -= angle

            return success
        else:
            return False

    # Set speed value of servo
    # speed -> speed of movement in rpm, speed = 0 -> maximum speed
    def setSpeedValue(self, speed: float, trigger: bool = False) -> bool:
        speed_in_ticks = self.__convertSpeedToTicks(speed)
        success = self.setMovingSpeed(speed_in_ticks, trigger)

        return success

    # Set speed value of servo
    # motor_load -> in radian
    def setMotorLoad(self, motor_load: float, trigger: bool = False) -> bool:
        if 0 < motor_load <= 100:
            speed_in_ticks = int(round(motor_load * self._SPEED_MAX_TICKS))
            success = self.setMovingSpeed(speed_in_ticks, trigger)

            return success
        else:
            return False

    def setCounterClockWise(self, ccw: bool):
        self.counterClockWise = ccw

    @staticmethod
    def doActionAllServo():
        dynamixel_broadcast = Dynamixel(Dynamixel.ID_BROADCAST)
        dynamixel_broadcast.action()
