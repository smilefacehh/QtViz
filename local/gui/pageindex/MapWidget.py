# -*- coding:utf-8 -*-
# 地图

from PyQt5 import QtCore, QtGui, QtWidgets

class MapWidget(QtWidgets.QWidget):
    """地图
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 垂直布局
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)