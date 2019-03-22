import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685
import sys

NECK_VER = 0
NECK_HOR = 1
MOTOR_RESET_ANGLE = 350
MOTOR_MAX_ANGLE = 500
MOTOR_MIN_ANGLE = 200
class Motor:
    
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.reset_angle()
        self.motor_neck_ver = MOTOR_RESET_ANGLE
        self.motor_neck_hor = MOTOR_RESET_ANGLE
    
    def set_angle(self, motor_num, angle):
        self.pwn.set_pwm(motor_num, 0, angle)
    
    def reset_angle(self):
        for i in range(12):
            self.set_angle(i, MOTOR_RESET_ANGLE)
        print("Set up finished...")
    
    def neck_lookup(self, diff_x, diff_y):
        if self.motor_neck_ver <= MOTOR_ANGLE_MIN or self.motor_neck_ver >= MOTOR_ANGLE_MAX:
            pass
        if self.motor_neck_hor <= MOTOR_ANGLE_MIN or self.motor_neck_hor >= MOTOR_ANGLE_MAX:
            pass
        speed = 5
        if diff_x > 5:
            self.motor_neck_ver += speed
        elif diff_x < -5:
            self.motor_neck_ver -= speed
        if diff_y > 5:
            self.motor_neck_hor += speed
        elif diff_y < -5:
            self.motor_neck_hor -= speed
        
        self.set_angle(NECK_VER, self.motor_neck_ver)
        self.set_angle(NECK_HOR, self.motor_neck_hor)

        
