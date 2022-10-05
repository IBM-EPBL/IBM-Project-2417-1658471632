import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

red=7
yellow=8
green=25

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

while True:
        GPIO.output(red, True)
        print("Red - ON")
        sleep(5)
        GPIO.output(red,False)

        GPIO.output(yellow, True)
        print("Yellow - ON")
        sleep(1)
        GPIO.output(yellow,False)

        GPIO.output(green, True)
        print("Green - ON")
        sleep(3)
        GPIO.output(green,False)
GPIO.cleanup()