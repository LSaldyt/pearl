from picamera import PiCamera
from time import sleep, time
#from sense_hat import SenseHat

#sense = SenseHat()
camera = PiCamera()

# preview needs a monitor or something to display
camera.start_preview()
for i in range(10):
    # sense.clear()
    # pres = sense.get_pressure()
    # print('pressure: ', pres)
    # temp = sense.get_temperature()
    # print('temperature: ', temp)
    # humidity = sense.get_humidity()
    # print('humidity: ', humidity)
    #print(str(int(time()))+'.jpg')
    filename = 'images/' + str(int(time())) + '.jpg'
    camera.capture(filename)
    sleep(10)

# to record video:
# camera.start_recording(str(int(time()))+'.h264'
#sleep(10) # len video
#camera.stop_recording()
#
#camera.stop_preview()
#
#w = (255, 255, 255)
#b = (0, 0, 255)
#
#pixels = [
#    w, w, w, w, w, w, w, w,
#    w, w, b, w, w, b, w, w,
#    w, w, b, w, w, b, w, w,
#    w, w, w, w, w, w, w, w,
#    w, b, w, w, w, w, b, w,
#    w, w, b, w, w, b, w, w,
#    w, w, w, b, b, w, w, w,
#    w, w, w, w, w, w, w, w
#]
#sense.set_pixels(pixels)
