from picamera import PiCamera
from time import sleep

async def capture(resolution, start_idx):
    camera = PiCamera(resolution = resolution)
    camera.capture(f'/home/pi/Pictures/image{start_idx}.jpg')
    sleep(1)