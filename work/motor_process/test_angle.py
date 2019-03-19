import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

import sys
angle = int(sys.argv[1])

GPIO.setmode(GPIO.BOARD)

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

MOTOR_HIGH = 400
MOTOR_LOW = 350
DIFF = MOTOR_HIGH - MOTOR_LOW
RANGE = 100

print("setup end")

while True:
    print("iter...")
    for i in range(RANGE):
        pwm.set_pwm(0, 0, int(MOTOR_LOW + i * DIFF / RANGE))
        time.sleep(1/RANGE)
    for i in range(RANGE):
        pwm.set_pwm(0, 0, int(MOTOR_HIGH - i * DIFF / RANGE))
        time.sleep(1/RANGE)
    time.sleep(1)
    """
    for i in range(RANGE):
        pwm.set_pwm(1, 0, int(MOTOR_LOW + i * DIFF / RANGE))
        time.sleep(1/RANGE)
    for i in range(RANGE):
        pwm.set_pwm(1, 0, int(MOTOR_HIGH - i * DIFF / RANGE))
        time.sleep(1/RANGE)
    for i in range(RANGE):
        pwm.set_pwm(2, 0, int(MOTOR_LOW + i * DIFF / RANGE))
        time.sleep(1/RANGE)
    for i in range(RANGE):
        pwm.set_pwm(2, 0, int(MOTOR_HIGH - i * DIFF / RANGE))
        time.sleep(1/RANGE)
    time.sleep(1)
    """
