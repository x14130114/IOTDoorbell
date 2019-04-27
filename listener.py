# import alsaaudio
import sys
from self import self
from firebase import Firebase
import RPi.GPIO as GPIO
from threading import Thread
from lock import Solenoid
from new_face import new_face
# from train_face import trainFace
# from facial_recognition import FacialRecognition
import time
import os

# creating objects for other methods in seperate classes
# fr = FacialRecognition()
# tface = trainFace()
nface = new_face()
door = Solenoid()
fb = Firebase()

class listener:
    print("in listener")

    # get method
    def get(self):
        # oldpos = ""
        while True:
            try:
                print("Starting the loop for checking values on Firebase")
                data = fb.get_data()
                # getting firebase values
                lock = data['doorbell']['lock']['state']
                face = data['doorbell']['face']['state']
                camera = data['doorbell']['camera']['state']
                audio = data['doorbell']['audio']['state']
                time.sleep(.5)
                print(lock)

                # checking if door has been unlockedd
                if lock == "open":
                    print ("The lock has been opened")
                    Solenoid.unlock_door(Solenoid.lock)
                    readings = {'doorbell/lock/state': "closed"}
                    fb.update_data(readings)

                # take pictures for new face recognition
                if face == "new":
                    print ("New face being added..")
                    nface.take_pictures()
                    print ("Face Added and Trained")
                    readings = {'doorbell/face/state': "added"}
                    fb.update_data(readings)
                # elif face == "train":
                #    print ("Face being trained")
                #    tface.train_faces()
                #    readings = {'doorbell/face/state': "trained"}
                #    fb.update_data(readings)

                if camera == "start":
                    print ("camera start")
                    os.system("docker start youtube")
                    readings = {'doorbell/camera/state': "waiting"}
                    fb.update_data(readings)
                elif camera == "stop":
                    print ("camera stop")
                    os.system("docker stop youtube")
                    readings = {'doorbell/camera/state': "waiting"}
                    fb.update_data(readings)

                if audio == "new":
                    fb.download_file()
                    print ("new audio")
                    #file = "audio.mp3"
                    # m = alsaaudio.Mixer("PCM")
                    # current_volume = m.getvolume()  # Get the current Volume
                    # m.setvolume(75)  # Set the volume to 70%.
                    # print (current_volume)
                    #os.system("mpg123 " + file)
                    os.system("omxplayer audio.mp3")
                    readings = {'doorbell/audio/state': "waiting"}
                    fb.update_data(readings)

            except KeyboardInterrupt:
                #p.stop()
                GPIO.cleanup()
                sys.exit(0)
                #threadGet.join()
                print ("Interrupted")

    #def threads(self):
    #    print("STARTING LISTENER")
    #    threadGet = Thread(target=self.get())
    #    threadGet.start()
    #    threadGet.join()

#print("before thread")
#listener.threads(self)
# running the main
#if __name__ == '__main__':
#    print("IN MAIN")
    # setup threads
#    threadGet = Thread(target=listener.get(self))
        # start threads
#    threadGet.start()
        # join threads
#    threadGet.join()