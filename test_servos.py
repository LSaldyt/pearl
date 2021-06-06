import serial
import lewansoul_lx16a
from time import sleep

SERIAL_PORT = '/dev/ttyUSB0'
IDS = list(range(1, 11))

controller = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200, timeout=1),
)

servos = [controller.servo(i) for i in IDS]

for servo in servos:
    servo.move(500)
    sleep(1)
 
for servo in servos:
    servo.move_prepare(0)

controller.move_start()
