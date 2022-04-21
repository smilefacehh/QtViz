# -*- coding:utf-8 -*-
# 地图

import random
from PyQt5 import QtCore, QtGui, QtWidgets
from core.OccupancyGrid import OccupancyGrid

class MapWidget(QtWidgets.QWidget):
    """地图
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("MapWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#MapWidget{"
                "background-color: #EEEEEE;"
                "border: 1px solid #AAAAAA;"
            "}"
        )
        
        # 垂直布局
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        self.setMinimumSize(280,280)
        self.map = None

    def updateMap(self, occupancy_map):
        """地图更新
        """
        print("update planning map")
        self.map = occupancy_map
        # print(self.map.width, self.map.height, self.map.resolution)
        self.update()


    def paintEvent(self, QPaintEvent):
        if self.map is not None:
            painter = QtGui.QPainter()
            painter.begin(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QColor(QtCore.Qt.transparent))

            for i in range(self.map.height):
                for j in range(self.map.width):
                    index = i * self.map.width + j
                    v = self.map.data[index]
                    if v == -1:
                        # 青色，未知
                        painter.setBrush(QtGui.QColor(102,139,139))
                    elif v == 0:
                        painter.setBrush(QtGui.QColor(220,220,220))
                    else:
                        c = int(v / 100 * 255)
                        painter.setBrush(QtGui.QColor(c,c,c))

                    painter.drawRect(i, j, 100, 100)