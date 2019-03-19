#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time

def moter_client_message(x):
    rospy.wait_for_service('moter')
    moter = rospy.ServiceProxy('moter', SendMoterIsHigh)
    moter_is_high = moter(x)
    return moter_is_high

    
if __name__ == '__main__':
    print(moter_client_message(1))
