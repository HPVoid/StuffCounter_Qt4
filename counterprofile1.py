from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_CounterWindow(object):
    def setupUi(self, CounterWindow):
        CounterWindow.setObjectName("CounterWindow")
        CounterWindow.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CounterWindow.sizePolicy().hasHeightForWidth())
        CounterWindow.setSizePolicy(sizePolicy)
        CounterWindow.setAutoFillBackground(False)
        CounterWindow.setStyleSheet("background-color: rgb(52, 61, 54);")
        self.button_up = QtWidgets.QPushButton(CounterWindow)
        self.button_up.setGeometry(QtCore.QRect(80, 60, 341, 180))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.button_up.setFont(font)
        self.button_up.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);\n}"
"QPushButton:pressed {border-style: solid; background-color: rgb(65, 85, 67)}")
        self.button_up.setDefault(True)
        self.button_up.setObjectName("button_up")
        self.button_up.setText("0")

        self.button_down = QtWidgets.QPushButton(CounterWindow)
        self.button_down.setGeometry(QtCore.QRect(450, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_down.setFont(font)
        self.button_down.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);\n}"
"QPushButton:pressed {border-style: solid; background-color: rgb(65, 85, 67)}")
        self.button_down.setObjectName("button_down")
        self.button_down.setText("-")
        QtCore.QMetaObject.connectSlotsByName(CounterWindow)


class CounterProfile:
    def __init__(self, master, profile_title, counter = 0):

        self.master = master
        self.profile_title = profile_title
        self.counter = counter

    def __repr__(self):
        return ("Counter:" + self.profile_title)

    def __call__(self, master, profile_title):

        self.CounterWindow = QtWidgets.QDialog()
        self.ui = Ui_CounterWindow()
        self.ui.setupUi(self.CounterWindow)
        self.CounterWindow.show()

        self.CounterWindow.setWindowTitle(profile_title)
        self.ui.button_up.setText(str(self.counter))

        self.ui.button_up.clicked.connect(self.count)
        self.ui.button_down.clicked.connect(self.minus)

        self.CounterWindow.exec()


    def change_button(self):
        self.ui.button_up.setText(str(self.counter))

    def count(self):
        self.counter += 1
        self.change_button()
        self.master.update_profile_count(self.profile_title)

    def minus(self):
        self.counter -= 1
        self.change_button()
        self.master.update_profile_count(self.profile_title)
