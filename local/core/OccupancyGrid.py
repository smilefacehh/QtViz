# -*- coding:utf-8 -*-
# 栅格地图

class OccupancyGrid:
    """栅格地图
    
    """

    def __init__(self, occupancy_grid_msg):
        self.resolution = occupancy_grid_msg.info.resolution
        self.width = occupancy_grid_msg.info.width
        self.height = occupancy_grid_msg.info.height
        self.data = occupancy_grid_msg.data