# Author: Harvey Ng
# Description: Contains the "model" of the calculator application. Implements the logic behind the calculator
# operations. The calculator is only able to add, subtract, multiply, or divide two numbers. Regular expressions
# are used to determine if the expression is valid.

import re


class CalcModel:
    """Responsible for the logic behind the calculator and whether an expression is valid or not."""
    def __init__(self):
        self.expression = ""
        self.first_num = None
        self.operator = None
        self.sec_num = None

    def assign_key(self, key):
        """Determines the proper action to take depending on what key is pressed"""
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
        """Determine if the key press results in a valid expression"""

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
        """Solves the expression entered into the calculator"""
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