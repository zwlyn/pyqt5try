# -*- coding: utf_8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QLabel, QApplication)
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):

        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60,100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)


        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
    
    def onChanged(self, text):

        self.lbl.setText(text)
        #self.lbl.abjustSize()adjustSize  !!! d和b不分！！
        self.lbl.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

