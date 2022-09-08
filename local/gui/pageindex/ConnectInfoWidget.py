# -*- coding:utf-8 -*-
# 连接信息

from PyQt5 import QtCore, QtGui, QtWidgets

class PaintWidget(QtWidgets.QWidget):
    """图标
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setFixedWidth(30)
        

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QColor(0, 255, 0))
        painter.setPen(QtGui.QColor(0, 255, 0))
        painter.drawEllipse(0, 4, 18, 18)
        painter.end()


class ConnectInfoWidget(QtWidgets.QWidget):
    """连接信息
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        # 连接信息
        paint_widget = PaintWidget(self)
        layout.addWidget(paint_widget, 1)

        device_combs = QtWidgets.QComboBox(self)
        device_combs.addItems(["本机", "192.168.1.12", "192.168.1.35"])
        device_combs.setStyleSheet(
            "QComboBox"
            "{"
                "selection-background-color: silver;"
            "}"
        )
        device_combs.currentIndexChanged[str].connect(self.f) # 条目发生改变时传递内容
        device_combs.currentIndexChanged[int].connect(self.f) # 条目发生改变时传递索引

        layout.addWidget(device_combs, 2)

        ping_label = QtWidgets.QLabel("Ping: 12ms")
        ping_label.setContentsMargins(20, 0, 0, 0)
        layout.addWidget(ping_label, 5)

    
    def f(self, e):
        pass