#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import RPi.GPIO as GPIO
import time


VIDEO_PATH = Path("black.mp4")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

player = OMXPlayer(VIDEO_PATH)
sleep(3)
player.quit()

try:
    while True:
        if GPIO.input(18) == 0:
            player = OMXPlayer(VIDEO_PATH)
            sleep(3)
            player.quit()
        else :
            print ("Button Pressed!")

except KeyboardInterrupt:
    GPIO.cleanup()


