import sys
import os

from search_box import SearchBox
from add_document import load_files
from cosine_similarity import process_querry
from display import Display

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication , QLabel , QGridLayout
from PyQt5 import *




'''
    ---app.py---
    This is main module of the app and it runs the whole application.
'''

class App(QWidget):

    # constructor
    def __init__(self):
        super().__init__()

        # load the indexed files  (see add_document.py)
        self.docs , self.doc_freq , self.term_frequencies = load_files()

        # create layout for app
        layout = QGridLayout()
        # create search box  (search_box.py)
        self.searchBox = SearchBox(self.search_query)

        # add search box to app
        layout.addWidget(self.searchBox,0,0)


        # create display    (display.py)
        self.disp = Display()
        #add display
        layout.addWidget(self.disp,1,0,5,0)

        self.setLayout(layout)

        self.setGeometry(300, 300, 700, 400)
        self.setWindowTitle('Cosine Similarity')
        self.show()


    # function => search_query
    # event handler function to be invoked when a query is searched
    def search_query(self):

        # trim the query
        text = self.searchBox.queryBox.text().strip()

        # check if querry is Empty
        if text == '':
            print('Empty string')
        else:
            # calculating the cosine_similarity of documents to the qiven query
            scores = process_querry(text,self.docs,self.doc_freq,self.term_frequencies)

            # update the display
            self.disp.display_query(scores)
            #print(rank,scores)




# main function
# creating application
def main():
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
