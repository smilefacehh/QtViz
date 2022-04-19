# -*- coding:utf-8 -*-
# 工具

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pagetool.InputAreaWidget import  InputAreaWidget
from gui.pagetool.ChooseFileWidget import ChooseFileWidget

class PageToolWidget(QtWidgets.QWidget):
    """工具

        指定保存路径
        指定路径pull文件
        指定路径push文件
        指定topic录制bag
        控制机器人运动（可浮动）
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        widget1 = QtWidgets.QWidget(self)
        widget1_layout = QtWidgets.QVBoxLayout(widget1)
        widget1.setLayout(widget1_layout)

        widget2 = QtWidgets.QWidget(self)
        widget2_layout = QtWidgets.QVBoxLayout(widget2)
        widget2.setLayout(widget2_layout)

        layout.addWidget(widget1, 1)
        layout.addWidget(widget2, 3)

        choose_file_widget = ChooseFileWidget("选择保存目录")
        choose_file_widget.setMaximumHeight(50)
        widget1_layout.addWidget(choose_file_widget, 1)
        
        record_bag_place_holder = "/hal/sensor/motor\n/hal/sensor/imu_with_odometry"
        record_bag_widget = InputAreaWidget("输入录制topic列表", "开始", record_bag_place_holder, self.f)
        widget1_layout.addWidget(record_bag_widget, 4)

        pull_file_place_holder = "/userdata/logs/\n/oem/DISK/bin/pita/perception/conf/"
        pull_file_widget = InputAreaWidget("输入机器人上拉取的文件路径", "开始", pull_file_place_holder, self.f)
        widget1_layout.addWidget(pull_file_widget, 4)

        pull_log_place_holder = "perception\n14~15"
        pull_log_widget = InputAreaWidget("拉取指定节点、指定时间段的日志", "开始", pull_log_place_holder, self.f)
        widget1_layout.addWidget(pull_log_widget, 4)

    def f(self, text):
        pass
        