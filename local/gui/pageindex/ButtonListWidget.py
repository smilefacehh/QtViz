# -*- coding:utf-8 -*-
# 按键列表

from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonListWidget(QtWidgets.QWidget):
    """按键列表
    """

    def __init__(self, title, button_list, click, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("ButtonListWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#ButtonListWidget{"
                "background-color: #EEEEEE;"
                "border: 1px solid #AAAAAA;"
            "}"
        )
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        title = QtWidgets.QLabel(title)
        title.setStyleSheet("font: bold;")
        layout.addWidget(title)
        
        # 栅格布局
        grid_widget = QtWidgets.QWidget(self)
        grid_layout = QtWidgets.QGridLayout()

        for i in range(len(button_list)):
            button = QtWidgets.QPushButton(button_list[i])
            button.setStyleSheet(
                "QPushButton"
                "{"
                    "background-color: #EEEEEE;"
                    "text-align: center;"
                    "color: #444444;" 
                "}"
                "QPushButton:hover {"
                    "background-color: silver;"
                "}"
            )
            # 点击事件的写法，不这么写多个按钮会输出同样的结果
            button.clicked.connect(lambda button_name=button_list[i]:click(button_name=button_name))
            grid_layout.addWidget(button, int(i/3), int(i%3))
        
        grid_widget.setLayout(grid_layout)
        layout.addWidget(grid_widget)