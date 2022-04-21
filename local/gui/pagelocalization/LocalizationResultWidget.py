# -*- coding:utf-8 -*-
# 结果曲线

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.common.LineChart import LineChart

class LocalizationResultWidget(QtWidgets.QWidget):
    """结果曲线
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

        # 折线图
        total_cpu_mem = {
            "CPU": 68,
            "MEM": 70
        }
        self.total_cpu_mem_chart = LineChart("系统", total_cpu_mem, 20, 1000)
        scroll_layout.addWidget(self.total_cpu_mem_chart.chart_view)

        node_cpu = {
            "Perception": 4,
            "Planning": 4,
            "Mapping": 5,
            "Mapserver": 4,
            "Hal": 4,
        }
        self.node_cpu_chart = LineChart("CPU", node_cpu, 20, 1000) # 一定要加self，不然不会更新
        scroll_layout.addWidget(self.node_cpu_chart.chart_view)


        node_mem = {
            "Perception": 28,
            "Planning": 32,
            "Mapping": 23,
            "Mapserver": 28,
            "Hal": 29,
        }
        self.node_mem_chart = LineChart("MEM", node_mem, 20, 1000)
        scroll_layout.addWidget(self.node_mem_chart.chart_view)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)