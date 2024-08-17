import network
import aws
from time import sleep, time
import machine
import binascii
import json
from neopixel import Neopixel
numpix = 96
strip = Neopixel(numpix, 0, 28)
strip.brightness(100)


colour = {
    "red" : (0, 255, 0),
    "orange" : (100, 255, 0),
    "yellow" : (150, 255, 0),
    "green" : (255, 0, 0),
    "cyan" : (128, 0, 128),
    "blue" : (0, 0, 255),
    "purple" : (0, 128, 130),
    "null" : (0,0,0)
}

def changeNeopixel(color):
    strip.fill(colour[color])
    strip.show()
    sleep(0.001)
    

def read_json(dataType):
    with open("network.json") as f:
        data = json.load(f)
    return data[dataType]

def connect(ssid, password):
    changeNeopixel("yellow") 
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()
    
    startTime = time()
    wlan.connect(ssid, password)
    changeNeopixel("green")
    while wlan.isconnected() == False and (time()-startTime) < 30:
        print(wlan.isconnected())
        sleep(1)   
    
def scanForNetwork(ssid):
    changeNeopixel("orange")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()
    startTime = time()
    foundNetwork = False
    sleep(0.5)
    while (time()-startTime) < 5 and not foundNetwork:
        networks = wlan.scan()
        for w in networks:
          print(w[0].decode())
          if w[0].decode() == ssid:
              foundNetwork = True
              return
            
        sleep(0.5)


    raise Exception("Can't find network")
    
def checkConnection():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if wlan.isconnected():
        ip = wlan.ifconfig()[0]
        if ip:
            return True
    else:
        changeNeopixel("cyan")
        sleep(2)
        return False

def getIP():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    try:
        return wlan.ifconfig()[0]
    except:
        changeNeopixel("cyan")
        raise Exception("Can't connect to network")


def tryConnect(info, trys):
    tryCount = 0
    connected = False
    print(tryCount)
    while tryCount < trys and not connected:
        print(tryCount)
        try:
            scanForNetwork(info['ssid'])
            connect(info['ssid'],info['password'])                   
            connected = checkConnection()
        except Exception as e:
            print(e)
        tryCount += 1

def startUp():
    changeNeopixel("red")

    sleep(1)
    tryConnect(read_json("current"), 1)

    if not checkConnection():
        changeNeopixel("blue")
        sleep(1)
        tryConnect(read_json("backup"), 3)
    
    ip = getIP()
    if checkConnection():
        changeNeopixel("null")     
        return ip
    else:
        changeNeopixel("purple")
    
    
    
        

