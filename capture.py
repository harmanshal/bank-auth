from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (320, 240)
camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
sleep(5)
camera.capture('dataset/picture.jpg')
camera.stop_preview()