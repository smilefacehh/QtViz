# -*- coding:utf-8 -*-
# 工具

from PyQt5 import QtCore, QtGui, QtWidgets


class PageToolWidget(QtWidgets.QWidget):
    """工具
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 网格布局
        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)
        
        