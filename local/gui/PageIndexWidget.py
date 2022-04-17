# -*- coding:utf-8 -*-
# 首页总览

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pageindex.RobotInfoWidget import RobotInfoWidget
from gui.pageindex.AllMapWidget import AllMapWidget
from gui.pageindex.ProfilerWidget import ProfilerWidget
from gui.pageindex.ControlWidget import ControlWidget


class PageIndexWidget(QtWidgets.QWidget):
    """首页widget

        局域网内可以adb connect上的机器人列表
        与机器人网络延迟（ping）
        CPU、MEM曲线
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        # 机器人信息
        self.robot_info_widget = RobotInfoWidget()
        layout.addWidget(self.robot_info_widget, 2)

        # 控制信息
        self.control_widget = ControlWidget()
        layout.addWidget(self.control_widget, 2)

        # 地图
        self.all_map_widget = AllMapWidget()
        layout.addWidget(self.all_map_widget, 3)

        # 性能
        self.profiler_widget = ProfilerWidget()
        layout.addWidget(self.profiler_widget, 3)