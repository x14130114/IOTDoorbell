from threading import Thread
from time import sleep

from self import self

from facial_recognition import FacialRecognition
from lock import Solenoid

fr = FacialRecognition()
lock = Solenoid()
id = 0
face = True

class facecheck:

    print("IN FACECHECK")
    id = 0
    def counter(self):
        c = 0
        while c < 3:
            c = c + 1
            sleep(1)

    def check(self):
        global face
        c = Thread(target=facecheck.counter, args=(self, ))
        c.daemon = True
        c.start()
        while c.is_alive():
            res = fr.recognize()
            print(res)
            if res is not None:
                print("%s, %s" % (id, res))
                if id != res[0]:
                    face = False
                    print (face)
                elif id == res[0] and res[1] > 70:
                    face = False
                    print (face)
                    break

    # function to replicate the below code
    def checking(self):
        print("CHECKING")
        #while True:
        #sleep(5)
        res = fr.recognize()
        print (res)
        if res is not None and res[1] < 80:
            id = res[0]
            t = Thread(target=facecheck.check, args=(self, ))
            t.start()
            t.join()
            #if id is res[0] and res[1] < 50:
            face = True
            print("unlocked")
            print(face)
            #Solenoid.unlock_door(Solenoid.lock)
            #sleep(5)

print("END FACECHECL")
while True:
    facecheck.checking(self)
    #sleep

#if __name__ == '__main__':
#    while True:
#        res = fr.recognize()
#        print (res)
#        if res is not None:
#            id = res[0]
#            t = Thread(target=facecheck.check(self))
#            t.start()
#            t.join()
#            if id is res[0] and res[1] < 85:
#                face = True
#                print("unlock")
                #Solenoid.unlock_door(Solenoid.lock)
#           # GPIO.cleanup()
#           # face = False
#            print(face)

