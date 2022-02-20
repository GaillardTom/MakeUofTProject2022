#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

DIO = 11
CLK = 15
STB = 12

LSBFIRST = 0                                                                                                                                                                                                                                                                                                                                                                                                                                          
MSBFIRST = 1

tmp = 0

def _shiftOut(dataPin, clockPin, bitOrder, val):
    for i in range(8):
        if bitOrder == LSBFIRST:
            GPIO.output(dataPin, val & (1 << i))
        else:
            GPIO.output(dataPin, val & (1 << (7 -i)))
        GPIO.output(clockPin, True)
        time.sleep(0.000001)
        GPIO.output(clockPin, False)
        time.sleep(0.000001)
        
def bitRead(value, bit):
    return value & (1 << bit)

def pickDigit(digit):
    print('test')
def sendCommand(cmd):
    GPIO.output(STB, False)
    _shiftOut(DIO, CLK, LSBFIRST, cmd)
    GPIO.output(STB, True)

def TM1638_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DIO, GPIO.OUT)
    GPIO.setup(CLK, GPIO.OUT)
    GPIO.setup(STB, GPIO.OUT)
    sendCommand(0x8f)

def numberDisplay(num):
    digits = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]
    sendCommand(0x40)
    firstNum = int(num/1000%10)
    secNum = int(num/100 % 10)
    thirdNum = int(num/10% 10)
    fourthNum = int(num%10)

    GPIO.output(STB, False)
    _shiftOut(DIO, CLK, LSBFIRST, 0xc0)
    _shiftOut(DIO, CLK, LSBFIRST, digits[firstNum])
    _shiftOut(DIO, CLK, LSBFIRST, 0x00)
    _shiftOut(DIO, CLK, LSBFIRST, digits[secNum])
    _shiftOut(DIO, CLK, LSBFIRST, 0x00)
    _shiftOut(DIO, CLK, LSBFIRST, digits[thirdNum])
    _shiftOut(DIO, CLK, LSBFIRST, 0x00)
    _shiftOut(DIO, CLK, LSBFIRST, digits[fourthNum])
    _shiftOut(DIO, CLK, LSBFIRST, 0x00)
    GPIO.output(STB, True)



