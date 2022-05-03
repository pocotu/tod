import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Hello World")
        self.setCentralWidget(self.label)
    
    def mouseMoveEvent(self, e):
        self.label.setText('mouse move evento')

    def mousePressEvent(self, e):
        self.label.setText('mouse press evento')

    def mouseReleaseEvent(self, e):
        self.label.setText('mouse release evento')

    def mouseDoubleClickEvent(self, e):
        self.label.setText('mouse double click evento')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()