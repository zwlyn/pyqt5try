#!/usr/bin/python3
# -*- coding-utf_8 -*-
import os
import re
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
                                     "QListWidget::Item{height:40px;border:0px solid gray;padding-left:0;color:rgb(0,0,0);}"
                                     "QListWidget::Item:hover{color:rgb(0,200,200);border:0px solid gray;}"
                                     "QListWidget::Item:{color:rgb(0,0,0);border:0px solid gray;}"
                                     "QListWidget::Item:selected:active{background:rgb();color:rgb(0,0,0);border-width:0;}"
                                     "QListWidget::Item[0]{color:rgb(255,0,0);border:0px solid gray;}"
                                    )


        self.settingBox=QGroupBox()
        self.settingBox.resize(1220, 700)
        #设置调整宽和高
        self.settingBox.setFixedSize(1220, 700)
        self.reportBox=QGroupBox()
        self.plotBox=QGroupBox('测试图像')

        self.configBox_list = list()

        self.init_settingBox()
        self.init_reportBox()
        self.init_plotBox()

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

        # 每5秒存储一次结果
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.save_date)

        self.timer.start(5000)

    def save_date(self):
        with open('start.json', 'w') as f:
            f.write(json.dumps(self.start_map, indent=4))

    # 关闭窗口时会执行累的close方法，并触发QCloseEvent信号，进而执行closeEvent(self,QCloseEvent)方法
    def closeEvent(self, event):
        # 退出前对内存中的改变进行存储
        with open('start.json', 'w') as f:
            f.write(json.dumps(self.start_map, indent=4))
        logger.info('改变已经保存')
        reply = QMessageBox.question(self, '本程序',
                                           "是否要退出程序？",
                                           QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def start_clicked(self,item):
        if item.text() == '启动':
            logger.info('点击了启动item，开始启动 ～～')
    
    def init_settingBox(self):

        mainLayout = QVBoxLayout()

        mainTab = QTabWidget()
        startTab = QWidget()
        configTab = QWidget()

        #--------------startBox----------------
        startBox = QHBoxLayout()

        layoutL = QFormLayout()

        self.startArgs = {
        'customer': QLineEdit(),
        'initialdays': QLineEdit(),
        'scalefactor': QLineEdit(),
        'uptime': QLineEdit(),
        'testtime': QLineEdit(),
        'dbconfig':{
            'ip': QLineEdit(),
            'dbname': QLineEdit(),
            'port': QLineEdit(),
            'username': QLineEdit(),
            'dbtype': QLineEdit(),
            'password': QLineEdit(),
            'instance': QLineEdit()
        }
        }

        self.startArgs['customer'].setText(str(self.start_map['customer']))
        self.startArgs['initialdays'].setText(str(self.start_map['initialdays']))
        self.startArgs['scalefactor'].setText(str(self.start_map['scalefactor']))
        self.startArgs['uptime'].setText(str(self.start_map['uptime']))
        self.startArgs['testtime'].setText(str(self.start_map['testtime']))

        self.startArgs['dbconfig']['ip'].setText(str(self.start_map['dbconfig']['ip']))
        self.startArgs['dbconfig']['port'].setText(str(self.start_map['dbconfig']['port']))
        self.startArgs['dbconfig']['username'].setText(str(self.start_map['dbconfig']['username']))
        self.startArgs['dbconfig']['password'].setText(str(self.start_map['dbconfig']['password']))
        self.startArgs['dbconfig']['dbname'].setText(str(self.start_map['dbconfig']['dbname']))
        self.startArgs['dbconfig']['dbtype'].setText(str(self.start_map['dbconfig']['dbtype']))


        layoutL.addRow(QLabel("用户数量:"), self.startArgs['customer'])
        layoutL.addRow(QLabel("初始天数:"), self.startArgs['initialdays'])
        layoutL.addRow(QLabel("比例因子:"), self.startArgs['scalefactor'])
        layoutL.addRow(QLabel("上升时长:"), self.startArgs['uptime'])
        layoutL.addRow(QLabel("测试时长:"), self.startArgs['testtime'])
        layoutL.addRow(QLabel("数据库配置:"))
        layoutL.addRow(QLabel("IP地址:"), self.startArgs['dbconfig']['ip'])
        layoutL.addRow(QLabel("端口号:"), self.startArgs['dbconfig']['port'])
        layoutL.addRow(QLabel("用户名:"), self.startArgs['dbconfig']['username'])
        layoutL.addRow(QLabel("密码:"), self.startArgs['dbconfig']['password'])
        layoutL.addRow(QLabel("数据库实例名:"), self.startArgs['dbconfig']['dbname'])
        layoutL.addRow(QLabel("数据库类别:"), self.startArgs['dbconfig']['dbtype'])


        # 设置信号糟，当行内容修改结束时进行修改
        self.startArgs['customer'].textEdited.connect(self.modify_startArgs)     
        self.startArgs['initialdays'].textEdited.connect(self.modify_startArgs)  
        self.startArgs['scalefactor'].textEdited.connect(self.modify_startArgs)  
        self.startArgs['uptime'].textEdited.connect(self.modify_startArgs)  
        self.startArgs['testtime'].textEdited.connect(self.modify_startArgs)  

        self.startArgs['dbconfig']['ip'].textEdited.connect(self.modify_startArgs)
        self.startArgs['dbconfig']['port'].textEdited.connect(self.modify_startArgs)
        self.startArgs['dbconfig']['username'].textEdited.connect(self.modify_startArgs)
        self.startArgs['dbconfig']['password'].textEdited.connect(self.modify_startArgs)
        self.startArgs['dbconfig']['dbname'].textEdited.connect(self.modify_startArgs)
        self.startArgs['dbconfig']['dbtype'].textEdited.connect(self.modify_startArgs)

        layoutR = QHBoxLayout()
        self.agent = {
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
        agent_layout.addRow(QLabel("IP地址:"), self.agent['ip'])
        agent_layout.addRow(QLabel("端口号:"), self.agent['port'])
        agent_layout.addRow(QLabel("并发数:"), self.agent['concurrency'])
        agent_layout.addRow(QLabel("实例数:"), self.agent['instance'])
        agent_layout.addRow(QLabel("起始id:"), self.agent['startid'])
        agent_layout.addRow(QLabel("终止id:"), self.agent['endid'])
        agent_layout.addRow(QLabel("延迟:"), self.agent['delay'])
        agentBox.setLayout(agent_layout)


        self.listAgent = QListWidget()
        self.listAgent.resize(50, 300)
        self.listAgent.setStyleSheet("QListWidget{color:rgb(0,0,0); background:rgb(255,255,255);border:0px solid gray;}"
                                     "QListWidget::Item{height:40px;border:0px solid gray;padding-left:0;color:rgb(0,0,0);}"
                                     "QListWidget::Item:hover{color:rgb(0,200,200);border:0px solid gray;}"
                                     "QListWidget::Item:{color:rgb(0,0,0);border:0px solid gray;}"
                                     "QListWidget::Item:selected:active{background:rgb();color:rgb(0,0,0);border-width:0;}"
                                     "QListWidget::Item[0]{color:rgb(255,0,0);border:0px solid gray;}"
                                    )
        self.listAgent.addItem('新建TPCEAgent')
        #self.listAgent.setCurrentItem(self.listAgent.item(1))

        self.init_agent()

        self.listAgent.itemClicked.connect(self.add_agent)
        self.listAgent.itemClicked.connect(self.select_agent)
        
        layoutR.addWidget(self.listAgent)
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

        layoutRight = QHBoxLayout()

        self.listdingdingUrl = QListWidget()
        self.listdingdingUrl.addItem('新建钉钉地址')
        self.listdingdingUrl.addItem('钉钉地址 1')
        self.listdingdingUrl.itemClicked.connect(self.create_dingdingUrl) 

        layoutRight.addWidget(self.listdingdingUrl)

        dingdingUrlBox = QFormLayout()


        configBox.addLayout(layoutRight)

        #将configBox放入标签中
        configTab.setLayout(configBox)

        mainTab.addTab(startTab, '启动参数')
        mainTab.addTab(configTab, '配置参数')

        mainLayout.addWidget(mainTab)

        self.settingBox.setLayout(mainLayout)

    def modify_startArgs(self):
        logger.info('modify_startArgs!!')

        self.start_map['customer'] = self.startArgs['customer'].text()
        self.start_map['testtime'] = self.startArgs['testtime'].text()
        self.start_map['initialdays'] = self.startArgs['initialdays'].text()
        self.start_map['scalefactor'] = self.startArgs['scalefactor'].text()
        self.start_map['uptime'] = self.startArgs['uptime'].text()

        self.start_map['dbconfig']['ip'] = self.startArgs['dbconfig']['ip'].text()
        self.start_map['dbconfig']['port'] = self.startArgs['dbconfig']['port'].text()
        self.start_map['dbconfig']['dbname'] = self.startArgs['dbconfig']['dbname'].text()
        self.start_map['dbconfig']['username'] = self.startArgs['dbconfig']['username'].text()
        self.start_map['dbconfig']['dbtype'] = self.startArgs['dbconfig']['dbtype'].text()
        self.start_map['dbconfig']['password'] = self.startArgs['dbconfig']['password'].text()


    def init_agent(self):
        for agent in self.start_map['agents']:
            self.listAgent.addItem('Agent%d' % len(self.listAgent))

    def add_agent(self, item):
        if item.text() == '新建TPCEAgent':
            self.listAgent.addItem('Agent%d' % len(self.listAgent))
            new_agent = {
                "ip": "",
                "port": "",
                "concurrency": "",
                "instance": "",
                "startid": "",
                "endid": "",
                "delay": ""
            }
            self.start_map['agents'].append(new_agent)

    def select_agent(self, item):

        if not item.text() == '新建TPCEAgent':
            agentid = int(item.text()[-1:]) - 1 

            self.agent['ip'].setText(str(self.start_map['agents'][agentid]['ip']))
            self.agent['port'].setText(str(self.start_map['agents'][agentid]['port']))
            self.agent['concurrency'].setText(str(self.start_map['agents'][agentid]['concurrency']))
            self.agent['instance'].setText(str(self.start_map['agents'][agentid]['instance']))
            self.agent['startid'].setText(str(self.start_map['agents'][agentid]['startid']))
            self.agent['endid'].setText(str(self.start_map['agents'][agentid]['endid']))
            self.agent['delay'].setText(str(self.start_map['agents'][agentid]['delay']))

        # 当输入数据后，且切换行和退出时进行存储
        self.agent['ip'].textEdited.connect(self.modify_agent)
        self.agent['port'].textEdited.connect(self.modify_agent)
        self.agent['concurrency'].textEdited.connect(self.modify_agent)
        self.agent['instance'].textEdited.connect(self.modify_agent)
        self.agent['startid'].textEdited.connect(self.modify_agent)
        self.agent['endid'].textEdited.connect(self.modify_agent)
        self.agent['delay'].textEdited.connect(self.modify_agent)



    def modify_agent(self):
        logger.info(self.listAgent.currentItem().text())
        currentItem = self.listAgent.currentItem()
        if not currentItem.text() == '新建TPCEAgent':
            agentid = int(currentItem.text()[5:]) - 1 
        
            self.start_map['agents'][agentid]['ip'] = self.agent['ip'].text()
            self.start_map['agents'][agentid]['port'] = self.agent['port'].text()
            self.start_map['agents'][agentid]['concurrency'] = self.agent['concurrency'].text()
            self.start_map['agents'][agentid]['instance'] = self.agent['instance'].text()
            self.start_map['agents'][agentid]['startid'] = self.agent['startid'].text()
            self.start_map['agents'][agentid]['endid'] = self.agent['endid'].text()
            self.start_map['agents'][agentid]['delay'] = self.agent['delay'].text()




    def create_dingdingUrl(self, item):
        if item.text() == '新建钉钉地址':
            self.listdingdingUrl.addItem('钉钉地址 %d' % len(self.listdingdingUrl))

    def init_reportBox(self):
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
        

    def init_plotBox(self):
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
    


