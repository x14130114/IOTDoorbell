import RPi.GPIO as GPIO
from threading import Thread
from time import sleep
from facial_recognition import FacialRecognition
from lock import Solenoid

fr = FacialRecognition()
lock = Solenoid()
id = 0
face = True

def counter():
    c = 0
    while c < 7:
        c = c + 1
        sleep(1)

def check():
    global face
    c = Thread(target=counter)
    c.daemon = True
    c.start()
    while c.is_alive():
        res = fr.recognize()
        if res is not None:
            print("%s, %s" % (id, res))
            if id != res[0]:
                face = False
                print (face)
            elif id == res[0] and res[1] > 70:
                face = False
                print (face)
            #elif id == res[0] and res[1] < 80:
            #    face = True
            #    Solenoid.unlock_door(Solenoid.lock)
                break

if __name__ == '__main__':
    while True:
        res = fr.recognize()
        #print("%s, %s" % (id, res))
        print (res)
        #res[0] = id
        #print (id)
        #sleep(.5)
        if res is not None and res[1] < 77:
            id = res[0]
            t = Thread(target=check)
            t.start()
            t.join()
            face = True
            Solenoid.unlock_door(Solenoid.lock)
            #GPIO.cleanup()
            #face = False
            print(face)

GPIO.cleanup()
