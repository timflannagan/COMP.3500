import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(28, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(14, GPIO.IN)
GPIO.setup(30, GPIO.IN)

counter = 0

while True:
    if ((counter & 3) == 0):
        GPIO.output(24, False)
        GPIO.output(28, False)
        GPIO.output(29, False)
    if ((counter & 3) == 1):
        GPIO.output(24, True)
        GPIO.output(28, False)
        GPIO.output(29, False)
    if ((counter & 3) == 2):
        GPIO.output(24, True)
        GPIO.output(28, True)
        GPIO.output(29, False)
    if ((counter & 3) == 3):
        GPIO.output(24, True)
        GPIO.output(28, True)
        GPIO.output(29, True)
        
    if (GPIO.input(30) == True):
        print "Counter has been reset"
        counter = 0
    if (GPIO.input(30) == True):
        counter = counter + 1
        print "Counter has been pressed"
        
    sleep(1);