# -*- coding:utf-8 -*-
# 折叠控件

from PyQt5 import QtCore, QtGui, QtWidgets

class CollapseBoxWidget(QtWidgets.QWidget):
    """折叠控件

    标题左侧有三角箭头符号，标题可点击展开，展开后添加子标题列表，每个子标题可以点击并调用传入的click方法。

    Attributes:
        title: 标题
        sub_titles: 子标题列表
        sub_title_click: 子标题点击回调，参数为子标题
    """
    def __init__(self, title, sub_titles, sub_title_click, parent=None):
        """
        Args:
            title: 标题
            sub_title_presses: {子标题:点击事件}
        """
        super(CollapseBoxWidget, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(text=title, checkable=True, checked=False)
        self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.content_area)

        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self.content_area, b"maximumHeight"))

        content_layout = QtWidgets.QVBoxLayout()
        # 添加子标题列表，为每个按钮添加点击事件
        for i in range(len(sub_titles)):
            button = QtWidgets.QPushButton(sub_titles[i])
            button.setStyleSheet(
                "QPushButton"
                "{"
                    "padding: 2px 2px 2px 18px;"
                    "border: none;"
                    "text-align: left;"
                    "color: #444444;" 
                "}"
                "QPushButton:hover {"
                    "background-color: silver;"
                "}"
            )
            # 点击事件的写法，不这么写多个按钮会输出同样的结果
            button.clicked.connect(lambda sub_title=sub_titles[i]: sub_title_click(sub_title=sub_title))
            content_layout.addWidget(button)

        self.setContentLayout(content_layout)
        

    @QtCore.pyqtSlot()
    def on_pressed(self):
        """按钮点击事件"""
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(QtCore.Qt.DownArrow if not checked else QtCore.Qt.RightArrow)
        self.toggle_animation.setDirection(
            QtCore.QAbstractAnimation.Forward
            if not checked
            else QtCore.QAbstractAnimation.Backward
        )
        self.toggle_animation.start()

    
    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = (self.sizeHint().height() - self.content_area.maximumHeight())
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)