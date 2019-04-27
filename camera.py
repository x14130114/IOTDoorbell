from picamera import PiCamera
from time import sleep
from datetime import datetime
import time
import sys
from pushbullet import Pushbullet
from gpiozero import Button
from threading import Thread

# connecting to push bullet api
from self import self

pb = Pushbullet("o.xWndImaQeTc7WvQC6tK3yyTAJVdBKxrU")
# push = pb.push_note("Title","body")
pushes = pb.get_pushes()

# check the available devices
print(pb.devices)
# samsung = pb.get_device('Samsung SM-G950F')
# set your device
huawei = pb.get_device('HUAWEI HMA-L29')

button = Button(18)
camera = PiCamera()
now = datetime.now()
filename = ''


class bellcam:

    def take_photo(self):
        global filename
        # change this naming convention as it is not working
        filename = 'bell.jpg'
        camera.resolution = (800, 600)
        # camera.rotation = 180
        # camera.start_preview()
        # sleep(1)
        camera.capture('/home/pi/Desktop/DoorbellIoT/SPdoorbell/' + (filename))
        # camera.stop_preview
        bellcam.push_notification(self)

    # when button is pressed, send_push notification to phone via pushbullet api
    def push_notification(self):
        print ('sending push notification with image...')
        with open("bell.jpg", "rb") as pic:
            img = pb.upload_file(pic, "Visitor at the door")
        huawei.push_file(**img)
        # push1 = pb.push_file(file_url="/home/pi/Desktop/Bmc/pb/bell.jpg", file_name="bell.jpg", file_type="image/jpeg")
        # push1 = samsung.push_note("Doorbell Alert","Visitor at the door..")
        print ('sent........')

    # def thread(self):
    #    print("STARTING BELL")
    #    threadBell = Thread(target=bellcam.bell_pressed(self))
    #    threadBell.start()
    #    threadBell.join()

    def bell_pressed(self):
        while True:
            print(button.value)
            time.sleep(2)
            # button.when_released
            if button.value is True:
                bellcam.take_photo(self)

    def set_btn(self):
        btn = button.value
        return btn

# btn = button.value()

# while True:
#	bellcam.bell_pressed(self)
# bellcam.thread(self)

# pbullet = samsung.push('IMAGE_MESSAGE', /home/pi/Desktop/bmc.png)
# push = pb.push_note("Title","body")
# pb.pushFile(devices[1]["Samsung SM-G950F"], "Intruder Alert!", "Image From PiCam", open(fileName, "bell.png"))
# push = pb.pushNote(devices[1]["iden"], 'Hello world', 'Test body')
