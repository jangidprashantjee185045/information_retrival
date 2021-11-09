import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication , QLabel , QLineEdit
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *



'''
    ---search_box.py---
    This module create the search box in the app
    This also handles the search events
'''

class SearchBox(QWidget):

    # constructor
    def __init__(self,button_click_handler):
        super().__init__()

        # create query box
        self.queryBox = QLineEdit()
        self.queryBox.setFont(QFont("Arial",15))

        # create submit button
        self.submit = QPushButton('submit',self)
        # add handler function to the button
        self.submit.clicked.connect(button_click_handler)

        # add query box and submit button to layout
        searchBox = QHBoxLayout()
        searchBox.addWidget(self.queryBox)
        searchBox.addWidget(self.submit)

        self.setLayout(searchBox)
