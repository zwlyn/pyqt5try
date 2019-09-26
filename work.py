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

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from log import logger

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
def load_json(fpath):
    with open(fpath,'r', encoding='utf-8') as f:
        dict_data = json.loads(f.read())
    return dict_data

class TPCEAutoRunnerUI(QDialog):

    def __init__(self):
        super(TPCEAutoRunnerUI, self).__init__()
        self.start_map = load_json('start.json')
        self.config_map = load_json('config.json')

        self.setGeometry(200,100,1280,780)
        self.setWindowTitle('TPCEAutoRunnerUI')
        

        self.leftlist = QListWidget()

        #调整初始大小
        self.leftlist.resize(60, 700)
        #设置调整宽和高
        self.leftlist.setFixedSize(60, 700)
        self.leftlist.insertItem(0,'设置')
        self.leftlist.insertItem(1,'绘图')
        self.leftlist.insertItem(2,'报告')
        self.leftlist.insertItem(3,'启动')

        #单机出发绑定的糟函数
        self.leftlist.itemClicked.connect(self.start_clicked)

        self.leftlist.setStyleSheet("QListWidget{color:rgb(0,0,0); background:rgb(255,255,255);border:0px solid gray;}"
                                  "QListWidget::Item{height:50px;border:0px solid gray;padding-left:0;}"
                                  "QListWidget::Item:hover{color:rgb(0,255,0);border:0px solid gray;}"
                                  #"QListWidget::Item:{color:rgb(0,0,0);border:0px solid gray;}"
                                  "QListWidget::Item:selected:active{background:rgb();color:rgb(0,0,0);border-width:0;}"
                                  )


        self.settingBox=QGroupBox()
        self.settingBox.resize(1220, 700)
        #设置调整宽和高
        self.settingBox.setFixedSize(1220, 700)
        self.configBox=QGroupBox('基础参数配置')
        self.plotBox=QGroupBox('测试图像')

        self.configBox_list = list()

        self.create_settingBox()
        self.create_configBox()
        self.create_plotBox()

        self.stack=QStackedWidget(self)

        self.stack.addWidget(self.settingBox)
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

    def start_clicked(self,item):
        if item.text() == '启动':
            logger.info('点击了启动item，开始启动 ～～')

        
    def create_settingBox(self):

        mainLayout = QHBoxLayout()

        mainTab = QTabWidget()
        startTab = QWidget()
        configTab = QWidget()


        #--------------startBox----------------
        startBox = QHBoxLayout()

        layoutL = QFormLayout()

        customer = QLineEdit()
        initialdays = QLineEdit()
        scalefactor = QLineEdit()
        uptime = QLineEdit()
        testtime = QLineEdit()
        dbip = QLineEdit()
        dbport = QLineEdit()
        dbusername = QLineEdit()
        dbpassword = QLineEdit()
        dbname = QLineEdit()
        dbtype = QLineEdit()

        customer.setText(str(self.start_map['customer']))
        initialdays.setText(str(self.start_map['initialdays']))
        scalefactor.setText(str(self.start_map['scalefactor']))
        uptime.setText(str(self.start_map['uptime']))
        testtime.setText(str(self.start_map['testtime']))

        dbip.setText(str(self.start_map['dbconfig']['ip']))
        dbport.setText(str(self.start_map['dbconfig']['port']))
        dbusername.setText(str(self.start_map['dbconfig']['username']))
        dbpassword.setText(str(self.start_map['dbconfig']['password']))
        dbname.setText(str(self.start_map['dbconfig']['dbname']))
        dbtype.setText(str(self.start_map['dbconfig']['dbtype']))

        layoutL.addRow(QLabel("用户数量:"), customer)
        layoutL.addRow(QLabel("初始天数:"), initialdays)
        layoutL.addRow(QLabel("比例因子:"), scalefactor)
        layoutL.addRow(QLabel("上升时长:"), uptime)
        layoutL.addRow(QLabel("测试时长:"), testtime)
        layoutL.addRow(QLabel("数据库配置:"))
        layoutL.addRow(QLabel("IP地址:"), dbip)
        layoutL.addRow(QLabel("端口号:"), dbport)
        layoutL.addRow(QLabel("用户名:"), dbusername)
        layoutL.addRow(QLabel("密码:"), dbpassword)
        layoutL.addRow(QLabel("数据库实例:"), dbname)
        layoutL.addRow(QLabel("数据库类别:"), dbtype)

        layoutR = QHBoxLayout()
        tab = QTabWidget()
        agent = {
        "ip": QLineEdit(),
        "port": QLineEdit(),
        "concurrency": QLineEdit(),
        "instance": QLineEdit(),
        "startid": QLineEdit(),
        "endid": QLineEdit(),
        "delay": QLineEdit()
        }

        tab1 = QWidget()
        agent_layout = QFormLayout()
        agent_layout.addRow(QLabel("TPCEAgent配置:"))
        agent_layout.addRow(QLabel("IP地址:"), agent['ip'])
        agent_layout.addRow(QLabel("端口号:"), agent['port'])
        agent_layout.addRow(QLabel("并发数:"), agent['concurrency'])
        agent_layout.addRow(QLabel("实例数:"), agent['instance'])
        agent_layout.addRow(QLabel("起始id:"), agent['startid'])
        agent_layout.addRow(QLabel("终止id:"), agent['endid'])
        agent_layout.addRow(QLabel("延迟:"), agent['delay'])
        tab1.setLayout(agent_layout)

        tab.addTab(tab1, 'Agent1')
        tab.setTabPosition(QTabWidget.West)
        layoutR.addWidget(tab)
               
        startBox.addLayout(layoutL)
        startBox.addLayout(layoutR)

        # 将startBox放入标签中
        startTab.setLayout(startBox)
        #------------configBox-------------
        configBox = QHBoxLayout()

        layoutLeft = QFormLayout()
        toolip = QLineEdit()
        toolport = QLineEdit()
        mapBedUrl = QLineEdit()
        dingdingTime = QLineEdit()
        resultTime = QLineEdit()
        errorTime = QLineEdit()
        reportLanguage = QLineEdit()

        toolip.setText(str(self.config_map['ip']))
        toolport.setText(str(self.config_map['port']))
        mapBedUrl.setText(str(self.config_map['mapBedUrl']))
        dingdingTime.setText(str(self.config_map['dingdingTime']))
        resultTime.setText(str(self.config_map['resultTime']))
        errorTime.setText(str(self.config_map['errorTime']))
        reportLanguage.setText(str(self.config_map['reportLanguage']))

        layoutLeft.addRow(QLabel("工具所在IP"), toolip)
        layoutLeft.addRow(QLabel("工具所在端口号"), toolport)
        layoutLeft.addRow(QLabel("图床地址"), mapBedUrl)
        layoutLeft.addRow(QLabel("钉钉消息间隔时间"), dingdingTime)
        layoutLeft.addRow(QLabel("获取结果间隔时间"), resultTime)
        layoutLeft.addRow(QLabel("测试异常兼容时间"), errorTime)
        layoutLeft.addRow(QLabel("报告语言"), reportLanguage)

        configBox.addLayout(layoutLeft)

        #将configBox放入标签中
        configTab.setLayout(configBox)

        mainTab.addTab(startTab, '启动参数')
        mainTab.addTab(configTab, '配置参数')
        mainLayout.addWidget(mainTab)

        self.settingBox.setLayout(mainLayout)



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
    


