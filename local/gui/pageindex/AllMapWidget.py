# -*- coding:utf-8 -*-
# 性能展示

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.common.MapWidget import MapWidget
from core.Test import Test
import threading
import time
from core.OccupancyGrid import OccupancyGrid

class AllMapWidget(QtWidgets.QWidget):
    """地图展示
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        update_map_th = threading.Thread(target=self.updateMap)
        update_map_th.start()

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 垂直布局
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        # scroll
        scroll = QtWidgets.QScrollArea(self)
        layout.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scroll_content = QtWidgets.QWidget(scroll)
        scroll_layout = QtWidgets.QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)
        scroll_layout.setSpacing(10)

        self.planning_map = MapWidget()
        self.localization_map = MapWidget()
        self.perception_map = MapWidget()
        scroll_layout.addWidget(self.planning_map)
        scroll_layout.addWidget(self.localization_map)
        scroll_layout.addWidget(self.perception_map)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)


    def updateMap(self):
        test = Test()
        while True:
            if test.map is not None:
                occupancy_map = OccupancyGrid(test.map)
                self.planning_map.updateMap(occupancy_map)
                test.map = None
            time.sleep(1)