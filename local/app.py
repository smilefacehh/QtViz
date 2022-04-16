# -*- coding:utf-8 -*-
# 主界面
import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from original import Ui_MainWindow
from widget.TopicListWidget import TopicListWidget
from widget.CollapseBoxWidget import CollapseBoxWidget
from widget.TopicDetailWidget import TopicDetailWidget, TopicAttrWidget
from widget.LineChartWidget import LineChartWidget, BlockChart
from core.Topic import Attr

class RobotWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RobotWindow, self).__init__(parent)
        self.setupUi(self)

        self.showMaximized() # 最大化窗口
        self.setWindowIcon(QtGui.QIcon("/home/lutao/workspace/me/QtViz/resources/icon.png")) # icon
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 60px;}")

        # 布局指定父控件，然后在布局里面添加一个控件
        QtWidgets.QHBoxLayout(self.centralwidget).addWidget(self.tabWidget)

        # tab2-曲线
        self.tab2_layout = QtWidgets.QHBoxLayout(self.tab2)
        self.topoic_detail_widget = TopicDetailWidget([])

        @QtCore.pyqtSlot()
        def g(attr):
            pass

        @QtCore.pyqtSlot()
        def f(sub_title):

            attrs = [
                TopicAttrWidget(Attr("imu.roll", int, 0, "roll"), g),
                TopicAttrWidget(Attr("tof", float, 0, "tof"), g),
                TopicAttrWidget(Attr("tof", float, 0, "tof"), g),
                TopicAttrWidget(Attr("tof", float, 0, "tof"), g),
                TopicAttrWidget(Attr("tof", float, 0, "tof"), g),
            ]
            # self.topoic_detail_widget = TopicDetailWidget(attrs)
            self.tab2_layout.replaceWidget(self.topoic_detail_widget, TopicDetailWidget(attrs))


        box1 = CollapseBoxWidget("hal", ["/hal/sensor/imu", "/hal/sensor/odom", "test", "test", "test", "test", "test", "test"], f)
        box2 = CollapseBoxWidget("preception", ["/hal/sensor/imu2", "/hal/sensor/odom2", "test", "test", "test", "test", "test", "test"], f)
        box3 = CollapseBoxWidget("preception", ["/hal/sensor/imu2", "/hal/sensor/odom2", "test", "test", "test", "test", "test", "test"], f)
        box4 = CollapseBoxWidget("preception", ["/hal/sensor/imu2", "/hal/sensor/odom2", "test", "test", "test", "test", "test", "test"], f)
        self.topoic_list_widget = TopicListWidget([box1, box2, box3, box4])

        chart1 = BlockChart("测试1", 10, 500)
        chart1.add(Attr("imu.roll", int, 0, "roll"))
        chart1.add(Attr("psd", int, 0, "psd"))
        chart2 = BlockChart("测试2", 10, 200)
        chart2.add(Attr("tof", float, 0, "tof"))
        chart3 = BlockChart("测试3", 10, 300)
        chart3.add(Attr("tof", float, 0, "tof"))
        chart4 = BlockChart("测试4", 10, 500)
        chart4.add(Attr("tof", float, 0, "tof"))
        chart5 = BlockChart("测试5", 10, 1000)
        chart5.add(Attr("tof", float, 0, "tof"))
        self.line_chart_widget = LineChartWidget([chart1, chart2, chart3, chart4, chart5])

        self.tab2_layout.addWidget(self.topoic_list_widget, 1)
        self.tab2_layout.addWidget(self.topoic_detail_widget, 1)
        self.tab2_layout.addWidget(self.line_chart_widget, 4)  
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = RobotWindow()
    MainWindow.show()
    sys.exit(app.exec_())
