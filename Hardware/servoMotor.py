import RPi.GPIO as GPIO
import time
import pigpio

garbagePin = 12
recyclingPin = 13
compostPin = 27
GPIO.setmode(GPIO.BCM)
pi = pigpio.pi()

def openBin(openBin):
    if openBin == 0: #Triggers compost pin
        pi.set_servo_pulsewidth(compostPin, 1000)
        time.sleep(1)
        pi.set_servo_pulsewidth(compostPin, 2000)
    elif openBin == 1: #Triggers recycling pin
        pi.set_servo_pulsewidth(recyclingPin, 1000)
        time.sleep(1)
        pi.set_servo_pulsewidth(recyclingPin, 2000)

    else: #Triggers garbage pin
        pi.set_servo_pulsewidth(garbagePin, 1000)
        time.sleep(1)
        pi.set_servo_pulsewidth(garbagePin, 2000)

def resetServo():
    pi.set_servo_pulsewidth(compostPin, 2000)
    pi.set_servo_pulsewidth(recyclingPin, 2000)
    pi.set_servo_pulsewidth(garbagePin, 2000)
