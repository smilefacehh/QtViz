# -*- coding:utf-8 -*-
# 版本信息

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pageindex.ShowListWidget import ShowListWidget

class VersionInfoWidget(QtWidgets.QWidget):
    """版本信息
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("VersionInfoWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#VersionInfoWidget{"
                "background-color: #EEEEEE;"
                "border: 1px solid #AAAAAA;"
            "}"
        )
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        # 机器人、基站版本信息
        robot_version_data = [
            "主控: 00.05.03.02",
            "驱动: 00.04.03.02",
            "蓝牙: 00.02.03.02"
        ]
        station_version_data = [
            "主控: 00.05.03.02",
            "驱动: 00.04.03.02",
            "蓝牙: 00.02.03.02",
        ]
        robot_version_widget = ShowListWidget("机器人", robot_version_data)
        station_version_widget = ShowListWidget("基站", station_version_data)

        layout.addWidget(robot_version_widget)
        layout.addWidget(station_version_widget)