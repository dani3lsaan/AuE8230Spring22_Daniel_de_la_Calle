#!/usr/bin/env python3
"""
Move Turtlesim in a circle
"""
import rospy
from geometry_msgs.msg import Twist

def circle():

    # Initialize publisher to "speak" with Turtlesim
    rospy.init_node('turtle_circle', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
     
    # Twist message, with linear x and angular z values
    mo_cmd = Twist()
    mo_cmd.linear.x = 1.0
    mo_cmd.angular.z = 1.0

    # Initialize time for publish rate
    # for continuous circles
    now = rospy.Time.now()
    rate = rospy.Rate(10)

    # For 20 seconds, command turtle to move
    # at the directed cmd_vel instructions
    while rospy.Time.now() < now + rospy.Duration.from_sec(20):
        pub.publish(mo_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
