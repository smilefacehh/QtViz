# -*- coding:utf-8 -*-
# 折线图

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

class LineChartWidget(QtWidgets.QWidget):
    """整体折线图

    """
    def __init__(self, block_chart_widgets, color="#FFFFFF", parent=None):
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
        for bc in block_chart_widgets:
            scroll_layout.addWidget(bc)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)