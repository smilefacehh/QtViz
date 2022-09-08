# -*- coding:utf-8 -*-
# 控制信息展示

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.pageindex.ButtonListWidget import ButtonListWidget
from gui.pageindex.ShowListWidget import ShowListWidget


class ControlWidget(QtWidgets.QWidget):
    """控制信息展示
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #EEEEEE;")
        
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

        # 任务状态
        task_state = "任务: 扫地暂停"
        task_state_label = QtWidgets.QLabel(task_state)
        scroll_layout.addWidget(task_state_label)

        # 按键列表
        button_list = [
            "扫地",
            "拖地",
            "扫拖同时",
            "出基站",
            "召回",
            "暂停",
            "恢复"
        ]
        button_list_widget = ButtonListWidget("功能列表", button_list, self.button_click)
        scroll_layout.addWidget(button_list_widget)

        # 定位状态
        localization_status_list = [
            "定位状态: 重定位",
            "定位置信度: 未知",
            "里程计状态: 不可信"
        ]
        localization_status_widget = ShowListWidget("定位状态", localization_status_list)
        scroll_layout.addWidget(localization_status_widget)

        # 感知状态
        perception_status_list = [
            "抱起: 1",
            "打滑: 0",
            "左边刷缠绕: 0",
            "右边刷缠绕: 1",
            "滚刷缠绕: 1",
            "左轮卡住: 1",
            "右轮卡住: 1",
            "风机堵: 0",
            "雷达罩异常: 0",
            "雷达异常: 0",
            "姿态异常: 0",
            "地毯: 0",
            "柔性: 0",
            "上盖: 0",
            "拖布状态: 0",
            "单位面积脏污: 0",
        ]
        perception_status_widget = ShowListWidget("感知状态", perception_status_list)
        scroll_layout.addWidget(perception_status_widget)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)

    
    def button_click(self, button_name):
        pass