#!/usr/bin/env python3
"""
Script to move Turtlesim in a 2x2 square
- .2 linear, .2 rotational
"""
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def mo_sq():
    rospy.init_node('turtle_open', anonymous = True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    vel_msg = Twist()
    
    # Initialize speeds (.2) and distances (2)
    ang_sp = float(115*2*PI/360)
    angle = float(90*2*PI/360)
    edge_dis = float(2)
    ForwardCheck = float(1)
    Clockwisecheck = float(1)
    
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    i = 0
    for i in range(12):
        cur_dis = 0
        # Get current time
        now = rospy.Time.now().to_sec()
        vel_msg.linear.x = 0.2
        
        while  cur_dis < edge_dis:
            if (ForwardCheck): vel_msg.linear.x = abs(0.2)
            
            # Publish x velocity at .2
            pub.publish(vel_msg)
                      
            # Calculate distance 
            t1 = rospy.Time.now().to_sec()
            cur_dis = 0.2*(t1 - now)
            
        # Stop turtle from moving forward
        vel_msg.linear.x = 0
        pub.publish(vel_msg)
            
        # Turn the turtle 90 degrees
        vel_msg.angular.z = ang_sp
        t2 = rospy.Time.now().to_sec()
        cur_ang = 0
            
        # turn the turtle 90 degrees
        while (cur_ang < angle):
            pub.publish(vel_msg)
            t3 = rospy.Time.now().to_sec()
            cur_ang = ang_sp*(t3-t2)
            
        # Stop the robot from turning 
        vel_msg.angular.z = 0
        pub.publish(vel_msg)
        i += 1
                 
        

if __name__ == '__main__':
    try:
        mo_sq()
    except rospy.ROSInterruptException:
        pass
