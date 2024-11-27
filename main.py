from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import QPoint
from PyQt6 import QtCore, QtWidgets
from random import randint
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 485)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 400, 151, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать окружность"))


class YellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Программа Максима Алябьева')
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(0, self.width() // 4)
        qp.drawEllipse(QPoint(randint(0, self.width()), randint(0, self.height())), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = YellowCircle()
    form.show()
    sys.exit(app.exec())
