from gpiozero import LED
from time import sleep

#initialize each segment of the seven degment led
ledF = LED(5)
ledG = LED(26)
ledE = LED(19)
ledD = LED(6)
ledDP = LED(25)
ledC = LED(21)
ledB = LED(16)
ledA = LED(20)

#turn seven segment led off
def segOff():   
    ledF.on()
    ledG.on()
    ledE.on()
    ledD.on()
    ledDP.on()
    ledC.on()
    ledB.on()
    ledA.on()

#display c on seven segment led
def segC():
    ledF.on()
    ledG.off()
    ledE.off()
    ledD.off()
    ledDP.on()
    ledC.on()
    ledB.on()
    ledA.on()

#display g on seven segment led
def segG():
    ledF.off()
    ledG.off()
    ledE.on()
    ledD.off()
    ledDP.on()
    ledC.off()
    ledB.off()
    ledA.off()

#display r on seven segment led
def segR():
    ledF.on()
    ledG.off()
    ledE.off()
    ledD.on()
    ledDP.on()
    ledC.on()
    ledB.on()
    ledA.on()

#update display on seven segment display depending on which bin is open
def updateSeg(bin):
    if bin == 'compost':
        segC()
    elif bin == 'garbage':
        segG()
    elif bin == 'recycling':
        segR()
    else:
        segOff()
    
