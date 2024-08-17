import inputs
import outputs
import connect as c
from machine import Pin
import time


stick = inputs.AnalogStick(26,27)
b1 = Pin(20, Pin.IN, Pin.PULL_DOWN) #purple
b2 = Pin(19, Pin.IN, Pin.PULL_DOWN) #yellow
b3 = Pin(18, Pin.IN, Pin.PULL_DOWN) #orange
b4 = Pin(28, Pin.IN, Pin.PULL_DOWN) 
c.startUp()
#check aws for new ip/wifi

while True:
    time.sleep(0.2)
    direction = stick.getDir()
    if direction != ["m","m"]:
        print(direction[0],direction[1])
        print(outputs.moveLegs(direction))
        #time.sleep(0.1)
    elif b1.value():
        print("right")
        outputs.moveArms("r")
        time.sleep(2)
    elif b2.value():
        print("left")
        outputs.moveArms("l")
        time.sleep(2)
    elif b3.value():
        print("both")
        outputs.moveArms("b")
        time.sleep(2)
    elif b4.value():
        print("fire")
        outputs.breatheFire()
        time.sleep(1)
    else:
        outputs.stop()
    #c.checkConnection()