#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685 as PCA9685

GPIO.setmode(GPIO.BOARD)
pwm = PCA9685.PCA9685()
pwm.set_pwm_freq(60)

MOTER_HIGH = 400
MOTER_LOW = 350
DIFF = MOTER_HIGH - MOTER_LOW
RANGE = 100

def moter_to_high():
    print("Called moter_to_high()")
    for i in range(RANGE):
        pwm.set_pwm(0, 0, int(MOTOR_LOW + i * DIFF / RANGE))
        time.sleep(1/RANGE)
    
def moter_to_low():
    print("Called moter_to_low()")
    for i in range(RANGE):
        pwm.set_pwm(0, 0, int(MOTOR_HIGH - i * DIFF / RANGE))
        time.sleep(1/RANGE)

def handle_moter_process(req):
    print("Receive Message(moter isHigh==:", req.isHigh ")")
    print(type(req.isHigh))
       
def listener():
    rospy.init_node('moter_process', anonymous=True)
    s = rospy.Service('moter', SendMoterIsHigh, handle_moter_process)
    rospy.spin()    

if __name__ == '__main__':
    listener()
