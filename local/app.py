# -*- coding:utf-8 -*-
# 主界面
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from original import Ui_MainWindow
from gui.pagedata.TopicListWidget import TopicListWidget
from gui.pagedata.CollapseBoxWidget import CollapseBoxWidget
from gui.pagedata.TopicDetailWidget import TopicDetailWidget, TopicAttrWidget
from gui.pagedata.LineChartWidget import LineChartWidget
from gui.pagedata.BlockChartWidget import BlockChart, BlockChartWidget
from core.Topic import Attr
from gui.PageIndexWidget import PageIndexWidget

class RobotWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RobotWindow, self).__init__(parent)
        self.setupUi(self)

        self.showMaximized() # 最大化窗口
        self.setWindowIcon(QtGui.QIcon("/home/lutao/workspace/me/QtViz/resources/icon.png")) # icon
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 60px;}")

        # 首页
        self.tab1_layout = QtWidgets.QHBoxLayout(self.tab1)
        self.page_index_widget = PageIndexWidget()
        self.tab1_layout.addWidget(self.page_index_widget)
        

        # 布局指定父控件，然后在布局里面添加一个控件
        QtWidgets.QHBoxLayout(self.centralwidget).addWidget(self.tabWidget)

        # tab2-曲线
        self.tab2_layout = QtWidgets.QHBoxLayout(self.tab2)
        self.topoic_detail_widget = TopicDetailWidget([])

        box1 = CollapseBoxWidget("hal", ["/hal/sensor/imu", "/hal/sensor/odom", "test", "test", "test", "test", "test", "test"], lambda sub_title:self.f(sub_title))
        box2 = CollapseBoxWidget("preception", ["/hal/sensor/imu2", "/hal/sensor/odom2", "test", "test", "test", "test", "test", "test"], lambda sub_title:self.f(sub_title))
        box3 = CollapseBoxWidget("preception", ["/hal/sensor/imu2", "/hal/sensor/odom2", "test", "test", "test", "test", "test", "test"], lambda sub_title:self.f(sub_title))
        box4 = CollapseBoxWidget("preception", ["/hal/sensor/imu2", "/hal/sensor/odom2", "test", "test", "test", "test", "test", "test"], lambda sub_title:self.f(sub_title))
        self.topoic_list_widget = TopicListWidget([box1, box2, box3, box4])

        # 注意这里为什么要用self，如果不用self，就是局部对象，声明周期结束销毁，导致chart里面的timer失效
        self.chart1 = BlockChart("测试1", 10, 500)
        self.chart1.add(Attr("imu.roll", int, 0, "roll"))
        self.chart1.add(Attr("psd", int, 0, "psd"))
        block_chart_widget1 = BlockChartWidget(self.chart1)
        self.chart2 = BlockChart("测试2", 10, 200)
        self.chart2.add(Attr("tof", float, 0, "tof"))
        block_chart_widget2 = BlockChartWidget(self.chart2)
        self.chart3 = BlockChart("测试3", 10, 300)
        self.chart3.add(Attr("tof", float, 0, "tof"))
        block_chart_widget3 = BlockChartWidget(self.chart3)
        self.chart4 = BlockChart("测试4", 10, 500)
        self.chart4.add(Attr("tof", float, 0, "tof"))
        block_chart_widget4 = BlockChartWidget(self.chart4)
        self.chart5 = BlockChart("测试5", 10, 1000)
        self.chart5.add(Attr("tof", float, 0, "tof"))
        block_chart_widget5 = BlockChartWidget(self.chart5)
        self.line_chart_widget = LineChartWidget([block_chart_widget1, block_chart_widget2, block_chart_widget3, block_chart_widget4, block_chart_widget5])

        self.tab2_layout.addWidget(self.topoic_list_widget, 1)
        self.tab2_layout.addWidget(self.topoic_detail_widget, 1)
        self.tab2_layout.addWidget(self.line_chart_widget, 4)  
    
    def f(self, sub_title):
        attrs = [
            TopicAttrWidget(Attr("imu.roll", int, 0, "roll"), lambda attr:self.g(attr)),
            TopicAttrWidget(Attr("tof", float, 0, "tof"), lambda attr:self.g(attr)),
            TopicAttrWidget(Attr("tof", float, 0, "tof"), lambda attr:self.g(attr)),
            TopicAttrWidget(Attr("tof", float, 0, "tof"), lambda attr:self.g(attr)),
            TopicAttrWidget(Attr("tof", float, 0, "tof"), lambda attr:self.g(attr)),
        ]
        # self.topoic_detail_widget = TopicDetailWidget(attrs)
        self.tab2_layout.replaceWidget(self.topoic_detail_widget, TopicDetailWidget(attrs))

    def g(self, attr):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = RobotWindow()
    MainWindow.show()
    sys.exit(app.exec_())
