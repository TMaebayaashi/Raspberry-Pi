import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

forlength = range(0, 100)


while True:
	pwm_led.ChangeDutyCycle(0)
	time.sleep(0.2)
	pwm_led.ChangeDutyCycle(100)
	time.sleep(0.1)
	


"""
while True:
	for x in forlength:
		pwm_led.ChangeDutyCycle(x)
		time.sleep(0.03)
	time.sleep(0.5)
		
	for x in reversed(forlength):
		pwm_led.ChangeDutyCycle(x)
		time.sleep(0.03)
	time.sleep(0.5)
"""

"""
while True:
	duty_s = raw_input("Enter Brightness (0 to 100):")
	duty = int(duty_s)
	pwm_led.ChangeDutyCycle(duty)
"""
