import rover

rover = rover.Rover()
try:
    while True:
        rover.move_forward(1000, 1)
        rover.move_forward(0, 1)
        rover.move_forward(-1000, 1)
finally:
    rover.move_forward(0, 1)
