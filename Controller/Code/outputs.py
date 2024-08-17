import urequests
import connect as c
from machine import Pin

#may need to change this to the ip address of the robot
url = "http://172.20.10.3:80/"
led = Pin(9, Pin.OUT)

def moveLegs(direction):
    x = direction[0]
    y = direction[1]
    print(url + x + y)
    
    makeRequest(x + y)
   
    
def moveArms(arm):
    makeRequest("a"+ arm)
    
def breatheFire():
    makeRequest("fire")
    
def stop():
    makeRequest("stop")
    
def makeRequest(endpoint):
    try:
        print(url + endpoint)
        r = urequests.post(url + endpoint)
        if r.content:
            led.value(0)
            return True
        else:
            led.value(1)
            return False
    except:
        led.value(1)
        return False
        