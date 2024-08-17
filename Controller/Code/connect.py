import network
from time import sleep, time
import machine
import binascii
from machine import Pin
import json

nood = Pin(8, Pin.OUT) 

def blinkLED(times):
    for i in range(times):
        nood.value(1)
        sleep(0.2)
        nood.value(0)
        sleep(0.2)

def read_json(dataType):
    with open("network.json") as f:
        data = json.load(f)
    return data[dataType]


def connect(ssid, password):
    blinkLED(3) 
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()
    
    startTime = time()
    wlan.connect(ssid, password)
    blinkLED(4)
    while wlan.isconnected() == False and (time()-startTime) < 30:
        print(wlan.isconnected())
        sleep(1)
        
def scanForNetwork(ssid):
    blinkLED(2)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()
    startTime = time()
    foundNetwork = False
    sleep(0.5)
    while (time()-startTime) < 15 and not foundNetwork:
        networks = wlan.scan()
        for w in networks:
          print(w[0].decode())
          if w[0].decode() == ssid:
              print("found")
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
        blinkLED(5)
        sleep(2)
        return False

def tryConnect(info, trys):
    tryCount = 0
    connected = False
    ssid = info['ssid']
    password = info['password']
    while tryCount < trys and not connected:
        try:
            scanForNetwork(ssid)
            connect(ssid,password)                   
            connected = checkConnection()
        except Exception as e:
            print(e)
        tryCount += 1


def getIP():
    pass
            
def startUp():
    blinkLED(1)
    sleep(1)
    tryConnect(read_json("current"), 5)
    connected = checkConnection()
    if not connected:
        blinkLED(6)
        sleep(1)
        tryConnect(read_json("backup"), 3)
    
    ip = getIP()
    if checkConnection():
        nood.value(1)
        return ip
    else:
        nood.value(0)