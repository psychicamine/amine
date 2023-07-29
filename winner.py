from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Winner's Determinant")
but = QPushButton('Generate')
text = QLabel('Click to find out the winner')
winner = QLabel('?')
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter )
line.addWidget(winner, alignment = Qt.AlignCenter )
line.addWidget(but, alignment = Qt.AlignCenter ) 
main_win.setLayout(line)
main_win.show()
app.exec_()


def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('winner:')
    
but.clicked.connect(show_winner)
main_win.show()
app.exec_()