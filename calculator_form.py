# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Calculator_window(object):
    def setupUi(self, Calculator_window):
        if not Calculator_window.objectName():
            Calculator_window.setObjectName(u"Calculator_window")
        Calculator_window.resize(700, 500)
        self.centralwidget = QWidget(Calculator_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.num_one = QPushButton(self.centralwidget)
        self.num_one.setObjectName(u"num_one")
        self.num_one.setGeometry(QRect(210, 350, 50, 50))
        self.num_one.setMaximumSize(QSize(51, 16777215))
        self.num_two = QPushButton(self.centralwidget)
        self.num_two.setObjectName(u"num_two")
        self.num_two.setGeometry(QRect(270, 350, 50, 50))
        self.num_three = QPushButton(self.centralwidget)
        self.num_three.setObjectName(u"num_three")
        self.num_three.setGeometry(QRect(330, 350, 50, 50))
        self.num_four = QPushButton(self.centralwidget)
        self.num_four.setObjectName(u"num_four")
        self.num_four.setGeometry(QRect(210, 290, 50, 50))
        self.num_four.setMaximumSize(QSize(51, 16777215))
        self.num_five = QPushButton(self.centralwidget)
        self.num_five.setObjectName(u"num_five")
        self.num_five.setGeometry(QRect(270, 290, 50, 50))
        self.num_five.setMaximumSize(QSize(51, 16777215))
        self.num_six = QPushButton(self.centralwidget)
        self.num_six.setObjectName(u"num_six")
        self.num_six.setGeometry(QRect(330, 290, 50, 50))
        self.num_six.setMaximumSize(QSize(51, 16777215))
        self.num_seven = QPushButton(self.centralwidget)
        self.num_seven.setObjectName(u"num_seven")
        self.num_seven.setGeometry(QRect(210, 230, 50, 50))
        self.num_seven.setMaximumSize(QSize(51, 16777215))
        self.num_eight = QPushButton(self.centralwidget)
        self.num_eight.setObjectName(u"num_eight")
        self.num_eight.setGeometry(QRect(270, 230, 50, 50))
        self.num_eight.setMaximumSize(QSize(51, 16777215))
        self.num_nine = QPushButton(self.centralwidget)
        self.num_nine.setObjectName(u"num_nine")
        self.num_nine.setGeometry(QRect(330, 230, 50, 50))
        self.num_nine.setMaximumSize(QSize(51, 16777215))
        self.num_zero = QPushButton(self.centralwidget)
        self.num_zero.setObjectName(u"num_zero")
        self.num_zero.setGeometry(QRect(390, 350, 50, 50))
        self.num_zero.setMaximumSize(QSize(51, 16777215))
        self.op_plus = QPushButton(self.centralwidget)
        self.op_plus.setObjectName(u"op_plus")
        self.op_plus.setGeometry(QRect(390, 290, 50, 50))
        self.op_plus.setMaximumSize(QSize(51, 16777215))
        self.op_slash = QPushButton(self.centralwidget)
        self.op_slash.setObjectName(u"op_slash")
        self.op_slash.setGeometry(QRect(450, 230, 50, 50))
        self.op_slash.setMaximumSize(QSize(51, 16777215))
        self.op_asterisk = QPushButton(self.centralwidget)
        self.op_asterisk.setObjectName(u"op_asterisk")
        self.op_asterisk.setGeometry(QRect(390, 230, 50, 50))
        self.op_asterisk.setMaximumSize(QSize(51, 16777215))
        self.op_equals = QPushButton(self.centralwidget)
        self.op_equals.setObjectName(u"op_equals")
        self.op_equals.setGeometry(QRect(450, 350, 50, 50))
        self.op_equals.setMaximumSize(QSize(51, 16777215))
        self.op_dash = QPushButton(self.centralwidget)
        self.op_dash.setObjectName(u"op_dash")
        self.op_dash.setGeometry(QRect(450, 290, 50, 50))
        self.op_dash.setMaximumSize(QSize(51, 16777215))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(210, 150, 291, 61))
        self.op_clear = QPushButton(self.centralwidget)
        self.op_clear.setObjectName(u"op_clear")
        self.op_clear.setGeometry(QRect(510, 230, 50, 50))
        self.op_clear.setMaximumSize(QSize(51, 16777215))
        self.op_back = QPushButton(self.centralwidget)
        self.op_back.setObjectName(u"op_back")
        self.op_back.setGeometry(QRect(510, 290, 50, 50))
        self.op_back.setMaximumSize(QSize(51, 16777215))
        self.op_decimal = QPushButton(self.centralwidget)
        self.op_decimal.setObjectName(u"op_decimal")
        self.op_decimal.setGeometry(QRect(510, 350, 50, 50))
        self.op_decimal.setMaximumSize(QSize(51, 16777215))
        self.pb_clickme = QPushButton(self.centralwidget)
        self.pb_clickme.setObjectName(u"pb_clickme")
        self.pb_clickme.setGeometry(QRect(510, 150, 50, 61))
        self.pb_clickme.setMaximumSize(QSize(51, 16777215))
        Calculator_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Calculator_window)
        self.statusbar.setObjectName(u"statusbar")
        Calculator_window.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator_window)

        QMetaObject.connectSlotsByName(Calculator_window)
    # setupUi

    def retranslateUi(self, Calculator_window):
        Calculator_window.setWindowTitle(QCoreApplication.translate("Calculator_window", u"MainWindow", None))
        self.num_one.setText(QCoreApplication.translate("Calculator_window", u"1", None))
        self.num_two.setText(QCoreApplication.translate("Calculator_window", u"2", None))
        self.num_three.setText(QCoreApplication.translate("Calculator_window", u"3", None))
        self.num_four.setText(QCoreApplication.translate("Calculator_window", u"4", None))
        self.num_five.setText(QCoreApplication.translate("Calculator_window", u"5", None))
        self.num_six.setText(QCoreApplication.translate("Calculator_window", u"6", None))
        self.num_seven.setText(QCoreApplication.translate("Calculator_window", u"7", None))
        self.num_eight.setText(QCoreApplication.translate("Calculator_window", u"8", None))
        self.num_nine.setText(QCoreApplication.translate("Calculator_window", u"9", None))
        self.num_zero.setText(QCoreApplication.translate("Calculator_window", u"0", None))
        self.op_plus.setText(QCoreApplication.translate("Calculator_window", u"+", None))
        self.op_slash.setText(QCoreApplication.translate("Calculator_window", u"/", None))
        self.op_asterisk.setText(QCoreApplication.translate("Calculator_window", u"*", None))
        self.op_equals.setText(QCoreApplication.translate("Calculator_window", u"=", None))
        self.op_dash.setText(QCoreApplication.translate("Calculator_window", u"-", None))
        self.op_clear.setText(QCoreApplication.translate("Calculator_window", u"Clear", None))
        self.op_back.setText(QCoreApplication.translate("Calculator_window", u"<--", None))
        self.op_decimal.setText(QCoreApplication.translate("Calculator_window", u".", None))
        self.pb_clickme.setText(QCoreApplication.translate("Calculator_window", u"Click me", None))
    # retranslateUi

