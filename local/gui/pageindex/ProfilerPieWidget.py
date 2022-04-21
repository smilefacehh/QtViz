# -*- coding:utf-8 -*-
# 性能展示，饼图

from colorsys import TWO_THIRD
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from gui.pageindex.ShowListWidget import ShowListWidget
from gui.common.PieChart import PieChart

class ProfilerPieWidget(QtWidgets.QWidget):
    """性能展示，饼图
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 垂直布局
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        # 列表
        prof_list_widget = QtWidgets.QWidget(self)
        prof_list_widget_layout = QtWidgets.QVBoxLayout(prof_list_widget)
        prof_list_widget.setLayout(prof_list_widget_layout)

        t_widget = QtWidgets.QWidget(prof_list_widget)
        t_widget_layout = QtWidgets.QHBoxLayout(t_widget)
        t_widget.setLayout(t_widget_layout)
        t_label = QtWidgets.QLabel("选择时长范围计算CPU&MEM均值:")
        t_widget_layout.addWidget(t_label, 4)

        t_combs = QtWidgets.QComboBox(self)
        t_combs.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        t_combs.setStyleSheet(
            "QComboBox"
            "{"
                "selection-background-color: silver;"
            "}"
        )
        t_combs.currentIndexChanged[str].connect(self.f) # 条目发生改变时传递内容
        t_combs.currentIndexChanged[int].connect(self.f) # 条目发生改变时传递索引
        t_widget_layout.addWidget(t_combs, 1)
        prof_list_widget_layout.addWidget(t_widget)

        prof_data = [
            "[System] CPU:E=12, M=20;  MEM:E=27, M=30",
            "[Perception] CPU:E=12, M=20;  MEM:E=12, M=20",
            "[Mapping] CPU:E=12, M=20;  MEM:E=12, M=20",
            "[Planning] CPU:E=12, M=20;  MEM:E=12, M=20",
            "[Mapserver] CPU:E=12, M=20;  MEM:E=12, M=20",
            "[Hal] CPU:E=12, M=20;  MEM:E=12, M=20",
        ]
        p_list_widget = ShowListWidget("CPU&MEM", prof_data)
        prof_list_widget_layout.addWidget(p_list_widget)

        # 饼图
        prof_pie_widget = QtWidgets.QWidget(self)
        prof_pie_widget_layout = QtWidgets.QVBoxLayout(prof_pie_widget)
        prof_pie_widget.setMinimumHeight(300)
        prof_pie_widget.setLayout(prof_pie_widget_layout)

        prof_pie_data = {
            "Perception": 4,
            "Mapserver": 6,
            "Application": 8,
            "Planning": 3,
            "Mapping": 4,
            "Hal": 5
        }
        prof_pie = PieChart("", prof_pie_data)
        prof_pie_widget_layout.addWidget(prof_pie.chartview)

        layout.addWidget(prof_list_widget)
        layout.addWidget(prof_pie_widget)

    def f(self, e):
        pass