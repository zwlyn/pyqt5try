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
        self.reportBox=QGroupBox()
        self.plotBox=QGroupBox('测试图像')

        self.configBox_list = list()

        self.create_settingBox()
        self.create_reportBox()
        self.create_plotBox()

        self.stack=QStackedWidget(self)

        self.stack.addWidget(self.settingBox)
        self.stack.addWidget(self.plotBox)
        self.stack.addWidget(self.reportBox)

        mainLayout =QVBoxLayout()

        menuBar = QMenuBar()
        menu = menuBar.addMenu('logo')

        mid = QWidget()
        midLayout = QHBoxLayout()
        midLayout.addWidget(self.leftlist)
        midLayout.addWidget(self.stack)
        midLayout.spacing()
        midLayout.addStretch(100)            
        midLayout.setSpacing(5)
        mid.setLayout(midLayout)

        statusBar = QStatusBar()
        statusBar.showMessage('Hello man!')

        mainLayout.addWidget(menuBar)
        mainLayout.addWidget(mid)
        mainLayout.addWidget(statusBar)


        self.setLayout(mainLayout)

        self.leftlist.currentRowChanged.connect(self.display)

        self.show()

    def start_clicked(self,item):
        if item.text() == '启动':
            logger.info('点击了启动item，开始启动 ～～')

        
    def create_settingBox(self):

        mainLayout = QVBoxLayout()

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
        agent = {
        "ip": QLineEdit(),
        "port": QLineEdit(),
        "concurrency": QLineEdit(),
        "instance": QLineEdit(),
        "startid": QLineEdit(),
        "endid": QLineEdit(),
        "delay": QLineEdit()
        }

        agentBox = QWidget()
        agent_layout = QFormLayout()
        agent_layout.addRow(QLabel("TPCEAgent配置:"))
        agent_layout.addRow(QLabel("IP地址:"), agent['ip'])
        agent_layout.addRow(QLabel("端口号:"), agent['port'])
        agent_layout.addRow(QLabel("并发数:"), agent['concurrency'])
        agent_layout.addRow(QLabel("实例数:"), agent['instance'])
        agent_layout.addRow(QLabel("起始id:"), agent['startid'])
        agent_layout.addRow(QLabel("终止id:"), agent['endid'])
        agent_layout.addRow(QLabel("延迟:"), agent['delay'])
        agentBox.setLayout(agent_layout)


        listAgent = QListWidget()
        listAgent.resize(300,120)
        listAgent.addItem('新建TPCEAgent')
        listAgent.addItem('Agent1')
        listAgent.itemClicked.connect(self.create_agent)


        layoutR.addWidget(listAgent)
        layoutR.addWidget(agentBox)
                     
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

    def create_agent(self, item):
        if item.text() == '新建TPCEAgent':
            btn = self.sender()   # 获取到被点击的按钮
            item.addItem('11')



    def create_reportBox(self):
        layout = QHBoxLayout()
        tab_list = QTabWidget()

        pixmap_mid = QPixmap("img/ball.png")
        midreport = QLabel()
        midreport.setPixmap(pixmap_mid)

        pixmap_best = QPixmap("img/background.png")
        bestreport = QLabel()
        bestreport.setPixmap(pixmap_best)


        tab_list.addTab(midreport, '中间报告') 
        tab_list.addTab(bestreport, '最佳报告')

        layout.addWidget(tab_list)
        self.reportBox.setLayout(layout)
        

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
    


