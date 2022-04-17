# -*- coding:utf-8 -*-
# 话题列表

from PyQt5 import QtCore, QtGui, QtWidgets

class TopicListWidget(QtWidgets.QWidget):
    """话题列表

    包含折叠控件列表。

    Attributes:
        collapse_box_widget_list: 折叠控件列表
        color: 背景颜色
    """
    def __init__(self, collapse_box_widget_list, color="#EEEEEE", parent=None):
        super(TopicListWidget, self).__init__(parent)
        
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
        for cb in collapse_box_widget_list:
            scroll_layout.addWidget(cb)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
