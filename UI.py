from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QLabel, QTextBrowser
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from Classification import Classifier
from YOLOv4 import YOLOLocaliser

from TextandLinks import pestcontrolURL
from TextandLinks import handling_method


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI.ui", self)
        self.Browse.clicked.connect(self.browse_file)
        self.Classify.clicked.connect(self.classify)
        self.img_path = ""

        self.label = QLabel(self)
        self.label.setStyleSheet("border: 2px solid grey;")
        self.label.move(10, 60)
        self.label.setFixedWidth(750)
        self.label.setFixedHeight(350)
        self.show()

        self.handling = QLabel(self)
        self.pestcontrol = QLabel(self)

        self.name = QLabel(self)
        self.name.adjustSize()
        self.name.move(5, 580)
        self.name.setFixedWidth(250)
        self.name.setFixedHeight(150)

        self.name.setText("Created by Nicholas Ho")
        self.name.setAlignment(Qt.AlignLeft)
        self.name.show()

    def browse_file(self):
        self.handling.setText("")
        self.label.clear()
        self.pestcontrol.clear()

        dir_open = './'
        target_image = QFileDialog.getOpenFileName(self, 'open file', dir_open, "Images (*.png *.jpeg *.jpg)")
        self.img_path = str(target_image[0])
        self.Img_path.setText(target_image[0])

    def classify(self):

        if self.img_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning!")
            msg.setText("You should input the image first!")
            msg.exec_()
            return True

        # Execute YOLO
        YOLOLocaliser(self.img_path)
        result = Classifier(self.img_path)
        YOLOResult_dir = './predictions.jpg'

        # Display YOLO's prediction
        pixmap = QPixmap(YOLOResult_dir)
        pixmap2 = pixmap.scaled(750, 350, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap2)
        self.label.adjustSize()

        # Print handling method
        self.handling.setText(handling_method[result[1]])
        self.handling.move(5, 420)
        self.handling.setFixedWidth(750)
        self.handling.setFixedHeight(150)
        self.handling.setStyleSheet("border: 1px solid darkgrey;")
        self.handling.setAlignment(Qt.AlignLeft)
        self.handling.show()

        self.pestcontrol.setOpenExternalLinks(True)
        self.pestcontrol.adjustSize()
        self.pestcontrol.move(500, 580)
        self.pestcontrol.setFixedWidth(250)
        self.pestcontrol.setFixedHeight(150)

        self.pestcontrol.setText(pestcontrolURL)
        self.pestcontrol.setAlignment(Qt.AlignRight)
        self.pestcontrol.show()

