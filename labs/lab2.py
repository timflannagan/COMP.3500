import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declare relevant variables
RED = 21
BLUE = 16
GREEN = 24
CYCLE = 20
FLASH = 5

# Setup relevant GPIO pins
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(CYCLE, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(FLASH, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Precondition: none
# Postcondition: function flashes three output pins at once then turns them off
def flash():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    time.sleep(0.4)

def step():
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    
def step1():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    
def step2():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.LOW)

def step3():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.HIGH)

# Precondition: none
# Postcondition: cycles through each light
def cycle():
    step()
    time.sleep(0.2)
    step1()
    time.sleep(0.3)
    step2()
    time.sleep(0.4)
    step3()
    time.sleep(0.5)
            
# Precondition: none
# Postcondition: GPIO outputs are set to False
def __init__():
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)

try:
    while True:
            # Test the flashing lights first
            if (GPIO.input(FLASH) == False):
                    flash()

            if (GPIO.input(CYCLE) == False):
                    cycle()
                    
            else:
                __init__()

            time.sleep(0.1)


except KeyboardInterrupt:
	GPIO.cleanup()
