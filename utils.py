import requests

ip = '192.168.0.21'
port = 8090
# define GPIO pins
GPIO_pins = (14, 15, 18)  # Microstep Resolution MS1-MS3 -> GPIO Pin
direction = 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin
stepdelay = .005
initdelay = 0.5

# Returns the coordinates of the selected object


def getCurrentCorrdinates():
    return makeRequest()

# Wrapper function
# scope = main => endpoint = [status, plugins, view]
# scope = objects => endpoint = [find, info, listobjecttypes, listobjectsbytype]


def makeRequest(scope='main', endpoint='view'):
    r = requests.get(
        'http://{}:{}/api/{}/{}'.format(ip, port, scope, endpoint))
    if r.status_code == 200:
        return r.json()
    else:
        print('[!] An error occured')

# Once the telescope is focused on plaris (manually), set the view in stellarium


def setPolaris():
    moveStellariumTo('polaris')

# Moves stellarium target to a desired object


def moveStellariumTo(target='polaris'):
    r = requests.post('http://{}:{}/api/main/focus'.format(ip,
                      port), data='target={}'.format(target))
    if r.status_code == 200:
        return r.json()
    else:
        print('[!] An error occured')

# Converts degree, minutes, seconds to best fit step count


def degree2steps(d, m, s):
    res = d + (m / 60) + (s / 3600)
    res = res / 1.8
    decimal, stepFull = math.modf(res)
    step16 = decimal / 0.1125
    return int(stepFull), int(step16)

# Returns the motor set up


def setUpMotor():
    # Declare an named instance of class pass GPIO pins numbers
    motor = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
    return motor

# TODO: This function should be able to select the direction of rotation


def autoMove(motorAR, motorDEC, object='moon'):


def getDirection(h, m, s):
    coords = getCurrentCorrdinates()


def autoMove(motorAR, motorDEC, objeto):

    # Moves the motor at full throttle


def motorFull(motor, clockwise=True, steps=200):
    moveMotor(motor, clockwise, 'Full', steps)

# Moves the motor at 1/16 throttle


def motor16(motor, clockwise=True, steps=200):
    moveMotor(motor, clockwise, '1/16', steps)

# Motor movement wrapper


def moveMotor(motor, clockwise=True, power='Full', steps='200'):
    motor.motor_go(clockwise, power, steps, stepdelay, False, initdelay)
