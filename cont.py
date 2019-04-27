
#from face import facecheck
#from camera import bellcam
from listener import listener

class Control:

    def __init__(self):
        self.listen = listener()
        #self.face = facecheck()
        #self.bell = bellcam()
        print("init")

    def getData(self):
        print("getting data")
        # Calling the method to start the thread to get from firebase
        #self.bell.thread()
        #self.bell.bell_pressed()
        self.listen.threads()
        #self.face.checking()

    def run(self):
        while True:
            self.getData()

# Create a new ComplexNumber object
c1 = Control()

# Call function
c1.run()

