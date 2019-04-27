from listener import listener
from face import facecheck
from threading import Thread


class Controller:
    print("in controller")
    # constructor for the objects
    def __init__(self):
        self.listen = listener()
        self.face = facecheck()
        print("ROSS")
        #self.run()

    # get command from listener class to constantly check for changes to the Firebase database and storage
    def __get(self):
        self.listen.get(self)

    def __face(self):
        self.face.checking(self)

    # commands to run in the loop
    def commands(self):
        self.__get(self)
        self.__face(self)

    def run(self):
        print("IN RUN")
        while True:
            self.commands()

cont = Controller()
cont.run()

#if __name__ == '__main__':
#    Controller.run()
