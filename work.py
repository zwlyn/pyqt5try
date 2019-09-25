#!/usr/bin/python3
# -*- coding-utf_8 -*-
import os
import sys
import json
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QStackedWidget, QListWidget, QWidget, QMainWindow, 
        QListWidgetItem)
from PyQt5.QtGui import QIcon
import PyQt5.QtGui as QtGui
from log import logger

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
class TPCEAutoRunnerUI(QDialog):

    def __init__(self):
        super(TPCEAutoRunnerUI, self).__init__()
        self.start_map = {
        "customer": 1000,
        "initialdays": 60,
        "scalefactor": 500,
        "uptime": 0,
        "testtime": 240,
        "dbconfig": {
            "ip": "192.168.3.79",
            "port":3307,
            "username": "root",
            "password": "123456",
            "dbname": "mysql",
            "dbtype": "mysql"
        },
        "agents": [
            {
                "ip": "192.168.3.79",
                "port": 4290,
                "concurrency": 5,
                "instance": 1,
                "startid": 1,
                "endid": 1000,
                "delay": 0
            }
            ]
         }

        self.config_map = {
            "ip": "192.168.3.79",
            "port": 8642,
            "mapBedUrl": "http://39.97.226.213:18800/upload",
            "dingdingUrl": [
                "https://oapi.dingtalk.com/robot/send?access_token=99c37364ccd38d5bbec915e20d335bc5aa6b8ef0acb753cf246dd629f75892e1"],
            "dingdingTime": 60,
            "resultTime": 10,
            "errorTime":600,
            "reportLanguage": "EN"
        }
        self.setGeometry(200,100,1000,1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.ico"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('TPCEAutoRunnerUI')
        

        self.leftlist=QListWidget()
        self.leftlist.insertItem(0,'开始参数配置')
        self.leftlist.insertItem(1,'基础参数配置')
        self.leftlist.insertItem(2,'测试图像')
        item1 = QListWidgetItem()
        item1.setSizeHint(QSize(200,50))
        self.leftlist.setItemWidget(item1)
        self.leftlist.setStyleSheet("QListWidget{color:rgb(173,175,178); background:rgb(25,27,31);border:0px solid gray;}"
                                  "QListWidget::Item{height:45px;border:0px solid gray;padding-left:15;}"
                                  "QListWidget::Item:hover{color:rgb(255,255,255);background:transparent;border:0px solid gray;}"
                                  "QListWidget::Item:selected{border-image:url(images/listwidget_h.png); color:rgb(255,255,255);border:0px solid gray;}"
                                  "QListWidget::Item:selected:active{background:#00FFFFFF;color:#FFFFFF;border-width:0;}"
                                  )


        self.startBox=QGroupBox('开始参数配置')
        self.configBox=QGroupBox('基础参数配置')
        self.plotBox=QGroupBox('测试图像')

        self.startBox_list = list()
        self.configBox_list = list()

        self.create_startBox()
        self.create_configBox()
        self.create_plotBox()

        self.stack=QStackedWidget(self)

        self.stack.addWidget(self.startBox)
        self.stack.addWidget(self.configBox)
        self.stack.addWidget(self.plotBox)


        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.leftlist)
        mainLayout.addWidget(self.stack)
        mainLayout.spacing()
        mainLayout.addStretch(100)            
        mainLayout.setSpacing(5)


        self.setLayout(mainLayout)

        self.leftlist.currentRowChanged.connect(self.display)

        self.show()    
        
    def create_startBox(self):
        layout = QFormLayout()
        for i in range(18):
            self.startBox_list.append(QLineEdit())

        self.startBox_list[0].setText('')
        self.startBox_list[1].setText('')
        self.startBox_list[2].setText('')
        self.startBox_list[3].setText('')
        self.startBox_list[4].setText('')
        self.startBox_list[5].setText('')
        self.startBox_list[6].setText('')
        self.startBox_list[7].setText('')
        self.startBox_list[8].setText('')
        self.startBox_list[9].setText('')
        self.startBox_list[10].setText('')
        self.startBox_list[11].setText('')
        self.startBox_list[12].setText('')
        self.startBox_list[13].setText('')
        self.startBox_list[14].setText('')
        self.startBox_list[15].setText('')
        self.startBox_list[16].setText('')
        self.startBox_list[17].setText('')

        layout.addRow(QLabel("customer:"), self.startBox_list[0])
        layout.addRow(QLabel("initialdays:"), self.startBox_list[1])
        layout.addRow(QLabel("scalefactor:"), self.startBox_list[2])
        layout.addRow(QLabel("uptime:"), self.startBox_list[3])
        layout.addRow(QLabel("testtime:"), self.startBox_list[4])
        layout.addRow(QLabel("dbconfig:"))
        layout.addRow(QLabel("ip:"), self.startBox_list[5])
        layout.addRow(QLabel("port:"), self.startBox_list[6])
        layout.addRow(QLabel("username:"), self.startBox_list[7])
        layout.addRow(QLabel("password:"), self.startBox_list[8])
        layout.addRow(QLabel("dbname:"), self.startBox_list[9])
        layout.addRow(QLabel("dbtype:"), self.startBox_list[10])
        layout.addRow(QLabel("agents:"))
        layout.addRow(QLabel("ip:"), self.startBox_list[11])
        layout.addRow(QLabel("port:"), self.startBox_list[12])
        layout.addRow(QLabel("concurrency:"), self.startBox_list[13])
        layout.addRow(QLabel("instance:"), self.startBox_list[14])
        layout.addRow(QLabel("startid:"), self.startBox_list[15])
        layout.addRow(QLabel("endid:"), self.startBox_list[16])
        layout.addRow(QLabel("delay:"), self.startBox_list[17])

        self.startBox.setLayout(layout)



    def create_configBox(self):
        layout = QFormLayout()
        for i in range(9):
            self.configBox_list.append(QLineEdit())

        self.configBox_list[0].setText('192.168.3.79')
        self.configBox_list[1].setText('8642')
        self.configBox_list[2].setText('http://39.97.226.213:18800/upload')
        self.configBox_list[3].setText('https://oapi.dingtalk.com/robot/send?access_token=99c37364ccd38d5bbec915e20d335bc5aa6b8ef0acb753cf246dd629f75892e1')
        self.configBox_list[4].setText('')
        self.configBox_list[5].setText('60')
        self.configBox_list[6].setText('10')
        self.configBox_list[7].setText('600')
        self.configBox_list[8].setText('EN')

        layout.addRow(QLabel("ip:"), self.configBox_list[0])
        layout.addRow(QLabel("port:"), self.configBox_list[1])
        layout.addRow(QLabel("mapBedUrl:"), self.configBox_list[2])
        layout.addRow(QLabel("dingdingUrl:"))
        layout.addRow(QLabel("dingdingUrl_1:"), self.configBox_list[3])
        layout.addRow(QLabel("dingdingUrl_2:"), self.configBox_list[4])
        layout.addRow(QLabel("dingdingTime"), self.configBox_list[5])
        layout.addRow(QLabel("resultTime:"), self.configBox_list[6])
        layout.addRow(QLabel("errorTime:"), self.configBox_list[7])
        layout.addRow(QLabel("reportLanguage:"), self.configBox_list[8])
        self.configBox.setLayout(layout)

    def create_plotBox(self):
        layout = QVBoxLayout()

        m = PlotCanvas(self)

        layout.addWidget(m)
        startButton = QPushButton('开始测试', self)
        startButton.clicked.connect(self.on_click)
        layout.addWidget(startButton)

        self.plotBox.setLayout(layout)

    def on_click(self):
        for index in range(len(self.startBox_list)):
            logger.info(self.startBox_list[index].text())
        for index in range(len(self.configBox_list)):
            logger.info(self.configBox_list[index].text())

    def display(self,i):
        #设置当前可见的选项卡的索引
        self.stack.setCurrentIndex(i)

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = list()
        for i in x:
            y.append(random.random()*100)

        self.axes.plot(x,y)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=TPCEAutoRunnerUI()
    sys.exit(app.exec_())


#读取start和config的通用处理
        # for key in self.start_map:
        #     value = self.start_map[key]
        #     logger.info(key)
        #     if type(value) == int or type(value) == str:
        #         layout.addRow(QLabel(key + ":"), QLineEdit())
        #     if type(value) == dict:

        #         layout.addRow(QLabel(key + ":"))
        #         for subkey in value:
        #             #subvalue = value[subkey]
        #             layout.addRow(QLabel(str(subkey) + ":"), QLineEdit())
        #     if type(value) == list:

        #         for item in value:
        #             if type(item) == dict:
        #                 for sublkey in item:
        #                     layout.addRow(QLabel(sublkey + ":"), QLineEdit())
        #             if type(item) ==str or type(item) == int:
        #                 layout.addRow(QLabel(key + ":"), QLineEdit())
    


