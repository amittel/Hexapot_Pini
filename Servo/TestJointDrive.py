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
    jointDrive13 = JointDrive(13)
    jointDriveBC = JointDrive(254)

    print('jd8 test moving max speed, angle 2.61')
    #jointDrive8.setMovingSpeed(0, True)
    #jointDrive8.setDesiredJointAngle(2.61, True)
    sleep(2)
    print('jd8 test moving speed 300, angle -2.61')
    jointDrive8.setMovingSpeed(300, True)
    jointDrive8.setDesiredJointAngle(-2.61, True)
    sleep(2)

    print('jd13 test moving speed max, angle 2.61')
    jointDrive13.setMovingSpeed(0, True)
    jointDrive13.setDesiredJointAngle(2.61, True)
    sleep(2)
    print('jd13 test moving speed 300, angle -2.61')
    jointDrive13.setMovingSpeed(300, True)
    jointDrive13.setDesiredJointAngle(-2.61, True)
    sleep(2)

    print('Broadcast moving speed max, angle 0')
    jointDriveBC.setMovingSpeed(0, True)
    jointDriveBC.setDesiredJointAngle(0, True)

    sleep(1)
    print('----test trigger false----')
    sleep(2)
    print('jd8 test moving speed max, angle 2.61')
    jointDrive8.setMovingSpeed(0, False)
    jointDrive8.setDesiredJointAngle(2.61, False)
    sleep(1)
    print('jd13 test moving speed max, angle 2.61')
    jointDrive13.setMovingSpeed(0, False)
    jointDrive13.setDesiredJointAngle(2.61, False)
    sleep(1)
    jointDriveBC.action()

    print('broadcast test moving speed 30, angle 2.5')
    jointDriveBC.setMovingSpeed(30, False)
    jointDriveBC.setDesiredJointAngle(2.5, False)
    sleep(1)
    jointDriveBC.action()

    print('broadcast test moving speed max, angle 2.2')
    jointDriveBC.setMovingSpeed(0, False)
    jointDriveBC.setDesiredJointAngle(2.2, False)
    sleep(1)
    jointDriveBC.action()

    print('broadcast test moving speed max, angle 2.0')
    jointDriveBC.setMovingSpeed(0, False)
    jointDriveBC.setDesiredJointAngle(2.0, False)
    sleep(1)
    jointDriveBC.action()

    print('broadcast test moving speed max, angle -1.5')
    jointDriveBC.setMovingSpeed(0, False)
    jointDriveBC.setDesiredJointAngle(-1.5, False)
    sleep(1)
    jointDriveBC.action()

    print('broadcast test moving speed max, angle 0')
    jointDriveBC.setMovingSpeed(0, False)
    jointDriveBC.setDesiredJointAngle(0, False)
    sleep(1)
    jointDriveBC.action()

    sleep(2)
    print("-----------------------")
    print('test getter jd8')
    #jointDrive8.setMovingSpeed(20, True)
    #jointDrive8.setDesiredJointAngle(2.5, True)
    #sleep(0.4)
    #print('Present speed: ', jointDrive8.getPresentSpeed())
    testGetters(jointDrive8)
    sleep(2)
    print("-----------------------")
    print("test getter jd13")
    testGetters(jointDrive13)
if __name__ == '__main__':
    main()
