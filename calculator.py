from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        container = QWidget()
        self.setCentralWidget(container)
        container.setLayout(QGridLayout())
        self.add_display(container)
        self.keypad(container)


    def add_display(self, container):
        """Adds text display to the calculator"""

        display = QLineEdit()
        container.layout().addWidget(display, 0, 0, 1, 4)

    def keypad(self, container):
        """Adds keypad to the calculator """

        clear = QPushButton("Clear")
        backspace = QPushButton("Backspace")
        container.layout().addWidget(clear, 1, 0, 1, 2)
        container.layout().addWidget(backspace, 1, 2, 1, 2)
        keys = [["7","8", "9", u"\u00F7"],
                ["4", "5", "6", "*"],
                ["1", "2", "3", "-"],
                [ "0", ".", "+"]]

        for row in keys:
            for key in row:
                rowNum = keys.index(row)
                colNum = row.index(key)
                container.layout().addWidget(QPushButton(f"{key}"), rowNum+2, colNum)

        container.layout().addWidget(QPushButton("="), 6, 2, 1, 2)







if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

