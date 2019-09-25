#在屏幕中心显示窗口
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
def center(self):
    
    #获得窗口
    qr = self.frameGeometry()
    #获得屏幕中心点
    cp = QDesktopWidget().availableGeometry().center()
    #显示到屏幕中心
    qr.moveCenter(cp)
    self.move(qr.topLeft())

 #消息确认框
 from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
 def closeEvent(self, event):
    
    reply = QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QMessageBox.Yes | 
        QMessageBox.No, QMessageBox.No)

    if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()     

 #关闭窗口
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication 
def initUI(self):               
    
    qbtn = QPushButton('Quit', self)
    qbtn.clicked.connect(QCoreApplication.instance().quit)
    qbtn.resize(qbtn.sizeHint())
    qbtn.move(50, 50)       
    
    self.setGeometry(300, 300, 250, 150)
    self.setWindowTitle('Quit button')    
    self.show()

 #显示提示语
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont
def initUI(self):
    #这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
    QToolTip.setFont(QFont('SansSerif', 10))
    
    #创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
    self.setToolTip('This is a <b>QWidget</b> widget')
    
    #创建一个PushButton并为他设置一个tooltip
    btn = QPushButton('Button', self)
    btn.setToolTip('This is a <b>QPushButton</b> widget')
    
    #btn.sizeHint()显示默认尺寸
    btn.resize(btn.sizeHint())
    
    #移动窗口的位置
    btn.move(50, 50)       
    
    self.setGeometry(300, 300, 300, 200)
    self.setWindowTitle('Tooltips')    
    self.show()


#计算器
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



 #评论例子
 import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#状态栏
from PyQt5.QtWidgets import  QApplication,QMainWindow

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('statusBar')
        self.show()

#菜单栏
import sys
from PyQt5.QtWidgets import  QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('img/1.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


#按下ESC按键后使程序退出
def keyPressEvent(self, e):

    if e.key() == Qt.Key_Escape:
        self.close()