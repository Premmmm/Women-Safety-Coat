import RPi.GPIO as GPIO
import time

channel=21

Gpio.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def motor_on(pin):
	GPIO.output(pin,GPIO.HIGH)

def motor_off(pin):
	GPIO.output(pin,GPIO.LOW)

if __Name__ == '__main__':
	try:
		motot_on(channel)
		time.sleep(1)
		motor_off(chcannel)
		time.sleep(1)
		GPIO.cleanup()
	except KeyboardINterrupt:
		GPIO.cleanup()
		pass