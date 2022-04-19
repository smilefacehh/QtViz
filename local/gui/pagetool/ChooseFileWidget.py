# -*- coding:utf-8 -*-
# 文件选择框

from PyQt5 import QtCore, QtGui, QtWidgets


class ChooseFileWidget(QtWidgets.QWidget):
    """文件选择框
    """

    def __init__(self, title, parent=None):
        super().__init__(parent=parent)

        # 背景颜色
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("ChooseFileWidget") # 防止所有的子控件都受下面的style影响
        self.setStyleSheet(
            "QWidget#ChooseFileWidget{"
                "background-color: #EEEEEE;"
                "border: 1px solid #AAAAAA;"
            "}"
        )
        
        # 水平布局
        layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(layout)

        title_widget = QtWidgets.QLabel(title)
        layout.addWidget(title_widget, 1)

        self.text_box = QtWidgets.QTextEdit(self)
        self.text_box.setPlaceholderText("选择路径")
        self.text_box.mousePressEvent = self.open
        layout.addWidget(self.text_box, 1)

    def open(self, evt):
        if evt.button() == QtCore.Qt.LeftButton:
            fold_path = QtWidgets.QFileDialog.getExistingDirectory(self.text_box, caption="选择目录", directory="~")
            if fold_path:
                self.text_box.setText(fold_path)
