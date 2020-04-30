# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'counter_2_qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyEntry(QtWidgets.QTextEdit):

    def __init__(self, parent, master):
        super().__init__(parent)
        self.master = master

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.master.add_profile_wrap()
            return
        super().keyPressEvent(QKeyEvent)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.set_size = 22
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 441+self.set_size)
        MainWindow.setWindowTitle("MainWindow")
        MainWindow.setAccessibleName("")
        MainWindow.setStyleSheet("background-color: rgb(52, 61, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_just_count = QtWidgets.QFrame(self.centralwidget)
        self.frame_just_count.setGeometry(QtCore.QRect(0, 60, 600, 181+self.set_size))
        self.frame_just_count.setAccessibleName("")
        self.frame_just_count.setAutoFillBackground(False)
        self.frame_just_count.setStyleSheet("border-color: rgb(79, 103, 81);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;")
        self.frame_just_count.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_just_count.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_just_count.setLineWidth(2)
        self.frame_just_count.setMidLineWidth(0)
        self.frame_just_count.setObjectName("frame_just_count")
        self.label_2 = QtWidgets.QLabel(self.frame_just_count)
        self.label_2.setGeometry(QtCore.QRect(10, 4, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAccessibleName("")
        self.label_2.setStyleSheet("color: rgb(79, 103, 81);\n"
"border-style: flat;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-width: 0px;\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.entry = MyEntry(self.frame_just_count, self)
        self.entry.setGeometry(QtCore.QRect(10, 140+self.set_size, 401, 31))
        self.entry.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(75)
        self.entry.setFont(font)
        self.entry.setAccessibleName("")
        self.entry.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color: rgb(79, 103, 81);")
        self.entry.setObjectName("entry")
        self.add = QtWidgets.QPushButton(self.frame_just_count)
        self.add.setGeometry(QtCore.QRect(420, 140+self.set_size, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add.setFont(font)
        self.add.setStatusTip("")
        self.add.setWhatsThis("")
        self.add.setAccessibleName("")
        self.add.setAccessibleDescription("")
        self.add.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        self.add.setDefault(True)
        self.add.setObjectName("add")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_just_count)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 29, 581, 101+self.set_size))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet("color: rgb(79, 103, 81);\n"
"border-style: flat;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-width: 0px;\n"
"")
        self.box_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.box_layout.setContentsMargins(0, 0, 0, 0)
        self.box_layout.setObjectName("box_layout")

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.group_box = QtWidgets.QGroupBox()
        self.form_layout = QtWidgets.QFormLayout()
        self.group_box.setLayout(self.form_layout)
        self.box_layout.addWidget(self.scroll)

        self.frame_click_counter = QtWidgets.QFrame(self.centralwidget)
        self.frame_click_counter.setGeometry(QtCore.QRect(0, 250+self.set_size, 600, 171))
        self.frame_click_counter.setAccessibleName("")
        self.frame_click_counter.setStyleSheet("\n"
"border-color:rgb(79, 103, 81);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;")
        self.frame_click_counter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_click_counter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_click_counter.setLineWidth(2)
        self.frame_click_counter.setObjectName("frame_click_counter")
        self.click = QtWidgets.QPushButton(self.frame_click_counter)
        self.click.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.click.setFont(font)
        self.click.setAccessibleName("")
        self.click.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        self.click.setObjectName("click")
        self.click.setCheckable(True)
        self.reset = QtWidgets.QPushButton(self.frame_click_counter)
        self.reset.setGeometry(QtCore.QRect(190, 30, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.reset.setFont(font)
        self.reset.setAccessibleName("")
        self.reset.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        self.reset.setObjectName("reset")
        self.export_click = QtWidgets.QPushButton(self.frame_click_counter)
        self.export_click.setGeometry(QtCore.QRect(280, 30, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.export_click.setFont(font)
        self.export_click.setAccessibleName("")
        self.export_click.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        self.export_click.setObjectName("export_click")
        self.frame_lmb = QtWidgets.QFrame(self.frame_click_counter)
        self.frame_lmb.setGeometry(QtCore.QRect(380, 10, 101, 71))
        self.frame_lmb.setAccessibleName("")
        self.frame_lmb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lmb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lmb.setObjectName("frame_lmb")
        self.lcd_lmb = QtWidgets.QLCDNumber(self.frame_lmb)
        self.lcd_lmb.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.lcd_lmb.setAccessibleName("")
        self.lcd_lmb.setStyleSheet("border-radius: 5px;\n"
"gridline-color: rgb(0, 85, 0);\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcd_lmb.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_lmb.setObjectName("lcd_lmb")
        self.lcd_lmb.setDigitCount(6)
        self.label_3 = QtWidgets.QLabel(self.frame_lmb)
        self.label_3.setGeometry(QtCore.QRect(35, 6, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAccessibleName("")
        self.label_3.setStyleSheet("border-width: 0px;\n"
"border-radius: 0px;")
        self.label_3.setObjectName("label_3")
        self.frame_rmb = QtWidgets.QFrame(self.frame_click_counter)
        self.frame_rmb.setGeometry(QtCore.QRect(490, 10, 101, 71))
        self.frame_rmb.setAccessibleName("")
        self.frame_rmb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rmb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rmb.setObjectName("frame_rmb")
        self.lcd_rmb = QtWidgets.QLCDNumber(self.frame_rmb)
        self.lcd_rmb.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.lcd_rmb.setAccessibleName("")
        self.lcd_rmb.setStyleSheet("border-radius: 5px;\n"
"gridline-color: rgb(0, 85, 0);\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcd_rmb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd_rmb.setSmallDecimalPoint(False)
        self.lcd_rmb.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_rmb.setObjectName("lcd_rmb")
        self.lcd_rmb.setDigitCount(6)
        self.label_4 = QtWidgets.QLabel(self.frame_rmb)
        self.label_4.setGeometry(QtCore.QRect(32, 6, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAccessibleName("")
        self.label_4.setStyleSheet("border-width: 0px;\n"
"border-radius: 0px;")
        self.label_4.setObjectName("label_4")
        self.cb_start_active = QtWidgets.QCheckBox(self.frame_click_counter)
        self.cb_start_active.setGeometry(QtCore.QRect(20, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cb_start_active.setFont(font)
        self.cb_start_active.setAccessibleName("")
        self.cb_start_active.setStyleSheet("border-width: 0px;\n"
"")
        self.cb_start_active.setObjectName("cb_start_active")
        self.cb_start_active_2 = QtWidgets.QCheckBox(self.frame_click_counter)
        self.cb_start_active_2.setGeometry(QtCore.QRect(20, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cb_start_active_2.setFont(font)
        self.cb_start_active_2.setAccessibleName("")
        self.cb_start_active_2.setStyleSheet("border-width: 0px;\n"
"")
        self.cb_start_active_2.setObjectName("cb_start_active_2")
        self.cb_start_active_3 = QtWidgets.QCheckBox(self.frame_click_counter)
        self.cb_start_active_3.setGeometry(QtCore.QRect(20, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cb_start_active_3.setFont(font)
        self.cb_start_active_3.setToolTip("This will export the hourly mouseclicks to a csv-file in your counter directory.")
        self.cb_start_active_3.setAccessibleName("")
        self.cb_start_active_3.setStyleSheet("border-width: 0px;\n"
"")
        self.cb_start_active_3.setObjectName("cb_start_active_3")
        self.label_5 = QtWidgets.QLabel(self.frame_click_counter)
        self.label_5.setGeometry(QtCore.QRect(10, 4, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAccessibleName("")
        self.label_5.setStyleSheet("color: rgb(79, 103, 81);\n"
"border-style: flat;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-width: 0px;\n"
"")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_click_counter)
        self.label_6.setGeometry(QtCore.QRect(380, 130, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setToolTipDuration(-1)
        self.label.setAccessibleName("")
        self.label.setStyleSheet("background-color: rgb(52, 61, 54);\n"
"color: rgb(79, 103, 81);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        #self.menubar.setAccessibleName("")
        #self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAccessibleName("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Just count stuff"))
        self.add.setText(_translate("MainWindow", "Add something to count"))
        self.click.setText(_translate("MainWindow", "Activate Click Counter"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.export_click.setText(_translate("MainWindow", "Export"))
        self.label_3.setText(_translate("MainWindow", "LMB"))
        self.label_4.setText(_translate("MainWindow", "RMB"))
        self.cb_start_active.setText(_translate("MainWindow", "Start activated"))
        self.cb_start_active_2.setText(_translate("MainWindow", "Add to windows auto-run"))
        self.cb_start_active_3.setText(_translate("MainWindow", "Automatic Export"))
        self.label_5.setText(_translate("MainWindow", "Click counter"))
        self.label_6.setText(_translate("MainWindow", "temporary click count:"))
        self.label.setText(_translate("MainWindow", "Stuff Counter"))
