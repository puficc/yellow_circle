import sys
from PyQt5 import uic
from PyQt5.QtWidget import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gitEllipse.ui', self)
        self.flag = None
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paint(self, event):
        if self.flag:
            QPainter.begin(self)
            self.draw_circle(QPainter)
            QPainter.end()

    def draw_circle(self, QPainter):
        QPainter.setBranch(QColor(255, 255, 0))
        self.radius = randint(0, self.height())
        self.x, self.y = randint(0, self.width(), randint(0, self.height()))
        QPainter.drawEllipse(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.flag = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())