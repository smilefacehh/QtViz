# -*- coding:utf-8 -*-
# 感知

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pageperception.BaseInfoWidget import BaseInfoWidget
from gui.pageperception.PerceptionMapWidget import PerceptionMapWidget
from gui.pageperception.PerceptionResultWidget import PerceptionResultWidget
from gui.pageperception.PerceptionReportWidget import PerceptionReportWidget

class PagePerceptionWidget(QtWidgets.QWidget):
    """感知控件

        CPU、MEM、Crash
        感知地图
        感知结果曲线
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        # 综合信息
        left_widget = QtWidgets.QWidget(self)
        left_widget_layout = QtWidgets.QVBoxLayout(left_widget)
        left_widget.setLayout(left_widget_layout)

        self.base_info_widget = BaseInfoWidget()
        left_widget_layout.addWidget(self.base_info_widget, 1)

        self.perception_map_widget = PerceptionMapWidget()
        left_widget_layout.addWidget(self.perception_map_widget, 1)

        self.report_widget = PerceptionReportWidget()
        left_widget_layout.addWidget(self.report_widget, 1)

        layout.addWidget(left_widget, 1)

        self.perception_result_widget = PerceptionResultWidget()
        layout.addWidget(self.perception_result_widget, 1)
