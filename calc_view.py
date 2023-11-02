# Author: Harvey Ng
# Description: Contains the "view" of the calculator application. The CalcView class is used to implement the
# calculator GUI.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CalcView(QMainWindow):
    """Represents the window of the calculator application."""
    def __init__(self):
        super().__init__()

        self.buttons = {}
        self.display = None
        self.setWindowTitle("Calculator")

        self.container = QWidget()
        self.setCentralWidget(self.container)
        self.layout = QGridLayout()
        self.container.setLayout(self.layout)

        self.add_display()
        self.add_buttons()

    def add_display(self):
        """Adds the display/viewport to the calculator GUI"""

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.display, 0, 0, 1, 4)

    def add_buttons(self):
        """Adds the buttons to the calculator GUI"""

        clear = QPushButton("Clear")
        backspace = QPushButton("Backspace")
        self.buttons["clear"] = clear
        self.buttons["backspace"] = backspace
        self.layout.addWidget(clear, 1, 0, 1, 2)
        self.layout.addWidget(backspace, 1, 2, 1, 2)
        keys = [["7", "8", "9", u"\u00F7"],
                ["4", "5", "6", "*"],
                ["1", "2", "3", "-"],
                ["0", ".", "=", "+"]]

        for row_num, row in enumerate(keys):
            for col_num, key in enumerate(row):
                self.buttons[key] = QPushButton(key)
                self.layout.addWidget(self.buttons[key], row_num+2, col_num)

    def set_display(self, expression):
        """Sets the text (numbers and operators) onto the calculator display"""

        self.display.setText(expression)

