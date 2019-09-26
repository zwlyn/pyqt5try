import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QpixmapDemo(QWidget):
    def __init__(self,parent=None):
        super(QpixmapDemo, self).__init__(parent)
        self.setGeometry(300,300,800,800)
        self.setWindowTitle('QPixmap例子')
        self.setWindowIcon(QIcon('img/start1.png'))

        layout=QVBoxLayout()

        lab1=QLabel('1234')
        lab1.setPixmap(QPixmap('img/start1.png'))

        layout.addWidget(lab1)

        btn = QPushButton('厉害按钮')
        icon = QIcon('start2.png')
        btn.setIcon(icon)
        size = QSize(60, 60)
        btn.setIconSize(size)
        layout.addWidget(btn)


        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo =QpixmapDemo()
    demo.show()
    sys.exit(app.exec_())
