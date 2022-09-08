# -*- coding:utf-8 -*-
# 定位基础信息

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pageindex.ShowListWidget import ShowListWidget


class BaseInfoWidget(QtWidgets.QWidget):
    """基础信息控件
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        # scroll
        scroll = QtWidgets.QScrollArea(self)
        layout.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scroll_content = QtWidgets.QWidget(scroll)
        scroll_layout = QtWidgets.QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)

        # 综合信息
        localization_data = [
            "CPU: 5",
            "MEM: 27",
            "Crash:\n\t[2022-04-17 21:51:02] Mapserver.core\n\t[2022-04-17 11:51:02] Mapserver.core"
        ]
        self.show_list_widget = ShowListWidget("定位状态", localization_data)
        scroll_layout.addWidget(self.show_list_widget)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)