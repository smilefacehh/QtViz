# -*- coding:utf-8 -*-
# 列表展示
from PyQt5 import QtCore, QtGui, QtWidgets


class ShowListWidget(QtWidgets.QWidget):
    """列表展示控件
    """
    def __init__(self, title, data, parent=None):
        super().__init__(parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("ShowListWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#ShowListWidget{"
                "background-color: #EEEEEE;"
                "border: 1px solid #AAAAAA;"
            "}"
        )

        # 垂直布局
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        title = QtWidgets.QLabel(title)
        title.setStyleSheet("font: bold;")
        layout.addWidget(title)

        for d in data:
            label = QtWidgets.QLabel(d)
            label.setStyleSheet("color: #444444")
            layout.addWidget(label)
