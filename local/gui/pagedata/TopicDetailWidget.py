# -*- coding:utf-8 -*-
# 话题详细数据列表

from urllib.response import addbase
from PyQt5 import QtCore, QtGui, QtWidgets
from core.Topic import Topic, Attr

class TopicAttrWidget(QtWidgets.QWidget):
    """话题字段
    
    字段包含: 添加按钮、类型、名称，过长则换行展示

    Attributes:
        attr: Attr字段
        click: 按钮点击回调
        color: 背景颜色
    """
    def __init__(self, attr, click, color="#EEEEEE", parent=None):
        super(TopicAttrWidget, self).__init__(parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: {};".format(color))

        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0,1,0,1)
        self.setLayout(layout)

        # 添加控件
        add_btn = QtWidgets.QPushButton("+")
        add_btn.clicked.connect(lambda attr=attr:click(attr))
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

        label = QtWidgets.QLabel(str(attr.type_str))
        label.setStyleSheet("color: #444444;")
        layout.addWidget(label, 2)

        label = QtWidgets.QLabel(attr.path)
        layout.addWidget(label, 6)


class TopicDetailWidget(QtWidgets.QWidget):
    """话题详细数据列表

    字段列表。

    Attributes:
        attrs: Attr列表
    """
    def __init__(self, attrs, color="#EEEEEE", parent=None):
        super(TopicDetailWidget, self).__init__(parent)
        
        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: {};".format(color))
        
        # 垂直布局
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
        for attr in attrs:
            scroll_layout.addWidget(attr)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
