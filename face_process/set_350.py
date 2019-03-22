import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685
import sys

GPIO.setmode(GPIO.BOARD)


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

MOTOR_LOW = 350

pwm.set_pwm(int(sys.argv[1]), 0, MOTOR_LOW)
time.sleep(0.5)
print("set up finished...")
  
