import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
GPIO.setup(5, GPIO.IN)

count = 0;

while True:
    if ((count & 3) == 0):
        GPIO.output(16, False)
        GPIO.output(21, False)
        GPIO.output(24, False)
        
    if ((count & 3) == 1):
        GPIO.output(16, True)
        GPIO.output(21, False)
        GPIO.output(24, False)
        
    if ((count & 3) == 2):
        GPIO.output(16, True)
        GPIO.output(21, True)
        GPIO.output(24, False)
        
    if ((count & 3) == 3):
        GPIO.output(16, True)
        GPIO.output(21, True)
        GPIO.output(24, True)
        
    if (GPIO.input(5) == 1):
        count = 0
    
    if (GPIO.input(20) == 1):
        count = count + 1
        
    sleep(1)