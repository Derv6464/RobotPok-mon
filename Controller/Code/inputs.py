from machine import ADC, Pin
from time import sleep


class AnalogStick:
    def __init__(self, xPin, yPin):
        self.x = ADC(xPin)
        self.y = ADC(yPin)
        
    def read(self):
        adc_valuey = self.y.read_u16()
        adc_valuex = self.x.read_u16()
    
        voltY = (3.3/65535)*adc_valuey
        voltX = (3.3/65535)*adc_valuex
    
        return [voltX, voltY]
    
    def getDir(self):
        volts = self.read()
        voltX = volts[0]
        voltY = volts[1]
        
        if voltX > 2.8:
            dirX = "r"
        elif voltX < 1:
            dirX = "l"
        else:
            dirX = "m"
    
        if voltY > 2.8:
            dirY = "u"
        elif voltY < 1:
            dirY = "d"
        else:
            dirY = "m"
            
        return [dirX, dirY]
    


            
        
        