import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from UI import MainWindow


def mainUI():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowTitle("Insect Classifier")
    widget.setFixedWidth(780)
    widget.setFixedHeight(600)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    mainUI()