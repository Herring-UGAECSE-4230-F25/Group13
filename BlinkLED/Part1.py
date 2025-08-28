#Blinking An LED using RPi.GPIO
import RPi.GPIO as GPIO
import time

Frequency = 20

sleepTime = (1/Frequency) / 2

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT,initial=GPIO.LOW)

while True:
    GPIO.output(7, GPIO.HIGH)
    time.sleep(sleepTime)
    GPIO.output(7, GPIO.LOW)
    time.sleep(sleepTime)


