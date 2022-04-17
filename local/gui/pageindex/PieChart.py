# -*- coding:utf-8 -*-
# 饼图

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart


class PieChart(QtChart.QChart):
    """饼图
    """
    def __init__(self, title, data):
        super().__init__()

        series = QtChart.QPieSeries()
        for name, val in data.items():
            series.append(name, val)

        # 单独处理某个扇区
        slice = QtChart.QPieSlice()
        for i in range(len(data)):
            slice = series.slices()[i]
            slice.setLabelVisible(True)
            color = list(np.random.choice(range(256), size=3))
            slice.setBrush(QtGui.QColor(*color))

        # self.legend().hide()
        self.addSeries(series)
        self.createDefaultAxes()
        self.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        self.setTitle(title)
        self.legend().setVisible(True)
        self.legend().setAlignment(QtCore.Qt.AlignRight)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor("#EEEEEE")))

        self.chartview = QtChart.QChartView(self)
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chartview.setStyleSheet("border: 1px solid #AAAAAA;")

        