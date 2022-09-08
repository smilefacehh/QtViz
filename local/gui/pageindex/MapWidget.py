# -*- coding:utf-8 -*-
# 地图

import random
from PyQt5 import QtCore, QtGui, QtWidgets


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

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        # 青色
        painter.setBrush(QtGui.QColor(102,139,139))
        painter.setPen(QtGui.QColor(QtCore.Qt.transparent))
        for i in range(500):
            x = random.randint(0, 50) * 10
            y = random.randint(0, 50) * 10
            painter.drawRect(x, y, 10, 10)
        
        # 灰色
        painter.setBrush(QtGui.QColor(220,220,220))
        # painter.setPen(QtGui.QColor(220,200,220))
        for i in range(300):
            x = random.randint(0, 50) * 10
            y = random.randint(0, 50) * 10
            painter.drawRect(x, y, 10, 10)

        # 黑色
        painter.setBrush(QtGui.QColor(255,255,255))
        # painter.setPen(QtGui.QColor(255,255,255))
        for i in range(100):
            x = random.randint(0, 50) * 10
            y = random.randint(0, 50) * 10
            painter.drawRect(x, y, 10, 10)
        painter.end()
