# -*- coding:utf-8 -*-
# 折线

import random
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from core.Topic import Attr


class LineChart(QtChart.QChart):
    """折线
    """
    def __init__(self, title, data, x_range, delta, show_title=True):
        super().__init__()

        self.x = 0
        self.x_range = x_range

        self.series_dict = dict()

        self.chart = QtChart.QChart()
        self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        self.x_ax = QtChart.QValueAxis()
        self.x_ax.setRange(0, x_range)
        self.y_ax = QtChart.QValueAxis()
        self.y_ax.setRange(0, 100)
        self.chart.addAxis(self.x_ax, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.y_ax, QtCore.Qt.AlignLeft)

        if show_title:
            self.chart.setTitle(title)

        for name, val in data.items():
            series = QtChart.QSplineSeries()
            series.setName(name)
            self.chart.addSeries(series) # 这个一定要在下面两句的前面
            series.attachAxis(self.x_ax)
            series.attachAxis(self.y_ax)
            self.series_dict[name] = series

        self.chart_view = QtChart.QChartView(self.chart)
        self.chart_view.setMinimumHeight(300)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.setGeometry(0,0,100,100)
        self.chart_view.chart().setBackgroundBrush(QtGui.QBrush(QtGui.QColor("#EEEEEE")))
        # self.chart_view.setStyleSheet("border: 1px solid #AAAAAA;")
        self.chart_view.show()

        self.timer = QtCore.QTimer(self)
        self.timer.start(delta)
        self.timer.timeout.connect(lambda: self.update())


    def update(self):
        """定时刷新"""
        self.x += 1
        if self.x >= self.x_range:
            self.chart.axisX().setRange(self.x - self.x_range, self.x)
        
        for k,v in self.series_dict.items():
            data = random.randint(0, 100)
            if v.count() > self.x_range:
                v.removePoints(0, v.count() - self.x_range)
            v.append(self.x, data)
