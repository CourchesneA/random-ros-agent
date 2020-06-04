#!/usr/bin/env python

import rospy

from duckietown_msgs.msg import Twist2DStamped


class random_agent(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        self.pub_car_cmd = rospy.Publisher("~car_cmd", Twist2DStamped, queue_size=1)

        rate = rospy.Rate(15)
        while not rospy.is_shutdown():
            send_car_command()
        
    def send_car_command(self):
        car_control_msg = Twist2DStamped()

        car_control_msg.v = 0.5
        car_control_msg.omega = 0.2

        self.logdebug("Sending car command: v: {} omega: {}".format(v, omega))
        self.pub_car_cmd.publish(car_control_msg)

if __name__ == "__main__":
    rospy.init_node("random_agent", anonymous=False, log_level=rospy.INFO)  # adapted to sonjas default file

    node = random_agent()
