#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
import hashlib
import tempfile
import shutil
import os
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as GPIO
from time import sleep
import random

GREEN = 21
RED = 16
BLUE = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.output(GREEN, 0)
GPIO.output(RED, 0)
GPIO.output(BLUE, 0)

## Search for a finger
##

## Tries to initialize the sensor
def search():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            GPIO.output(BLUE, 1)
            sleep(1)
            GPIO.output(BLUE, 0)
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        GPIO.output(BLUE, 1)
        sleep(1)
        GPIO.output(BLUE, 0)
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to search the finger and calculate hash
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass
        
        print('Downloading image (this take a while)...')

        if (os.path.isfile('/home/pi/webapp/static/fingerprint.bmp')):
            os.remove('/home/pi/webapp/static/fingerprint.bmp')

        imageDestination = '/home/pi/webapp/static/fingerprint.bmp'
        f.downloadImage(imageDestination)
        print('The image was saved to "' + imageDestination + '".')

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            GPIO.output(RED, 1)
            sleep(1)
            GPIO.output(RED, 0)
            print('No match found!')
            return 0
        else:
            GPIO.output(GREEN, 1)
            sleep(1)
            GPIO.output(GREEN, 0)
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))

        ## OPTIONAL stuff
        ##

        ## Loads the found template to charbuffer 1
        f.loadTemplate(positionNumber, 0x01)

        ## Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        ## Hashes characteristics of template
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

        return 1;
        
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)