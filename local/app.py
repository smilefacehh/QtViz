# -*- coding:utf-8 -*-
# 主界面
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from original import Ui_MainWindow
from gui.PageIndexWidget import PageIndexWidget
from gui.PageDataWidget import PageDataWidget
from gui.PageToolWidget import PageToolWidget
from gui.PagePerceptionWidget import PagePerceptionWidget
from gui.PageLocalizationWidget import PageLocalizationWidget

class RobotWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RobotWindow, self).__init__(parent)
        self.setupUi(self)

        self.showMaximized() # 最大化窗口
        self.setWindowIcon(QtGui.QIcon("/home/lutao/workspace/me/QtViz/resources/icon.png")) # icon
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 60px;}")

        # 布局指定父控件，然后在布局里面添加一个控件
        QtWidgets.QHBoxLayout(self.centralwidget).addWidget(self.tabWidget)

        # tab1-首页
        self.tab1_layout = QtWidgets.QHBoxLayout(self.tab1)
        self.page_index_widget = PageIndexWidget()
        self.tab1_layout.addWidget(self.page_index_widget)

        # tab2-曲线
        self.tab2_layout = QtWidgets.QHBoxLayout(self.tab2)
        self.page_data_widget = PageDataWidget()
        self.tab2_layout.addWidget(self.page_data_widget)

        # tab3-工具
        self.tab3_layout = QtWidgets.QHBoxLayout(self.tab3)
        self.page_tool_widget = PageToolWidget()
        self.tab3_layout.addWidget(self.page_tool_widget)

        # tab4-感知
        self.tab4_layout = QtWidgets.QHBoxLayout(self.tab4)
        self.page_perception_widget = PagePerceptionWidget()
        self.tab4_layout.addWidget(self.page_perception_widget)
        
        # tab5-定位
        self.tab5_layout = QtWidgets.QHBoxLayout(self.tab5)
        self.page_localizition_widget = PageLocalizationWidget()
        self.tab5_layout.addWidget(self.page_localizition_widget)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = RobotWindow()
    MainWindow.show()
    sys.exit(app.exec_())
