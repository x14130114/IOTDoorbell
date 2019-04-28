import self

from listener import listener
from camera import bellcam
#from face import facecheck
#from test2 import check
from threading import Thread, ThreadError
import time

class Controlling:
    listen = listener()
    bell = bellcam()
    #fcheck = facecheck()
    #ck = check()

    def __init__(self):
        self.listen = listener()
        self.bell = bellcam()
       # self.faced = facecheck()
       # self.ck()

    def run(self):
        bell_thread = Thread(target=Controlling.button_pressed, args=(self,))
        listener_thread = Thread(target=Controlling.listen, args=(self,))
        #bell_thread.setDaemon(True)
        #listener_thread.setDaemon(True)
        bell_thread.start()
        listener_thread.start()
        bell_thread.join()
        listener_thread.join()
        while True:
            pass

    def button_pressed(self):
        while True:
            print(bellcam.set_btn(self))
            time.sleep(.1)
            if bellcam.set_btn(self) is True:
                #self.bell.take_photo()
                bellcam.take_photo(self)

    def listen(self):
        while True:
            #self.listen.get()
            listener.get(self)

    def face(self):
        while True:
            try:
                print("")
            #self.fcheck.checking()
                #facecheck.checking(self)
            except ImportError as e:
                print(e)

# Create a new ComplexNumber object
c1 = Controlling()

# Call function
c1.run()

    #if __name__ == '__main__':
     #   print("IN MAIN")
      #  try:
            #bell_thread = Thread(target=button_pressed, args=(self,))
            #listener_thread = Thread(target=listen, args=(self,))
            #face_thread = Thread(target=face, args=(self,))

            #bell_thread.start()
            #listener_thread.start()
            #face_thread.start()

            #bell_thread.join()
            #listener_thread.join()
            #face_thread.join()
       # except ThreadError:
        #    print(ThreadError)

