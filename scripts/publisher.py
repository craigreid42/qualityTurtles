#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random
from turtles.msg import TurtleQuality


def magic_hat():
    pub = rospy.Publisher('quality_turtles', TurtleQuality, queue_size=10)
    rospy.init_node('magic_hat')
    rate = rospy.Rate(5)  # 5hz
    index = 0
    while not rospy.is_shutdown():
        quality = random.randint(1, 10)
        if quality >= 7:
            msg = TurtleQuality(index, quality)
            pub.publish(msg)
        rate.sleep()
        index = index + 1


if __name__ == '__main__':
    try:
        magic_hat()
    except rospy.ROSInterruptException:
        pass
