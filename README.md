# AuE8230Spring22_Daniel_de_la_Calle
Dr. Krovi's Spring [Autonomy: Science and Systems] - CU-ICAR

This is Daniel de la Calle's Spring 2022 repository for the
class Autonomy Sicence and Systems. Each branch is deticated
to a particular task or assignment, with a self directed
emphasis for autonomous racing


Open loop square: 
To create an open loop controlled square path followed by the turtlebot in turtlesim environment, straightline movement and rotation of the turtle was considered The code allows to define some parameters and asks user for an input of desired distance to be followed by a robot with the angle of rotation after the desired distance is achieved Distance is calculated based on the time data and linear velocity available with us to give the robot a stop command to follow next step Similar to the distance, angular rotation is calculated based on angular velocity and the time As observed, To achieve a near perfect square path the linear velocity of the turtle should be low.


closed loop square:
Go to goal is used as a reference to create a closed loop controlller for turtlebot to follow a square path Proportional controller is implemented which consider the speed and distance based on the previous input velocity will be larger when the distance is more and vice versa Coordinates of the desired square are input in the function for turtle to follow the path Near perfect square was achieved by iterating the linear velocity and angular velocity input values to avoid the overshooting and spinningof the turtlebot.


circle: 
Following a circular path by a turtlebot in turtlesim is based on the parameters defined for the linear and angular velocities. Code is written by initiating a node and publishing respective velocity. the Twist() function is used to access the linear and angular velocities in x,y and z direction. For a turtle to follow a perfect circular path of radius 1 the angular velocity and linear velocity needs to be equal based on v=r*omega formula Thus a single input variable for angular and linear velocity works to generate a circular path of radius of 1 rate.sleep() command is used further to keep running the turtle in infinite loop.
