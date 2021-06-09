'''
Motors:
    1: Back right
    2: Front right
    3: Front left
    4: Back left
    5: Middle right
    6: Middle left
    7: Back left steering
    8: Front left steering
    9: Back right steering
    10: Front right steering
'''

from time import sleep
import serial
import lewansoul_lx16a

class Rover:
    def __init__(self):
        self.controller = lewansoul_lx16a.ServoController(serial.Serial('/dev/ttyUSB0', 115200, timeout=5))
        self.drivers = [self.controller.servo(i) for i in range(1, 7)]
        self.back_left_steer = self.controller.servo(7)
        self.front_left_steer = self.controller.servo(8)
        self.back_right_steer = self.controller.servo(9)
        self.front_right_steer = self.controller.servo(10)
        # calibrate motors

    def move_forward(self, speed, time):
        for motor in self.drivers:
            motor.set_motor_mode(speed)
        sleep(time)
        for motor in self.drivers:
            motor.set_motor_mode(0)

    def move_backward(self, speed, time):
        self.move_forward(-speed, time)

