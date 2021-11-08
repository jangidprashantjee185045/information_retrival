import sys
import os

from search_box import SearchBox
from add_document import load_files
from cosine_similarity import process_querry
from display import Display

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication , QLabel , QGridLayout
from PyQt5 import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.docs , self.doc_freq , self.term_frequencies = load_files()

        layout = QGridLayout()

        self.searchBox = SearchBox(self.search_query)

        layout.addWidget(self.searchBox,0,0)
        self.disp = Display()
        layout.addWidget(self.disp,1,0,5,0)

        self.setLayout(layout)

        self.setGeometry(300, 300, 700, 400)
        self.setWindowTitle('App')
        self.show()

    def search_query(self):
        text = self.searchBox.queryBox.text().strip()
        if text == '':
            print('Empty string')
        else:
            scores = process_querry(text,self.docs,self.doc_freq,self.term_frequencies)
            self.disp.display_query(scores)
            #print(rank,scores)


def main():
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
