import pygame
import math
from threading import Thread

class Controller:

    def __init__(self):
        # initialise Pygame 
        pygame.init()

        # Joystick
        self.joystickName = ""

        # Button ID
        self.buttonA = 0
        self.buttonB = 1
        self.buttonX = 2
        self.buttonY = 3
        self.buttonLB = 4
        self.buttonRB = 5

        # 0 = Robot leg low, 1 = Robot leg high
        self.ButtonLeghight = 0

        # X/Y Coordinates
        self.axis1_X = 0
        self.axis1_Y = 0

        self.axis2_Y = 0
        self.axis2_X = 0

        # Angle from Joystick left
        self.winkel1 = 0

        # Velocity Abs (from Joystick right)
        self.speed = 0

        # Controller detected
        self.controllerDetected = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Initialise the joysticks
        pygame.joystick.init()

        joysticks = []

        for i in range(0, pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
            joysticks[-1].init()
            self.joystickName = joysticks[-1].get_name()
            self.controllerDetected = True

        con_thread = Thread(target=self.readController, args=())
        con_thread.start()

    def __del__(self):
        # Quit Pygame
        pygame.quit()

    # Translate radiant in Robotlanguage (y = Angle - 1/2 pi)
    def winkelUmrechnen(self):
        self.winkel1 = self.winkel1 - (1/2 * math.pi)

    # Getter
    def getAngleDirection(self):
        return self.winkel1

    def getVelocity(self):
        if self.speed > 1:
            return 1
        if self.speed < -1:
            return 0
        return self.speed

    def getButtonLeghight(self):
        return self.ButtonLeghight

    def getControllerName(self):
        return self.joystickName

    def getControllerDetected(self):
        return self.controllerDetected


    def readController(self):
        # -------- Main Program Loop -----------

        while True:

            joystick = pygame.joystick.Joystick(0)
            # Limit to 60 frames per second
            self.clock.tick(60)
            # EVENT PROCESSING STEP
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop

                if event.type == pygame.JOYBUTTONDOWN:
                    # Possible action: "Button pressed"
                    if event.button == self.buttonLB:
                        self.ButtonLeghight = 1
                    if event.button == self.buttonRB:
                        self.ButtonLeghight = 0
                   
                
                #Left stick
                
                self.axis1_X = -joystick.get_axis(1)
                self.axis1_Y =  joystick.get_axis(0)

                #Right stick 
                
                self.axis2_X = joystick.get_axis(4)
                self.axis2_Y = - joystick.get_axis(3)
                
                #Right stick abs
                
                self.rightStickBetrag = math.sqrt(self.axis2_X ** 2 + self.axis2_Y ** 2)
               
                # Joystick Left: Coordinates Angle(rad)

                if (self.axis1_X < 0.3 and self.axis1_X > -0.3 and self.axis1_Y < 0.3 and self.axis1_Y > -0.3):
                    self.winkel1 = 0.0
                else:
                    self.winkel1 = math.atan2(self.axis1_Y, self.axis1_X)

                # Right Stick fuer absoluten Wert fragen
                if (self.axis2_Y > 0):
                    self.speed = self.rightStickBetrag
                if (self.axis2_Y < 0):
                    self.speed = - self.rightStickBetrag
