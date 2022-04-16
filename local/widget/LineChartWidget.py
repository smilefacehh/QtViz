# -*- coding:utf-8 -*-
# 折线图

import random
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from core.Topic import Attr

class BlockChart(QtChart.QChart):
    """一个Block为一个折线图，包含多个字段，数据范围接近

    Attributes:

    """
    def __init__(self, title, x_range, delta):
        super().__init__()

        self.x = 0
        self.x_range = x_range
        self.series_list = list()

        self.chart = QtChart.QChart()
        self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        self.x_ax = QtChart.QValueAxis()
        self.x_ax.setRange(0, x_range)
        self.y_ax = QtChart.QValueAxis()
        self.y_ax.setRange(0, 10)
        self.chart.addAxis(self.x_ax, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.y_ax, QtCore.Qt.AlignLeft)
        self.chart.setTitle(title)

        self.chart_view = QtChart.QChartView(self.chart)
        self.chart_view.setMinimumHeight(400)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.setGeometry(0,0,100,100)
        self.chart_view.show()

        self.update(delta)

    def add(self, attr):
        """添加一个字段"""
        series = QtChart.QSplineSeries()
        series.setName(attr.label)
        self.chart.addSeries(series) # 这个一定要在下面两句的前面

        series.attachAxis(self.x_ax)
        series.attachAxis(self.y_ax)

        self.series_list.append(series)

    def delete(self, attr):
        """删除一个字段"""
        pass

    def update(self, delta):
        self.timer = QtCore.QTimer(self)
        self.timer.start(delta)
        self.timer.timeout.connect(lambda: self.update_data())

    def update_data(self):
        """每隔delta时间刷新一次，外部调用"""
        self.x += 1
        if self.x >= self.x_range:
            self.chart.axisX().setRange(self.x - self.x_range, self.x)
        
        for series in self.series_list:
            data = random.randint(0, 10)
            if series.count() > self.x_range:
                series.removePoints(0, series.count() - self.x_range)
            series.append(self.x, data)


class LineChartWidget(QtWidgets.QWidget):
    """整体折线图

    """
    def __init__(self, block_chart_list, color="#FFFFFF", parent=None):
        super().__init__(parent)
        
        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: {};".format(color))
        
        # 布局
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        # scroll
        scroll = QtWidgets.QScrollArea(self)
        layout.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scroll_content = QtWidgets.QWidget(scroll)
        scroll_layout = QtWidgets.QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)

        # 折叠控件列表
        for bc in block_chart_list:
            scroll_layout.addWidget(bc.chart_view)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
