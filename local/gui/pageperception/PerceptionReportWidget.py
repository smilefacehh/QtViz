# -*- coding:utf-8 -*-
# 感知报告组件

from unicodedata import category
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.common.BarChart import BarChart

class PerceptionReportWidget(QtWidgets.QWidget):
    """感知报告组件
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        category = ["打滑","抱起","边刷缠绕","滚刷缠绕"]
        data = [10, 2, 16, 7]
        result_bar_chart = BarChart("状态检测结果统计", category, data)
        layout.addWidget(result_bar_chart.chartview)