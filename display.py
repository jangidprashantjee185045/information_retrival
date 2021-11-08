import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication , QLabel , QLineEdit , QTableWidget , QTableWidgetItem
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class Display(QWidget):

    def __init__(self, *args):
        super().__init__()

        self.layout = QVBoxLayout()

        image_label = QLabel()
        default_image = QPixmap('./images/default.jpeg')
        image_label.setPixmap(default_image)
        self.layout.addWidget(image_label)

        self.setLayout(self.layout)

    def display_query(self,scores):

        prev = self.layout.itemAt(0)
        self.layout.removeItem(prev)

        #print(scores)

        table = QTableWidget()
        table.setRowCount(len(scores))
        table.setColumnCount(2)

        #rendundent terms are not valid in this type of scheme of indexing

        i = 0
        for k,v in sorted(scores.items(), key=lambda item: item[1] ,reverse=True):
            table.setItem(i,0,QTableWidgetItem(k))
            table.setItem(i,1,QTableWidgetItem(str(round(v,8))))
            i+=1


        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        table.setHorizontalHeaderLabels(['Document','Score'])

        self.layout.addWidget(table)
        self.layout.activate()

        self.update()
