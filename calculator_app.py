# This Python file uses the following encoding: utf-8
import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

# Important:
# You need to run the following command to generate the calculator_form.py file
#     pyside6-uic calculator_form.ui -o calculator_form.py, or
#     pyside2-uic calculator_form.ui -o calculator_form.py

from calculator_form import Ui_Calculator_window

class MainWindow(QMainWindow, Ui_Calculator_window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Calculator_window()
        self.ui.setupUi(self)

        # input values
        self.current_number = ""  # For storing the current input number
        self.first_operand = None  # To store the first number
        self.operator = None  # To store the operation (e.g., '+', '-')
        self.pending_second_operand = False

        # numbers
        self.ui.num_one.clicked.connect(lambda: self.number_pressed('1'))
        self.ui.num_two.clicked.connect(lambda: self.number_pressed('2'))
        self.ui.num_three.clicked.connect(lambda: self.number_pressed('3'))
        self.ui.num_four.clicked.connect(lambda: self.number_pressed('4'))
        self.ui.num_five.clicked.connect(lambda: self.number_pressed('5'))
        self.ui.num_six.clicked.connect(lambda: self.number_pressed('6'))
        self.ui.num_seven.clicked.connect(lambda: self.number_pressed('7'))
        self.ui.num_eight.clicked.connect(lambda: self.number_pressed('8'))
        self.ui.num_nine.clicked.connect(lambda: self.number_pressed('9'))
        self.ui.num_zero.clicked.connect(lambda: self.number_pressed('0'))
        self.ui.op_decimal.clicked.connect(lambda: self.number_pressed('.'))

        # operators
        self.ui.op_plus.clicked.connect(lambda: self.operator_pressed('+'))
        self.ui.op_dash.clicked.connect(lambda: self.operator_pressed('-'))
        self.ui.op_asterisk.clicked.connect(lambda: self.operator_pressed('*'))
        self.ui.op_slash.clicked.connect(lambda: self.operator_pressed('/'))
        self.ui.op_back.clicked.connect(lambda: self.back_space_pressed())
        self.ui.op_clear.clicked.connect(lambda: self.reset_calculator())


        self.ui.op_equals.clicked.connect(self.calculate_result)

    def number_pressed(self, number):
        if self.pending_second_operand == True:
            self.current_number = number
            self.pending_second_operand = False
        else:
            self.current_number += number
        self.ui.lcdNumber.display(self.current_number)

    def back_space_pressed(self):
        self.current_number = self.current_number[:-1]
        self.ui.lcdNumber.display(self.current_number)

        if self.first_operand is not None and self.second_operand is None:
            self.first_operand = self.current_number
            self.ui.lcdNumber.display(self.first_operand)
        elif self.first_operand is not None and self.second_operand is not None:
            self.second_operand = self.current_number
            self.ui.lcdNumber.display(self.second_operand)


    def operator_pressed(self, operator):
        if self.operator is not None and not self.pending_second_operand:
            self.calculate_result()

        if self.first_operand is None:
            self.first_operand = float(self.current_number)

        self.operator = operator
        self.ui.lcdNumber.display(self.operator)
        self.pending_second_operand = True

    def calculate_result(self):
        if self.first_operand is not None and self.operator is not None:
            self.second_operand = float(self.current_number)


            if self.operator == "+":
                result = self.first_operand + self.second_operand
            elif self.operator == "-":
                result = self.first_operand - self.second_operand
            elif self.operator == "*":
                result = self.first_operand * self.second_operand
            elif self.operator == "/":
                if self.second_operand == 0:
                    self.ui.lcdNumber.display("Error")
                    self.reset_calculator()
                    return
                else:
                    result = self.first_operand / self.second_operand
            else:
                self.ui.lcdNumber.display("Error")
                self.reset_calculator()
                return


            self.ui.lcdNumber.display(result)

            self.first_operand = result if result != "Error" else None
            self.current_number = str(result)
            self.operator = None
            self.pending_second_operand = False
        else:
            self.ui.lcdNumber.display("Error")


    def reset_calculator(self):
        self.first_operand = None
        self.second_operand = None
        self.pending_second_operand = False
        self.current_number = ""
        self.ui.lcdNumber.display(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
