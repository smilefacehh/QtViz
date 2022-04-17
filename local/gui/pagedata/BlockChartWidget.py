# -*- coding:utf-8 -*-
# 单个block折线图

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
        self.title = title
        self.x_range = x_range
        self.series_dict = dict()

        self.chart = QtChart.QChart()
        self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        self.x_ax = QtChart.QValueAxis()
        self.x_ax.setRange(0, x_range)
        self.y_ax = QtChart.QValueAxis()
        self.y_ax.setRange(0, 10)
        self.chart.addAxis(self.x_ax, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.y_ax, QtCore.Qt.AlignLeft)
        # self.chart.setTitle(title)

        self.chart_view = QtChart.QChartView(self.chart)
        self.chart_view.setMinimumHeight(400)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.setGeometry(0,0,100,100)
        # self.chart_view.chart().setBackgroundBrush(QtGui.QBrush(QtGui.QColor("#EEEEEE")))
        # self.chart_view.setStyleSheet("border: 1px solid #AAAAAA;")
        self.chart_view.show()

        self.timer = QtCore.QTimer(self)
        self.timer.start(delta)
        self.timer.timeout.connect(lambda: self.update())

    def add(self, attr):
        """添加一个字段"""
        series = QtChart.QSplineSeries()
        series.setName(attr.label)
        self.chart.addSeries(series) # 这个一定要在下面两句的前面

        series.attachAxis(self.x_ax)
        series.attachAxis(self.y_ax)

        self.series_dict[attr.path] = (attr, series)

    def delete(self, attr):
        """删除一个字段"""
        if attr.path in self.series_dict:
            self.chart.removeSeries(self.series_dict[attr.path][1])
            del self.series_dict[attr.path]

    def update(self):
        """定时刷新"""
        self.x += 1
        if self.x >= self.x_range:
            self.chart.axisX().setRange(self.x - self.x_range, self.x)
        
        for k,v in self.series_dict.items():
            data = random.randint(0, 10)
            if v[1].count() > self.x_range:
                v[1].removePoints(0, v[1].count() - self.x_range)
            v[1].append(self.x, data)



class BlockAttrWidget(QtWidgets.QWidget):
    """Block中的一个Attr
    """
    def __init__(self, attr, click, color="#FFFFFF", parent=None):
        super().__init__(parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        # self.setStyleSheet("background-color: {};".format(color))

        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,1,0,1)
        self.setLayout(layout)

        # 添加控件
        add_btn = QtWidgets.QPushButton("-")
        add_btn.clicked.connect(lambda: click(attr))
        add_btn.setStyleSheet(
            "QPushButton"
            "{"
                "border: none;"
                "background-color: #DDDDDD;"
                "color: #444444;" 
            "}"
            "QPushButton:hover {"
                "background-color: silver;"
            "}"
        )
        layout.addWidget(add_btn, 1)

        label = QtWidgets.QLabel(attr.label)
        layout.addWidget(label, 3)


class BlockChartWidget(QtWidgets.QWidget):
    """Block折线图控件

    Attributes:

    """
    def __init__(self, block_chart, parent=None):
        super().__init__(parent)

        self.clicked = False
        self.block_chart = block_chart
        self.block_attr_widget_dict = dict()

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "QWidget {"
                "background-color: #EEEEEE;"
            "}"
            "QWidget:hover {"
                "background-color: silver;"
            "}"
        )
        
        # 布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        # 添加子控件
        tool_box = QtWidgets.QWidget(self)
        self.tool_box_layout = QtWidgets.QVBoxLayout(tool_box)

        title = QtWidgets.QLabel(block_chart.title)
        title.setContentsMargins(0, 0, 0, 10)
        self.tool_box_layout.addWidget(title)

        for k,v in block_chart.series_dict.items():
            block_attr_widget = BlockAttrWidget(v[0], self.attr_click)
            self.tool_box_layout.addWidget(block_attr_widget)
            self.block_attr_widget_dict[v[0]] = block_attr_widget
        
        self.tool_box_layout.addStretch()
        tool_box.setLayout(self.tool_box_layout)

        layout.addWidget(tool_box, 1)
        layout.addWidget(block_chart.chart_view, 10)


    def mousePressEvent(self, evt):
        if evt.button() == QtCore.Qt.LeftButton:
            if self.clicked:
                self.clicked = False
                self.setStyleSheet(
                    "QWidget {"
                        "background-color: #EEEEEE;"
                    "}"
                )
            else:
                self.clicked = True
                self.setStyleSheet(
                    "QWidget {"
                        "background-color: #C1CDC1;"
                    "}"
                )

    def attr_click(self, attr):
        self.block_chart.delete(attr)
        if attr in self.block_attr_widget_dict:
            self.tool_box_layout.removeWidget(self.block_attr_widget_dict[attr])
            del self.block_attr_widget_dict[attr]
