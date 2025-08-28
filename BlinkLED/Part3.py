#Blinking An LED using pigpio
import pigpio as GPIO

Freq = 7000
x = 0

pi=GPIO.pi()
pi.set_PWM_frequency(4, Freq)
pi.set_PWM_dutycycle(4, 30)

while True:
    x += 0.01
    if x > 1000000:
        pi.set_PWM_dutycycle(4, 0)
        break

