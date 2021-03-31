#TODO - fill this out on a RaspberryPi
#import RPi.GPIO as GPIO

def setPin(num, val):
    #TODO - replace this
    print("Setting pin ", num, " to ", val)

#7-segment number codes
numbers = {0: [1,1,1,0,1,1,1],
           1: [0,0,1,0,0,1,0],
           2: [1,0,1,1,1,0,1],
           3: [1,0,1,1,0,1,1],
           4: [0,1,1,1,0,1,0],
           5: [1,1,0,1,0,1,1],
           6: [1,1,0,1,1,1,1],
           7: [1,0,1,0,0,1,0],
           8: [1,1,1,1,1,1,1],
           9: [1,1,1,1,0,1,1]}

class SevenSegment:
    def __init__(self, a, b, c, d, e, f, g, decimal=None):
        """Creates a seven segment display. Top, TL, TR, Middle, BL, BR, Bottom"""
        self.pins = [a,b,c,d,e,f,g]
        self.decimal = decimal

    def clear(self):
        for pin in self.pins:
            setPin(pin, 0)
            setPin(self.decimal, 0)

    def showNumber(self, num, decimal=False):
        number = numbers[num]
        for i in range(0,7):
            setPin(self.pins[i], number[i])
        setPin(self.decimal, decimal)