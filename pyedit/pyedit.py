from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QLabel, QPushButton, QComboBox, QApplication,
    QTextEdit
)
from PyQt6.QtCore import Qt
import sys


class PyeditWin(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyEdit"
        self.setGeometry(100, 100, 800, 600)

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.draw_ui()

    def draw_ui(self):
        self.text_edit_area = QTextEdit()
        self.grid.addWidget(self.text_edit_area)


if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = PyeditWin()
    window.show()
    sys.exit(app.exec())
