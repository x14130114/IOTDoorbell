import self

from listener import listener
from camera import bellcam
from threading import Thread
import time

class Controlling:
    listen = listener()
    bell = bellcam()
    b = bell.set_btn()
    #print(b)

    def __init__(self):
        self.listen = listener()
        self.bell = bellcam()
        b = self.bell.set_btn()
        print(b)

    def run(self):

        bell_thread = Thread(target=self.button_pressed())
        listener_thread = Thread(target=self.listen.get())

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
            #print(Controlling.b)
            time.sleep(.1)
            #bellcam.set_btn(self)
            if bellcam.set_btn(self) is True:
                #self.bell.take_photo()
                bellcam.take_photo(self)

    def listen(self):
        while True:
            #self.listen.get()
            listener.get(self)

# Create a new ComplexNumber object
#c1 = Controlling()

# Call function
#c1.run()

    if __name__ == '__main__':
        print("IN MAIN")
        bell_thread = Thread(target=button_pressed, args=(self,))
        listener_thread = Thread(target=listen, args=(self,))

        bell_thread.start()
        listener_thread.start()

        bell_thread.join()
        listener_thread.join()

