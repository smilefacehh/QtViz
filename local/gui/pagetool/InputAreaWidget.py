# -*- coding:utf-8 -*-
# 输入框

from PyQt5 import QtCore, QtGui, QtWidgets


class InputAreaWidget(QtWidgets.QWidget):
    """输入框
    """

    def __init__(self, title, button_text, place_holder_text, click, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("InputAreaWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#InputAreaWidget{"
                "background-color: #EEEEEE;"
                "border: 1px solid #AAAAAA;"
            "}"
        )
        
        # 垂直布局
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        title_button_widget = QtWidgets.QWidget(self)
        title_button_widget_layout = QtWidgets.QHBoxLayout(title_button_widget)
        title_button_widget.setLayout(title_button_widget_layout)

        text_area_widget = QtWidgets.QPlainTextEdit(self)
        text_area_widget.setPlaceholderText(place_holder_text)

        title = QtWidgets.QLabel(title)
        title_button_widget_layout.addWidget(title, 3)
        button = QtWidgets.QPushButton(button_text)
        button.clicked.connect(lambda text=text_area_widget.getPaintContext():click(text=text))
        title_button_widget_layout.addWidget(button, 1)

        
        layout.addWidget(title_button_widget, 1)
        layout.addWidget(text_area_widget, 5)