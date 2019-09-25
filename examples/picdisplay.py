# -*- coding: utf_8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("img/ball.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle("Red Rock")
        self.show()

        # self.setGeometry(300, 300, 350, 300)
        # self.setWindowTitle('Calendar')
        # self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

