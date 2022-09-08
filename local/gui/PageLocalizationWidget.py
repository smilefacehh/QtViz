# -*- coding:utf-8 -*-
# 定位

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pagelocalization.BaseInfoWidget import BaseInfoWidget
from gui.pagelocalization.LocalizationMapWidget import LocalizationMapWidget
from gui.pagelocalization.LocalizationResultWidget import LocalizationResultWidget


class PageLocalizationWidget(QtWidgets.QWidget):
    """定位控件
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        # 综合信息
        left_widget = QtWidgets.QWidget(self)
        left_widget_layout = QtWidgets.QVBoxLayout(left_widget)
        left_widget.setLayout(left_widget_layout)

        self.base_info_widget = BaseInfoWidget()
        left_widget_layout.addWidget(self.base_info_widget, 1)

        self.localization_map_widget = LocalizationMapWidget()
        left_widget_layout.addWidget(self.localization_map_widget, 1)

        layout.addWidget(left_widget, 1)

        self.localization_result_widget = LocalizationResultWidget()
        layout.addWidget(self.localization_result_widget, 1)
