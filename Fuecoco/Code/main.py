import connect as c
from microdot import Microdot
from cors import CORS
import PicoRobotics
import time
import machine
from neopixel import Neopixel
import urandom
import aws

ip = c.startUp()
print(ip)
#checking if the ip address has been updated from aws, not needed
#if aws.writeNew():
#    ip = c.startUp()
#    print(ip)
    
#aws.pushIP(c.getIP())


app = Microdot()
CORS(app, allowed_origins='*', allow_credentials=True)
board = PicoRobotics.KitronikPicoRobotics()
strip = Neopixel(96, 0, 28)
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
    time.sleep(0.001)

def forward():
    board.motorOn(1, "f", 100)
    board.motorOn(2, "r", 100)
    board.motorOn(3, "r", 100)
    
def stop():
    board.motorOn(1, "f", 0)
    board.motorOn(2, "f", 0)
    board.motorOn(3, "f", 0)
    
def backward():
    board.motorOn(1, "r", 100)
    board.motorOn(2, "f", 100)
    board.motorOn(3, "f", 100)
    
def left():
    board.motorOn(1, "f", 0)
    board.motorOn(2, "f", 100)
    board.motorOn(3, "r", 100)
    
def right():
    board.motorOn(1, "f", 0)
    board.motorOn(2, "r", 100)
    board.motorOn(3, "f", 100)
    
def arm():
    print("arms")
    board.servoWrite(1, 65)
    board.servoWrite(5, 30)
    time.sleep(0.5)
    board.servoWrite(1, 90)
    board.servoWrite(5, 25)
    time.sleep(0.5)
    board.servoWrite(1, 55)
    board.servoWrite(5, 50)
    time.sleep(0.5)
    board.servoWrite(1, 65)
    board.servoWrite(5, 30)
    board.adjustServos(0)
    
def leftArm():
    print("left")
    board.servoWrite(5, 30)
    time.sleep(0.5)
    board.servoWrite(5, 25)
    time.sleep(0.5)
    board.servoWrite(5, 50)
    time.sleep(0.5)
    board.servoWrite(5, 30)
    time.sleep(0.5)
    board.adjustServos(0)

def rightArm():
    print("right")
    board.servoWrite(1, 65)
    time.sleep(0.5)
    board.servoWrite(1, 90)
    time.sleep(0.5)
    board.servoWrite(1, 55)
    time.sleep(0.5)
    board.servoWrite(1, 65)
    time.sleep(0.5)
    board.adjustServos(0)
    
def fl():
    board.motorOn(1, "f", 100)
    board.motorOn(2, "r", 10)
    board.motorOn(3, "r", 100)
    
def fr():
    board.motorOn(1, "f", 100)
    board.motorOn(2, "r", 100)
    board.motorOn(3, "r", 20)

def bl():
    board.motorOn(1, "r", 100)
    board.motorOn(2, "f", 10)
    board.motorOn(3, "f", 100)
    
def br():
    board.motorOn(1, "r", 100)
    board.motorOn(2, "f", 100)
    board.motorOn(3, "f", 20)

    
def bounds(value, min_val, max_val):
    return max(min(value, max_val), min_val)


def fire():
    start = time.time()
    end = 2
    while (time.time()-start) < end:
        r = 255
        g = 80
        b = 20

        #Flicker, based on our initial RGB values
        for i in range (0, 96):
            flicker = urandom.randint(0,110)
            r1 = bounds(r-flicker, 0, 255)
            g1 = bounds(g-flicker, 0, 255)
            b1 = bounds(b-flicker, 0, 255)
            strip[i] = (g1,r1,b1)
        strip.show()
        time.sleep(0.1)
    changeNeopixel("null")
    
@app.route('/stop', methods=['POST'])
def motorOn(request):
    print('connented')
    stop()
    return "done"

@app.route('/mu', methods=['POST'])
def motorOn(request):
    print('connented')
    forward()
    return "done"

@app.route('/md', methods=['POST'])
def motorOff(request):
    print('connented')
    backward()
    return "done"

@app.route('/lm', methods=['POST'])
def motorOff(request):
    print('connented')
    left()
    return "done"

@app.route('/lu', methods=['POST'])
def motorOff(request):
    print('connented')
    fl()
    return "done"

@app.route('/ld', methods=['POST'])
def motorOff(request):
    print('connented')
    bl()
    return "done"

@app.route('/rm', methods=['POST'])
def motorOff(request):
    print('connented')
    right()
    return "done"

@app.route('/ru', methods=['POST'])
def motorOff(request):
    print('connented')
    fr()
    return "done"

@app.route('/rd', methods=['POST'])
def motorOff(request):
    print('connented')
    br()
    return "done"

@app.route('/al', methods=['POST'])
def motorOff(request):
    print('connented')
    leftArm()
    return "done"

@app.route('/ar', methods=['POST'])
def motorOff(request):
    print('connented')
    rightArm()
    return "done"

@app.route('/ab', methods=['POST'])
def motorOff(request):
    print('connented')
    arm()
    return "done"

@app.route('fire',methods=['POST'])
def motorOff(request):
    print('connented')
    fire()
    return "done"

print('running app')
app.run(port=80)
