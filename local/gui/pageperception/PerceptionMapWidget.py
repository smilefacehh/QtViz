# -*- coding:utf-8 -*-
# 感知地图

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pageindex.MapWidget import MapWidget


class PerceptionMapWidget(QtWidgets.QWidget):
    """感知地图
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("PerceptionMapWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#PerceptionMapWidget{"
                "background-color: #EEEEEE;"
                "border: 1px solid #AAAAAA;"
            "}"
        )
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        self.map = MapWidget()
        layout.addWidget(self.map)