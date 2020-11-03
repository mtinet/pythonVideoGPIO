import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)

print "Press the button!"

try:
    while True:
        if GPIO.input(18) == 1:
            print "Button pressed!"
        else :
            print "Button Released!"

except KeyboardInterrupt:
    GPIO.cleanup()

