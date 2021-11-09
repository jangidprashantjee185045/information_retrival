import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication , QLabel , QLineEdit , QTableWidget , QTableWidgetItem
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


'''
    ---display.py---
    this module shows the body of the app
    This renders the table of all the documets with their cosine Similarity score
'''

class Display(QWidget):

    def __init__(self, *args):
        super().__init__()


        self.layout = QVBoxLayout()

        #add default image to the body
        image_label = QLabel()
        default_image = QPixmap('./images/default.jpeg')
        image_label.setPixmap(default_image)
        self.layout.addWidget(image_label)

        self.setLayout(self.layout)


    # function => query()
    # param :
    #   1) scores : dictionary of all the documets with their respective score
    # this function is invoked when a query is searched by user
    def display_query(self,scores):

        # remove the previous element in the layout
        prev = self.layout.itemAt(0)
        self.layout.removeItem(prev)

        #print(scores)

        #create the table to store the scores
        table = QTableWidget()
        table.setRowCount(len(scores))
        table.setColumnCount(2)

        # add all the rows to the table
        i = 0
        for k,v in sorted(scores.items(), key=lambda item: item[1] ,reverse=True):
            table.setItem(i,0,QTableWidgetItem(k))
            table.setItem(i,1,QTableWidgetItem(str(round(v,8))))
            i+=1


        # set table header name and size
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setHorizontalHeaderLabels(['Document','Score'])


        # add table to layout
        self.layout.addWidget(table)
        self.layout.activate()

        # update the body
        self.update()
