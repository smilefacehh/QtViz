# -*- coding:utf-8 -*-

import rospy
from nav_msgs.msg import OccupancyGrid
import threading

class Test:

    def __init__(self):
        self.map = None
        th = threading.Thread(target=self.ros_th)
        th.start()

    def ros_th(self):
        rospy.init_node("test", anonymous=False, disable_signals=True)
        rospy.Subscriber("lidar_map_3cm", OccupancyGrid, self.map_callback)
        rospy.spin()

    def map_callback(self, map):
        print("recv map")
        self.map = map
