from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_CounterWindow(object):
    def setupUi(self, CounterWindow):
        CounterWindow.setObjectName("CounterWindow")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        sizePolicy.setHeightForWidth(CounterWindow.sizePolicy().hasHeightForWidth())
        CounterWindow.setSizePolicy(sizePolicy)
        CounterWindow.setAutoFillBackground(False)

        self.gridLayout = QtWidgets.QGridLayout(CounterWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 5, 5)
        self.button_up = QtWidgets.QPushButton(CounterWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        sizePolicy.setHeightForWidth(self.button_up.sizePolicy().hasHeightForWidth())
        self.button_up.setSizePolicy(sizePolicy)
        self.button_up.setMinimumSize(QtCore.QSize(340, 180))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.button_up.setFont(font)

        self.button_up.setAutoDefault(False)
        self.button_up.setDefault(True)
        self.button_up.setObjectName("button_up")
        self.gridLayout.addWidget(self.button_up, 1, 1, 1, 1)

        self.button_down = QtWidgets.QPushButton(CounterWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_down.sizePolicy().hasHeightForWidth())
        self.button_down.setSizePolicy(sizePolicy)
        self.button_down.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_down.setFont(font)

        self.button_down.setObjectName("button_down")
        self.gridLayout.addWidget(self.button_down, 3, 3, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 2)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 2, 1)

        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)


        self.retranslateUi(CounterWindow)
        QtCore.QMetaObject.connectSlotsByName(CounterWindow)

    def retranslateUi(self, CounterWindow):
        _translate = QtCore.QCoreApplication.translate
        CounterWindow.setWindowTitle(_translate("CounterWindow", "Counter Title"))
        self.button_up.setText(_translate("CounterWindow", "0"))
        self.button_down.setText(_translate("CounterWindow", "-"))


class CounterProfile:
    def __init__(self, master, profile_title, counter = 0):

        self.master = master
        self.profile_title = profile_title
        self.counter = counter

    def __repr__(self):
        return ("Counter:" + self.profile_title)

    def __call__(self, master, profile_title):

        self.CounterWindow = QtWidgets.QDialog(self.master)
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
