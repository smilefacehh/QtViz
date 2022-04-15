# -*- coding:utf-8 -*-
# 主界面

import sys
from main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout
from PyQt5.QtGui import QIcon

class RobotWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RobotWindow, self).__init__(parent)
        self.setupUi(self)

        self.showMaximized() # 最大化窗口
        self.setWindowIcon(QIcon("/home/lutao/workspace/me/QtViz/resources/icon.png")) # icon

        # 添加布局，让子控件随父控件大小动态调整
        layout = QHBoxLayout()
        layout.addWidget(self.tabWidget)
        self.centralwidget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = RobotWindow()
    MainWindow.show()
    sys.exit(app.exec_())
