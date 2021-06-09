import serial
import lewansoul_lx16a
from time import sleep

SERIAL_PORT = '/dev/ttyUSB0'
IDS = list(range(1, 11))
IDS = list(range(1, 7))

controller = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200, timeout=1),
)

servos = [controller.servo(i) for i in IDS]
print(servos)

for control in [0, 1000, 0, 500, 0, 1000]:
    for servo in servos:
        servo.move_prepare(control)
    controller.move_start()
    sleep(1)
