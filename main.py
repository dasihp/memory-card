from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication([])

from card_window import *

card_win.setWindowTitle("Memory card")
card_win.resize(600, 500)
card_win.setLayout(card_layout)
card_win.show()

app.exec_()