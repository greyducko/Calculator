from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial
import re


class MainWindow(QMainWindow):

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
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.display, 0, 0, 1, 4)

    def add_buttons(self):

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
        self.display.setText(expression)



class CalcController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_buttons()

    def connect_buttons(self):
        for key in self.view.buttons:
            button = self.view.buttons[key]
            button.clicked.connect(partial(self.button_pressed, key))

    def button_pressed(self, key):
        self.view.set_display(self.model.assign_key(key))

class CalcModel:
    def __init__(self):
        self.expression = ""
        self.first_num = None
        self.operator = None
        self.sec_num = None

    def assign_key(self, key):
        if key == "=":
            return self.compute()

        if key == "clear":
            self.expression = ""
            return ""

        if key == "backspace":
            if len(self.expression) > 0:
                self.expression = self.expression[:-1]
                return self.expression

        if self.is_valid_expression(key):
            self.expression += key
            print(self.expression)
            return self.expression
        else:
            return self.expression

    def is_valid_expression(self, key):

        expression = self.expression
        expression = expression + key
        valid_exp_1 = re.search(r"^-?$", expression)
        valid_exp_2 = re.search(r"^-?(0|([1-9][0-9]*))$", expression)
        valid_exp_3 = re.search(r"^-?(0|([1-9][0-9]*))\.?$", expression)
        valid_exp_4 = re.search(r"^-?(0|([1-9][0-9]*))\.[0-9]+$", expression)
        valid_exp_5 = re.search(r"^-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)[*\-+\u00F7]$", expression)
        valid_exp_6 = re.search(r"^-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)[*\-+\u00F7]-?$", expression)
        valid_exp_7 = re.search(r"^-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)[*\-+\u00F7]-?(0|([1-9][0-9]*))$", expression)
        valid_exp_8 = re.search(r"^-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)[*\-+\u00F7]-?(0|([1-9][0-9]*))\.?$",
                                expression)
        valid_exp_9 = re.search(r"^-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)[*\-+\u00F7]-?(0|([1-9][0-9]*))\.[0-9]+$",
                                expression)
        valid_exp_10 = re.search(
            r"^-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)[*\-+\u00F7]-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)$", expression)
        if (valid_exp_1 or valid_exp_2 or valid_exp_3 or valid_exp_4 or valid_exp_5 or valid_exp_6 or valid_exp_7 or
                valid_exp_8 or valid_exp_9 or valid_exp_10):
            return True

    def compute(self):
        expression = self.expression
        valid_exp = re.search(
            r"^-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)[*\-+\u00F7]-?(0|([1-9][0-9]*))((\.[0-9]+)|[1-9]*)$", expression)

        if valid_exp:
            first = expression[0]
            removed_first = expression[1:]

            if "+" in removed_first:
                floats = removed_first.split("+", 1)
                floats[0] = first + floats[0]
                return self.add(floats)
            elif "*" in removed_first:
                floats = removed_first.split("*", 1)
                floats[0] = first + floats[0]
                return self.multiply(floats)
            elif "\u00F7" in removed_first:
                floats = removed_first.split("\u00F7", 1)
                floats[0] = first + floats[0]
                return self.divide(floats)
            else:
                floats = removed_first.split("-", 1)
                floats[0] = first + floats[0]
                return self.subtract(floats)

        return self.expression

    def subtract(self, floats):
        result = float(floats[0])-float(floats[1])
        result = f"{result:g}"
        return result

    def add(self, floats):
        result = float(floats[0])+float(floats[1])
        result = f"{result:g}"
        return result

    def multiply(self, floats):
        result = float(floats[0])*float(floats[1])
        result = f"{result:g}"
        return result

    def divide(self, floats):
        second_num = floats[1]
        if second_num == "0" or second_num == "-0":
            return "Cannot divide by zero."
        result = float(floats[0])/float(floats[1])
        result = f"{result:g}"
        return result










def main():
    calculator = QApplication([])
    view = MainWindow()
    view.show()
    model = CalcModel()
    CalcController(model, view)
    calculator.exec_()

if __name__ == "__main__":
    main()


