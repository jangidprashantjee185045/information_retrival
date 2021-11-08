import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication , QLabel , QLineEdit
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class SearchBox(QWidget):

    def __init__(self,button_click_handler):
        super().__init__()

        self.queryBox = QLineEdit()
        self.queryBox.setFont(QFont("Arial",15))
        self.submit = QPushButton('submit',self)
        self.submit.clicked.connect(button_click_handler)

        searchBox = QHBoxLayout()
        searchBox.addWidget(self.queryBox)
        searchBox.addWidget(self.submit)

        self.setLayout(searchBox)
