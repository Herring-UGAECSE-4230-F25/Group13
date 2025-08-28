#Blinking An LED using wiringpi
import wiringpi as GPIO

Freq = 20
x = 0

GPIO.wiringPiSetup()

GPIO.softToneCreate(7)
GPIO.softToneWrite(7, Freq)

while True:
    x += 0.01
    if x > 1000000:
        GPIO.softToneWrite(7, 0)
        break
    

