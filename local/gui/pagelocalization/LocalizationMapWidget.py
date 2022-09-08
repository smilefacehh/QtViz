# -*- coding:utf-8 -*-
# 定位地图

from PyQt5 import QtCore, QtGui, QtWidgets


class LocalizationMapWidget(QtWidgets.QWidget):
    """定位地图
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("LocalizationMapWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#LocalizationMapWidget{"
                "background-color: #EEEEEE;"
                # "border: 1px solid #AAAAAA;"
            "}"
        )
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        self.label = QtWidgets.QLabel("定位地图")
        layout.addWidget(self.label)