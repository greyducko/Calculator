# Author: Harvey Ng
# Description: Contains the main function to run the calculator.

from PyQt5.QtWidgets import *
from calc_controller import CalcController
from calc_view import CalcView
from calc_model import CalcModel


def main():
    """Initializes the model, view, and controller of the calculator. Runs the calculator application."""

    calculator = QApplication([])
    view = CalcView()
    view.show()
    model = CalcModel()
    CalcController(model, view)
    calculator.exec_()


if __name__ == "__main__":
    main()




