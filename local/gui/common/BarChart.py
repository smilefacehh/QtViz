# -*- coding:utf-8 -*-
# 柱状图

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart


class BarChart(QtChart.QChart):
    """柱状图
    """
    def __init__(self, title, category, data):
        super().__init__()

        self.setTitle(title)
        self.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        # self.setTheme(QtChart.QChart.ChartThemeDark)

        series = QtChart.QBarSeries()
        barset = QtChart.QBarSet("")
        for d in data:
            barset << d
        series.append(barset)

        self.addSeries(series)

        axis = QtChart.QBarCategoryAxis()
        axis.append(category)
        
        self.createDefaultAxes()
        self.setAxisX(axis, series)

        self.chartview = QtChart.QChartView(self)