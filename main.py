import math
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
import utils

# Declare an named instance of class pass GPIO pins numbers
#mymotortest = utils.setUpMotor()

#stepFull, step16 = utils.degree2steps(19,60,54)

utils.setPolaris()

print(utils.getCurrentCorrdinates())
