import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685


GPIO.setmode(GPIO.BOARD)

#GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

MOTOR_HIGH = 300
MOTOR_LOW = 200
MOTOR_NUM = 6

while True:
    pwm.set_pwm(0, 0, MOTOR_HIGH)
    time.sleep(0.5)
    pwm.set_pwm(0, 0, MOTOR_LOW)
    time.sleep(0.5)

    """
    for i in range(MOTOR_NUM):
        pwm.set_pwm(i, 0, MOTOR_HIGH)
    time.sleep(1)
    for i in range(MOTOR_NUM):
        pwm.set_pwm(i, 0, MOTOR_LOW)
    time.sleep(1)
    """
  
