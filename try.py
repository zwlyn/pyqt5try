from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton,QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import sys



class Ui(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('阿威十八式')
        self.setGeometry(10, 10, 640, 400)

        m = PlotCanvas(self)
        m.move(0,0)

        button = QPushButton('按钮', self)
        self.show()


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
    print('start')
    app = QApplication(sys.argv)
    ex = Ui()
    sys.exit(app.exec_())
    print('over')


