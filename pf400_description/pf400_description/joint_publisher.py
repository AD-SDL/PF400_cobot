#! /usr/bin/env python3

import rclpy                 # import Rospy
from rclpy.node import Node  # import Rospy Node
from std_msgs.msg import String
from std_srvs.srv import Empty

from time import sleep
import math

# from pf400_module_services.srv import pf400WhereJ 
# from wei_services.srv import WeiDescription 
# from wei_services.srv import WeiActions  

from sensor_msgs.msg import JointState
from std_msgs.msg import Header

# from pf400_driver.pf400_driver import PF400

# RATE = 20

class PF400JointPublisher(Node):
    '''
    The jointControlNode inputs data from the 'action' topic, providing a set of commands for the driver to execute. It then receives feedback, 
    based on the executed command and publishes the state of the peeler and a description of the peeler to the respective topics.
    '''
    def __init__(self, NODE_NAME = "pf400_joint_publisher"):
        '''
        The init function is neccesary for the peelerNode class to initialize all variables, parameters, and other functions.
        Inside the function the parameters exist, and calls to other functions and services are made so they can be executed in main.
        '''

        super().__init__(NODE_NAME)

        print("PF400 joint online") 

        self.state = "UNKNOWN"

        # self.pf400 = PF400("192.168.50.50", "10100")
        # self.pf400.initialize_robot()



        self.get_logger().info('What are my joint positions?')
        self.joint_publisher_function()

    def joint_publisher_function(self): 
        
        # self.pf400.force_initilize()
     
        # joint_states  = self.pf400.get_joint_states()
        joint_states = [0.01,-1.34,1.86,-3.03,0.05,0.91]
        # print(joint_states)
        # joint_states[0] *= 0.001  
        # joint_states[1] *= math.pi / 180  
        # joint_states[2] *= math.pi / 180  
        # joint_states[3] *= math.pi / 180  
        # joint_states[4] *= 0.0005  
        # joint_states[5] *= 0.01  
        joint_states[0] = 2.0
        joint_states[1] = 1.6  
        joint_states[2] = 5.0 
        joint_states[3] = 10.0
        joint_states[4] = 0.0  
        joint_states[5] = 0.7 

        self.get_logger().info("joint_states")

        # self.joint_state.header.stamp = rospy.Time.now()
        # self.joint_state.position = joint_states

        sensor_msgs.msg.JointState(header=std_msgs.msg.Header(stamp=builtin_interfaces.msg.Time(sec=1665690968, nanosec=762290846), frame_id=''), name=['J1', 'J2', 'J3', 'J4', 'J5', 'J6'], position=[0.01, -1.34, 1.86, -3.03, 0.05, 0.91], velocity=[], effort=[])
        # Create publisher object 
        pub_msg = JointState() # Make a new msg to publish results
        pub_msg.header = Header()
        # pub_msg.name = data.name
        # msg = JointState()
        # msg.header.stamp = self.get_clock().now()
        pub_msg.position = joint_states
        pub_msg.name = ["J1", "J2","J3","J4","J5","J6"]
        pub_msg.velocity = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        joint_publisher = self.create_publisher(JointState,'joint_states',10)
        # joint_publisher.position = joint_states
        rate = self.create_rate(10)

        # Publish the heartbeat
        while rclpy.ok():
            joint_publisher.publish(pub_msg)
            rate.sleep()



def main(args = None):

    NAME = "pf400_joint_publisher"
    rclpy.init(args=args)  # initialize Ros2 communication
    node = PF400JointPublisher(NODE_NAME=NAME)
    rclpy.spin(node)     # keep Ros2 communication open for action node
    rclpy.shutdown()     # kill Ros2 communication

if __name__ == '__main__':
    main()