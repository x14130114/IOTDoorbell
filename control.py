from listener import listener
from camera import bellcam
from threading import Thread
import time

class Controlling:

    def __init__(self):
        self.listen = listener()
        self.bell = bellcam()

    def run(self):
        listener_thread = Thread(target=self.listen.get())
        listener_thread.setDaemon(True)
        listener_thread.start()
        #listener_thread.join()

        bell_thread = Thread(target=self.button_pressed())
        bell_thread.setDaemon(True)
        bell_thread.start()
        #bell_thread.join()

        while True:
            pass

    def button_pressed(self):
        while True:
            #btn = self.bell.
            print(self.bell.set_btn())
            time.sleep(2)
            # button.when_released
            if self.bell.set_btn() is True:
                self.bell.take_photo()

# Create a new ComplexNumber object
c1 = Controlling()

# Call function
c1.run()

