# -*- coding:utf-8 -*-
# 机器人信息

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pageindex.ConnectInfoWidget import ConnectInfoWidget
from gui.pageindex.VersionInfoWidget import VersionInfoWidget
from gui.pageindex.ShowListWidget import ShowListWidget

class RobotInfoWidget(QtWidgets.QWidget):
    """机器人信息
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
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

        # 连接信息
        connect_info_widget = ConnectInfoWidget()
        scroll_layout.addWidget(connect_info_widget)

        # 版本信息
        version_widget = VersionInfoWidget()
        scroll_layout.addWidget(version_widget)

        # 标定文件参数
        calib_data = [
            "激光雷达: 0.2",
            "tof: 0.3",
            "psd: 0.2",
            "imu: 0.3",
            "cliff: 0.3"
        ]
        calib_widget = ShowListWidget("标定参数", calib_data)
        scroll_layout.addWidget(calib_widget)

        # 崩溃文件列表
        crash_data = [
            "[2022-04-17 12:02:23] perception.core",
            "[2022-04-17 14:02:23] mapserver.core"
        ]
        crash_widget = ShowListWidget("崩溃列表", crash_data)
        scroll_layout.addWidget(crash_widget)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)

    
    def f(self, e):
        pass