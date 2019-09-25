import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer
import random
import numpy as np


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = '这里可以修改标题'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)#实例化一个画布对象
        m.move(0, 0)

        button = QPushButton('这是一个按钮', self)
        button.setToolTip('This s an example button')
        button.move(500, 0)
        button.resize(140, 100)
        button.clicked.connect(m.plot)

        self.show()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.init_plot()
        self.plot()

    def plot(self):
        timer = QTimer(self)
        timer.start(100)

    def init_plot(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        self.axes.plot(x, y)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())