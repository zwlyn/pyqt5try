# -×- encoding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QComboBox, QCheckBox, QGridLayout)
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        cb1 = QCheckBox('Show title', self)
        cb1.toggle()  # 初始的时候打上勾的
        cb1.stateChanged.connect(self.changeTitle)


        names = ['Cls', 'Bck', '1', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions  = [(i,j) for i in range(5) for j in range(4)]


        for position, name in zip(positions, names):

            cb = QCheckBox(name ,self)
            cb.toggle()
            grid.addWidget(cb, *position)



        cb2 = QCheckBox('CheckBox2', self)
        cb2.toggle()

        grid.addWidget(cb1, 1, 1)
        grid.addWidget(cb2, 10, 10)

        self.setLayout(grid)




        self.setGeometry(300, 300, 250, 150)  # x, y, 宽, 高
        self.setWindowTitle('Absolute')       # 绝对定位
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())