import math
from time import sleep
from Servo.jointdrive import JointDrive

def resetJointDrive(jointDrive: JointDrive):
    STD_POS = 0  # standard position in ticks
    STD_SPD = 0  # standard speed in ticks
    STD_CCW = False  # standard counter clock wise

    jointDrive.setGoalPosition(STD_POS, True)
    sleep(1)
    jointDrive.setMovingSpeed(STD_SPD, True)
    sleep(1)
    jointDrive.setCounterClockWise(STD_CCW)
    sleep(1)
    print("Reset servo")

def testGetters(jointDrive: JointDrive):
    print("Get current angle of servo: ", jointDrive.getCurrentJointAngle())
    sleep(1)
    print("Get time of return delay: ",   jointDrive.getReturnDelay())
    sleep(1)
    print("Get status return level: ",    jointDrive.getReturnLevel())
    sleep(1)
    print("Get goal position: ",          jointDrive.getGoalPosition())
    sleep(1)
    print("Get moving speed: ",           jointDrive.getMovingSpeed())
    sleep(1)
    print("Get present speed: ",          jointDrive.getPresentSpeed())
    sleep(1)





def main():
    jointDrive8 = JointDrive(8)

    print('jd8 test moving max speed, angle 2.61')
    jointDrive8.setMovingSpeed(300, True)
    jointDrive8.setDesiredJointAngle(2.0, True)

    jointDrive8.getMovingSpeed()
    jointDrive8.getGoalPosition()


if __name__ == '__main__':
    main()
