#! /usr/bin/env python3

import rclpy                 # import Rospy
from rclpy.node import Node  # import Rospy Node
from std_msgs.msg import String
from std_srvs.srv import Empty
from .TCSJointClient import TCSJointClient
from time import sleep

# from pf400_module_services.srv import pf400WhereJ 
from pf400_module_services.srv import MoveJ 


class jointControlNode(Node):
    '''
    The jointControlNode inputs data from the 'action' topic, providing a set of commands for the driver to execute. It then receives feedback, 
    based on the executed command and publishes the state of the peeler and a description of the peeler to the respective topics.
    '''
    def __init__(self, PORT="/dev/ttyUSB0" , NODE_NAME="PF400_Joint_Node"):
        '''
        The init function is neccesary for the peelerNode class to initialize all variables, parameters, and other functions.
        Inside the function the parameters exist, and calls to other functions and services are made so they can be executed in main.
        '''

        super().__init__(NODE_NAME)
        
        print("Wakey wakey eggs & bakey") 

        self.state = "UNKNOWN"

        self.client = TCSJointClient("192.168.50.50", "10100")

        # Enable high power if necessary
        is_hp = self.client.SendCommand("hp")
        if is_hp == "0 0":
            self.client.SendCommand("hp 1")
            sleep(5)

        # Attach the robot to this thread
        self.client.SendCommand("attach 1")

        # # Home if necessary
        is_homed = self.client.SendCommand("pd 2800")
        if is_homed == "0 0":
            self.client.SendCommand("home")


        self.client.SendCommand("attach 1")


        timer_period = 0.5  # seconds


        self.statePub = self.create_publisher(String, 'state', 10)

        self.stateTimer = self.create_timer(timer_period, self.stateCallback)

        self.descriptionSrv = self.create_service(Empty, "pf400_whereJ", self.whereJCallback)

        # self.actionSrv = self.create_service(PeelerActions, "peeler_actions", self.actionCallback)


    def stateCallback(self):

        '''
        Publishes the peeler state to the 'state' topic. 
        '''

        msg = String()

        msg.data = 'State: %s' % self.state

        self.statePub.publish(msg)

        self.get_logger().info('Publishing: "%s"' % msg.data)
        
        self.state = "READY"


    def whereJCallback(self, request, response):

        '''
        The descriptionCallback function is a service that can be called to showcase the available actions a robot
        can preform as well as deliver essential information required by the master node.
        '''

        self.get_logger().info('What are my joint positions?')

        var  = self.client.SendCommand("wherej")
        print(var)
        return response



def main(args = None):

    NAME = "PF400_Joint_Node"

    rclpy.init(args=args)  # initialize Ros2 communication

    node = jointControlNode(NODE_NAME=NAME)

    rclpy.spin(node)     # keep Ros2 communication open for action node

    rclpy.shutdown()     # kill Ros2 communication


if __name__ == '__main__':

    main()
