# -×- encoding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QFormLayout, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
                            , QApplication, QComboBox, QCheckBox, QGridLayout, QGroupBox, QLineEdit
                            , QTextEdit, QSpinBox, QDialogButtonBox, QDialog, QMenuBar, QMenu)
from PyQt5.QtCore import Qt

class Dialog(QDialog):
    
    def __init__(self):
        super(Dialog,self).__init__()

        self.createHbox()
        self.createGridBox()
        self.createFormBox()
        self.createButtonBox()
        self.createMenu()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.MenuBar)
        mainLayout.addWidget(self.Hbox)
        mainLayout.addWidget(self.GridBox)
        mainLayout.addWidget(self.FormBox)
        mainLayout.addWidget(QTextEdit('This widget takes up all the remaining space in the top-level layout.'))
        mainLayout.addWidget(self.ButtonBox)


        self.setLayout(mainLayout)

        #self.setGeometry(300, 300, 500, 800)  # x, y, 宽, 高
        self.setWindowTitle('test')  
        self.show()

    def createMenu(self):
        self.MenuBar = QMenuBar()
        self.FileMenu = QMenu('&File')
        self.exitAction = self.FileMenu.addAction('&Exit')

        self.MenuBar.addMenu(self.FileMenu)

        self.exitAction.triggered.connect(self.accept)




    def createHbox(self):
        self.Hbox = QGroupBox('Horizontal layout')
        layout = QHBoxLayout()
        layout.setSpacing(5)
        for i in range(1,5):
            layout.addWidget(QPushButton('Button %d' % i))

        self.Hbox.setLayout(layout)

    def createGridBox(self):
        self.GridBox = QGroupBox('Grid Layout')
        layout = QGridLayout()
        for i in range(1,4):
            layout.addWidget(QLabel("line %d :" % i), i, 0)    # 行号， 列号
            layout.addWidget(QLineEdit(), i, 1 )

        layout.addWidget(QTextEdit('This widget takes up about two thirds of the grid layout.'),0,2,4,5)  

        self.GridBox.setLayout(layout)

    def createFormBox(self):
        self.FormBox = QGroupBox('Form layout')
        layout = QFormLayout()

        layout.addRow(QLabel('Line 1:  '), QLineEdit(''))
        layout.addRow(QLabel('Line2,long text: '), QComboBox())
        layout.addRow(QLabel('Line3:  '), QSpinBox())   # 旋转盒子

        self.FormBox.setLayout(layout)

    def createButtonBox(self):
        self.ButtonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Dialog()
    sys.exit(app.exec_())