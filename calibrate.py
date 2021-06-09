import serial
import lewansoul_lx16a
from time import sleep

SERIAL_PORT = '/dev/ttyUSB0'
IDS = list(range(1, 11))

controller = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200, timeout=30),
)

servos = [controller.servo(i) for i in IDS]

for servo in servos:
    print(servo.get_position(timeout=1))
    # servo.set_servo_mode()
    # print(servo.get_servo_id())
    # print(servo.get_mode())
    # print(servo.get_position_offset())
