from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import sys
from counter_main_window import Ui_MainWindow, MyEntry, Mainwindow_changed
from counterprofile1 import CounterProfile
from profile_frame_qt4 import ProfileFrame
import win32api
from datetime import datetime
import time
import os
import getpass
from PyQt5.QtGui import QImage

class MyEntry(QtWidgets.QTextEdit):

    def __init__(self, parent, master, function):
        super().__init__(parent)
        self.master = master
        self.function = function


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.function()
            return
        super().keyPressEvent(QKeyEvent)

class SystemTray(QtWidgets.QSystemTrayIcon):

    def __init__(self, parent = None):
        QtWidgets.QSystemTrayIcon.__init__(self, parent)
        self.setIcon(QtGui.QIcon("Icon.png"))

        menu = QtWidgets.QMenu(parent)
        menu.addAction("Show")
        menu.addAction("Info")
        menu.addAction("Quit")

        self.setContextMenu(menu)
        self.contextMenu().triggered.connect(self.triggered)

        self.activated.connect(self.icon_clicked)

    def triggered(self, action):
        if action.text() == "Quit":
            self.hide()
            app.quit()
        if action.text() == "Show":
            main_window.show()
        if action.text() == "Info":
            main_window.info_window()

    def icon_clicked(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            main_window.show()

class Ui_MainWindow(QtWidgets.QMainWindow):

        def __init__(self):
            super().__init__()
            self.trayIcon = SystemTray()

        def closeEvent(self, event):
            event.ignore()
            self.hide()
            self.trayIcon.show()

        def setupUi(self):
            self.setObjectName("MainWindow")
            self.setWindowModality(QtCore.Qt.NonModal)
            self.resize(776, 584)
            self.setStyleSheet("background-color: rgb(29, 67, 88);\n"
    "border-color:rgb(30, 121, 177);\n"
    "color:rgb(30, 121, 177);\n"
    "\n"
    "")
            self.centralwidget = QtWidgets.QWidget(self)
            self.centralwidget.setObjectName("centralwidget")

            self.setWindowIcon(QIcon("Icon.png"))

            self.verticalLayout_main_window = QtWidgets.QVBoxLayout(self.centralwidget)
            self.verticalLayout_main_window.setContentsMargins(10, 10, 10, 10)
            self.verticalLayout_main_window.setSpacing(10)
            self.verticalLayout_main_window.setObjectName("verticalLayout_main_window")
            self.label = QtWidgets.QLabel(self.centralwidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
            self.label.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(30)
            font.setBold(True)
            font.setWeight(75)
            font.setKerning(True)
            self.label.setFont(font)

            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.verticalLayout_main_window.addWidget(self.label)
            self.frame_just_count = QtWidgets.QFrame(self.centralwidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_just_count.sizePolicy().hasHeightForWidth())
            self.frame_just_count.setSizePolicy(sizePolicy)
            self.frame_just_count.setAutoFillBackground(False)
            self.frame_just_count.setStyleSheet("border-style: solid;\n"
    "border-width: 2px;\n"
    "border-radius: 10px;\n")
            self.frame_just_count.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_just_count.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.frame_just_count.setLineWidth(2)
            self.frame_just_count.setMidLineWidth(0)
            self.frame_just_count.setObjectName("frame_just_count")
            self.frame_just_count.setMinimumSize(QtCore.QSize(621, 254))
            self.verticalLayout_just_count = QtWidgets.QVBoxLayout(self.frame_just_count)
            self.verticalLayout_just_count.setContentsMargins(10, 10, 10, 10)
            self.verticalLayout_just_count.setSpacing(10)
            self.verticalLayout_just_count.setObjectName("verticalLayout_just_count")
            self.label_2 = QtWidgets.QLabel(self.frame_just_count)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
            self.label_2.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("border-width: 0px;\n")
            self.label_2.setTextFormat(QtCore.Qt.AutoText)
            self.label_2.setObjectName("label_2")
            self.verticalLayout_just_count.addWidget(self.label_2)


            self.scroll = QtWidgets.QScrollArea()
            self.scroll.setWidgetResizable(True)
            self.scroll.setStyleSheet("border-width: 0px;\n")

            self.group_box = QtWidgets.QGroupBox()
            self.group_box.setStyleSheet("border-width: 0px;\n")
            self.form_layout = QtWidgets.QFormLayout()
            self.group_box.setLayout(self.form_layout)

            self.verticalLayout_just_count.addWidget(self.group_box)
            self.verticalLayout_just_count.addWidget(self.scroll)

            self.horizontalLayout_add_entry = QtWidgets.QHBoxLayout()
            self.horizontalLayout_add_entry.setSpacing(10)
            self.horizontalLayout_add_entry.setObjectName("horizontalLayout_add_entry")
            self.add = QtWidgets.QPushButton(self.frame_just_count)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
            self.add.setSizePolicy(sizePolicy)
            self.add.setMinimumSize(QtCore.QSize(160, 31))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.add.setFont(font)
            self.add.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(41, 96, 125);\n"
    "color:rgb(0, 0, 0)}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
            self.add.setDefault(True)
            self.add.setObjectName("add")
            self.horizontalLayout_add_entry.addWidget(self.add)
            self.entry = MyEntry(self.frame_just_count, self, self.add_profile_wrap)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.entry.sizePolicy().hasHeightForWidth())
            self.entry.setSizePolicy(sizePolicy)
            self.entry.setMinimumSize(QtCore.QSize(401, 31))
            self.entry.setSizeIncrement(QtCore.QSize(150, 31))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            self.entry.setFont(font)
            self.entry.setStyleSheet("background-color:rgb(0, 0, 0)")
            self.entry.setLineWidth(1)
            self.entry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.entry.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.entry.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
            self.entry.setObjectName("entry")
            self.horizontalLayout_add_entry.addWidget(self.entry)
            self.verticalLayout_just_count.addLayout(self.horizontalLayout_add_entry)
            self.verticalLayout_main_window.addWidget(self.frame_just_count)

            self.frame_click_counter = QtWidgets.QFrame(self.centralwidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_click_counter.sizePolicy().hasHeightForWidth())
            self.frame_click_counter.setSizePolicy(sizePolicy)
            self.frame_click_counter.setMinimumSize(QtCore.QSize(0, 0))
            self.frame_click_counter.setMaximumSize(QtCore.QSize(16777215, 220))
            self.frame_click_counter.setStyleSheet("border-style: solid;\n"
    "border-width: 2px;\n"
    "border-radius: 10px;")
            self.frame_click_counter.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_click_counter.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.frame_click_counter.setLineWidth(2)
            self.frame_click_counter.setObjectName("frame_click_counter")
            self.gridLayout_click_counter = QtWidgets.QGridLayout(self.frame_click_counter)
            self.gridLayout_click_counter.setContentsMargins(10, 10, 10, 10)
            self.gridLayout_click_counter.setSpacing(10)
            self.gridLayout_click_counter.setObjectName("gridLayout_click_counter")
            self.cb_start_active = QtWidgets.QCheckBox(self.frame_click_counter)
            self.cb_start_active.setMinimumSize(QtCore.QSize(0, 20))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.cb_start_active.setFont(font)
            self.cb_start_active.setAccessibleName("")
            self.cb_start_active.setStyleSheet("border-width: 0px;\n"
        "color: rgb(0, 0, 0)")
            self.cb_start_active.setObjectName("cb_start_active")
            self.gridLayout_click_counter.addWidget(self.cb_start_active, 4, 0, 1, 1)
            self.cb_hide = QtWidgets.QCheckBox(self.frame_click_counter)
            self.cb_hide.setMinimumSize(QtCore.QSize(0, 20))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.cb_hide.setFont(font)
            self.cb_hide.setAccessibleName("")
            self.cb_hide.setStyleSheet("border-width: 0px;\n"
        "color: rgb(0, 0, 0)")
            self.cb_hide.setObjectName("cb_hide")
            self.gridLayout_click_counter.addWidget(self.cb_hide, 6, 0, 1, 1)
            self.label_6 = QtWidgets.QLabel(self.frame_click_counter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
            self.label_6.setSizePolicy(sizePolicy)
            self.label_6.setMinimumSize(QtCore.QSize(0, 20))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.label_6.setFont(font)
            self.label_6.setStyleSheet("border-width: 0px;\n")
            self.label_6.setFrameShape(QtWidgets.QFrame.HLine)
            self.label_6.setLineWidth(0)
            self.label_6.setObjectName("label_6")
            self.gridLayout_click_counter.addWidget(self.label_6, 7, 4, 1, 2)
            self.export_click = QtWidgets.QPushButton(self.frame_click_counter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.export_click.sizePolicy().hasHeightForWidth())
            self.export_click.setSizePolicy(sizePolicy)
            self.export_click.setMinimumSize(QtCore.QSize(75, 31))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.export_click.setFont(font)
            self.export_click.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(41, 96, 125);\n"
    "color:rgb(0, 0, 0)}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
            self.export_click.setObjectName("export_click")
            self.gridLayout_click_counter.addWidget(self.export_click, 1, 2, 1, 1)
            self.cb_auto_export = QtWidgets.QCheckBox(self.frame_click_counter)
            self.cb_auto_export.setMinimumSize(QtCore.QSize(0, 20))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.cb_auto_export.setFont(font)
            self.cb_auto_export.setToolTip("This will export the hourly mouseclicks to a csv-file in your counter directory.")
            self.cb_auto_export.setStyleSheet("border-width: 0px;\n"
    "color: rgb(0, 0, 0)")
            self.cb_auto_export.setObjectName("cb_auto_export")
            self.gridLayout_click_counter.addWidget(self.cb_auto_export, 7, 0, 1, 1)
            spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_click_counter.addItem(spacerItem, 1, 3, 1, 1)
            self.reset = QtWidgets.QPushButton(self.frame_click_counter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
            self.reset.setSizePolicy(sizePolicy)
            self.reset.setMinimumSize(QtCore.QSize(75, 31))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.reset.setFont(font)
            self.reset.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(41, 96, 125);\n"
    "color:rgb(0, 0, 0)}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
            self.reset.setObjectName("reset")
            self.gridLayout_click_counter.addWidget(self.reset, 1, 1, 1, 1)
            self.click = QtWidgets.QPushButton(self.frame_click_counter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.click.sizePolicy().hasHeightForWidth())
            self.click.setSizePolicy(sizePolicy)
            self.click.setMinimumSize(QtCore.QSize(160, 31))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.click.setFont(font)
            self.click.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(41, 96, 125);\n"
    "color:rgb(0, 0, 0)}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
            self.click.setCheckable(True)
            self.click.setObjectName("click")
            self.gridLayout_click_counter.addWidget(self.click, 1, 0, 1, 1)
            self.frame_rmb = QtWidgets.QFrame(self.frame_click_counter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_rmb.sizePolicy().hasHeightForWidth())
            self.frame_rmb.setSizePolicy(sizePolicy)
            self.frame_rmb.setMinimumSize(QtCore.QSize(111, 81))
            self.frame_rmb.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_rmb.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_rmb.setObjectName("frame_rmb")
            self.verticalLayout_rmb = QtWidgets.QVBoxLayout(self.frame_rmb)
            self.verticalLayout_rmb.setContentsMargins(10, 10, 10, 10)
            self.verticalLayout_rmb.setSpacing(5)
            self.verticalLayout_rmb.setObjectName("verticalLayout_rmb")
            self.label_4 = QtWidgets.QLabel(self.frame_rmb)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.label_4.setFont(font)
            self.label_4.setAccessibleName("")
            self.label_4.setStyleSheet("border-width: 0px;")
            self.label_4.setAlignment(QtCore.Qt.AlignCenter)
            self.label_4.setObjectName("label_4")
            self.verticalLayout_rmb.addWidget(self.label_4)
            self.lcd_rmb = QtWidgets.QLCDNumber(self.frame_rmb)
            self.lcd_rmb.setStyleSheet("border-radius: 5px;\n"
    "gridline-color: rgb(0, 85, 0);\n"
    "color: rgb(170, 0, 0);\n"
    "background-color: rgb(0, 0, 0);\n"
    "border-color:rgb(41, 96, 125)")
            self.lcd_rmb.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.lcd_rmb.setSmallDecimalPoint(False)
            self.lcd_rmb.setDigitCount(6)
            self.lcd_rmb.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.lcd_rmb.setProperty("intValue", 0)
            self.lcd_rmb.setObjectName("lcd_rmb")
            self.verticalLayout_rmb.addWidget(self.lcd_rmb)
            self.gridLayout_click_counter.addWidget(self.frame_rmb, 0, 5, 1, 1)
            self.cb_auto_start = QtWidgets.QCheckBox(self.frame_click_counter)
            self.cb_auto_start.setMinimumSize(QtCore.QSize(0, 20))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.cb_auto_start.setFont(font)
            self.cb_auto_start.setAccessibleName("")
            self.cb_auto_start.setStyleSheet("border-width: 0px;\n"
    "color: rgb(0, 0, 0)")
            self.cb_auto_start.setObjectName("cb_auto_start")
            self.gridLayout_click_counter.addWidget(self.cb_auto_start, 5, 0, 1, 1)
            self.label_5 = QtWidgets.QLabel(self.frame_click_counter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
            self.label_5.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            self.label_5.setFont(font)
            self.label_5.setStyleSheet("border-width: 0px;")
            self.label_5.setTextFormat(QtCore.Qt.AutoText)
            self.label_5.setObjectName("label_5")
            self.gridLayout_click_counter.addWidget(self.label_5, 0, 0, 1, 1)
            spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            self.gridLayout_click_counter.addItem(spacerItem1, 3, 0, 1, 1)
            self.frame_lmb = QtWidgets.QFrame(self.frame_click_counter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_lmb.sizePolicy().hasHeightForWidth())
            self.frame_lmb.setSizePolicy(sizePolicy)
            self.frame_lmb.setMinimumSize(QtCore.QSize(111, 81))
            self.frame_lmb.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_lmb.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_lmb.setObjectName("frame_lmb")
            self.verticalLayout_lmb = QtWidgets.QVBoxLayout(self.frame_lmb)
            self.verticalLayout_lmb.setContentsMargins(10, 10, 10, 10)
            self.verticalLayout_lmb.setSpacing(5)
            self.verticalLayout_lmb.setObjectName("verticalLayout_lmb")
            self.label_3 = QtWidgets.QLabel(self.frame_lmb)
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("border-width: 0px;")
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.label_3.setObjectName("label_3")
            self.verticalLayout_lmb.addWidget(self.label_3)
            self.lcd_lmb = QtWidgets.QLCDNumber(self.frame_lmb)
            self.lcd_lmb.setAccessibleName("")
            self.lcd_lmb.setStyleSheet("border-radius: 5px;\n"
    "gridline-color: rgb(0, 85, 0);\n"
    "color: rgb(170, 0, 0);\n"
    "background-color: rgb(0, 0, 0);\n"
    "border-color:rgb(41, 96, 125)")
            self.lcd_lmb.setDigitCount(6)
            self.lcd_lmb.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.lcd_lmb.setObjectName("lcd_lmb")
            self.verticalLayout_lmb.addWidget(self.lcd_lmb)
            self.gridLayout_click_counter.addWidget(self.frame_lmb, 0, 4, 3, 1)
            self.verticalLayout_main_window.addWidget(self.frame_click_counter)
            self.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(self)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 21))
            self.menubar.setObjectName("menubar")
            self.menubar.setStyleSheet("color: rgb(0,0,0)")
            self.setMenuBar(self.menubar)
            action_app = self.menubar.addMenu("Options")
            action_app.addAction("Info")
            action_app.addAction("Reset all")
        #    action_app.addAction("Dolphin")
            quit_action = action_app.addAction("Quit")
            quit_action.setShortcut("Ctrl+Q")

            self.statusbar = QtWidgets.QStatusBar(self)
            self.statusbar.setObjectName("statusbar")
            self.setStatusBar(self.statusbar)

            self.retranslateUi()
            QtCore.QMetaObject.connectSlotsByName(self)

        def retranslateUi(self):
            _translate = QtCore.QCoreApplication.translate
            self.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label.setText(_translate("MainWindow", "Stuff Counter"))
            self.label_2.setText(_translate("MainWindow", "Just count stuff"))
            self.add.setText(_translate("MainWindow", "Add something to count"))
            self.click.setText(_translate("MainWindow", "Activate Click Counter"))
            self.cb_auto_export.setText(_translate("MainWindow", "Automatic Export"))
            self.export_click.setText(_translate("MainWindow", "Export"))
            self.label_5.setText(_translate("MainWindow", "Click counter"))
            self.cb_hide.setText(_translate("MainWindow", "Hide window on start-up"))
            self.cb_auto_start.setText(_translate("MainWindow", "Add to windows auto-run"))
            self.cb_start_active.setText(_translate("MainWindow", "Start activated"))
            self.reset.setText(_translate("MainWindow", "Reset"))
            self.label_3.setText(_translate("MainWindow", "LMB"))
            self.label_4.setText(_translate("MainWindow", "RMB"))
            self.label_6.setText(_translate("MainWindow", "temporary click count:"))

class ClickCounterThread(QtCore.QThread):
    def __init__(self, master):
        self.master = master
        QtCore.QThread.__init__(self)
        file2 = open("click_count.txt","r")
        click_count_list = file2.read().split(" ")

    def run(self):

        self.state_left = win32api.GetKeyState(0x01)
        self.state_right = win32api.GetKeyState(0x02)

        while self.master.stop_loop == False:
            left = win32api.GetKeyState(0x01)
            right = win32api.GetKeyState(0x02)
            if left != self.state_left:
                self.state_left = left

                if left < 0:
                    self.master.click_count_l += 1
                    self.master.lcd_lmb.display(self.master.click_count_l)
                    if self.master.cb_auto_export.isChecked():
                        self.master.click_count_l_temp += 1
                        self.master.label_6.setText("temporary click count: "+ str(self.master.click_count_l_temp) + " " + str(self.master.click_count_r_temp))
                    self.master.store_click_count()


            if right != self.state_right:
                self.state_right = right

                if right < 0:
                    self.master.click_count_r += 1
                    self.master.lcd_rmb.display(self.master.click_count_r)
                    if self.master.cb_auto_export.isChecked():
                        self.master.click_count_r_temp += 1
                        self.master.label_6.setText("temporary click count: "+ str(self.master.click_count_l_temp) + " " + str(self.master.click_count_r_temp))
                    self.master.store_click_count()

            time.sleep(0.04)

class LogTimeThread(QtCore.QThread):
    def __init__(self, master):
        self.master = master
        QtCore.QThread.__init__(self)

    def run(self):

        while self.master.cb_auto_export.isChecked():
            now_datetime = datetime.now().isoformat(timespec='seconds')
            file_time = open("timelog.txt", "w")
            file_time.write(self.master.new_start_datetime + "\n" + now_datetime)
            file_time.close()
            self.master.auto_export(0)
            print(now_datetime)

            time.sleep(1)

class CounterApp(Ui_MainWindow):
    def __init__(self):

        super().__init__()
        super().setupUi()
        super().retranslateUi()

        self.menubar.triggered.connect(self.options)

        self.add.clicked.connect(self.add_profile_wrap)
        self.reset.clicked.connect(self.sure)
        self.export_click.clicked.connect(self.click_export)
        self.click.clicked[bool].connect(self.click_counter)

        #open click counts on startup
        file2 = open("click_count.txt","r")
        click_count_list = file2.read().split(" ")
        self.click_count_l = int(click_count_list[0])
        self.click_count_r = int(click_count_list[1])
        self.click_count_l_temp = int(click_count_list[2])
        self.click_count_r_temp = int(click_count_list[3])
        self.lcd_lmb.display(self.click_count_l)
        self.lcd_rmb.display(self.click_count_r)

        #open profiles on startup
        file1 = open("profile_dict.txt","r")
        self.profile_dict = eval(file1.read())
        self.profiles = {}
        self.frame_dict = {}
        for key, value in self.profile_dict.items():
            self.create_profile(key, value)
            #self.add_frame(key)
        print(self.profiles)

        #creating frames for each counter profile
        for key in self.profile_dict.keys():
            self.add_frame(key)

        #open the state of checkboxes on startup
        self.cb_start_active.checkStateSet()
        file3 = open("state.txt","r")
        file3_list = eval(file3.read())
        self.cb_start_active.setChecked(file3_list[0])
        self.cb_auto_start.setChecked(file3_list[1])
        if file3_list[0]:
            self.cb_auto_export.setChecked(file3_list[2])
        else:
            self.cb_auto_export.setChecked(False)

        self.cb_hide.setChecked(file3_list[3])

        self.cb_start_active.stateChanged.connect(self.set_start_active)
        self.cb_auto_start.stateChanged.connect(self.set_auto_start)
        self.cb_auto_export.stateChanged.connect(self.set_auto_export)
        self.cb_hide.stateChanged.connect(self.set_hide)
        self.cb_auto_export.setEnabled(False)

        USER_NAME = getpass.getuser()
        self.file_dir = os.path.dirname(os.path.realpath(__file__))
        self.file_path = self.file_dir + "\counter_2_qt4.exe"
        self.bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        #dealing with bugs:
        if os.path.exists(self.bat_path + '\\' + "StuffCounter_qt.bat") and not self.cb_auto_start.isChecked():
            self.cb_auto_start.setChecked(True)
        if not os.path.exists(self.bat_path + '\\' + "StuffCounter_qt.bat") and self.cb_auto_start.isChecked():
            self.cb_auto_start.setChecked(False)

        self.start_active()

    def start_active(self):
        if self.cb_start_active.isChecked():
            self.click_counter(True)
            self.click.toggle()

    def set_start_active(self):
        file3 = open("state.txt","w")
        file3.write(str([self.cb_start_active.isChecked(), self.cb_auto_start.isChecked(), self.cb_auto_export.isChecked(), self.cb_hide.isChecked()]))
        file3.close()

    def set_auto_start(self):
        file3 = open("state.txt","w")
        file3.write(str([self.cb_start_active.isChecked(), self.cb_auto_start.isChecked(), self.cb_auto_export.isChecked(), self.cb_hide.isChecked()]))
        file3.close()

        if os.path.exists(self.bat_path + '\\' + "StuffCounter_qt.bat") and self.cb_auto_start.isChecked()==False:
            os.remove(self.bat_path + '\\' + "StuffCounter_qt.bat")
            return

        with open(self.bat_path + '\\' + "StuffCounter_qt.bat", "w+") as bat_file:
            bat_file.write(r'set workingdir=%s' % self.file_dir + "\n" + r'pushd %workingdir%' + "\n" + r'start "" counter_2_qt4.exe')

    def set_hide(self):
        file3 = open("state.txt","w")
        file3.write(str([self.cb_start_active.isChecked(), self.cb_auto_start.isChecked(), self.cb_auto_export.isChecked(), self.cb_hide.isChecked()]))
        file3.close()

    def set_auto_export(self):
        file3 = open("state.txt","w")
        file3.write(str([self.cb_start_active.isChecked(), self.cb_auto_start.isChecked(), self.cb_auto_export.isChecked(), self.cb_hide.isChecked()]))
        file3.close()
        self.log_time()

        if not self.cb_auto_export.isChecked():
            self.reset_click_counter_temp()

    def log_time(self):
        if self.cb_auto_export.isChecked():
            self.auto_export(1)
            self.new_start_datetime = datetime.now().isoformat(timespec='seconds')

            self.log_time_thread = LogTimeThread(self)
            self.log_time_thread.start()

    def auto_export(self, index):
        if not os.path.exists("timelog.txt"):
            file_time2 = open("timelog.txt", "w")
            file_time2.write(datetime.now().isoformat(timespec='seconds') + "\n" + datetime.now().isoformat(timespec='seconds'))
            file_time2.close()
        file_time2 = open("timelog.txt", "r")
        time_list = file_time2.read().split("\n")
        #time of starting the timelog:
        start_datetime = datetime.now().isoformat(timespec='seconds')
        start_date = start_datetime.split("T")[0]
        start_time = start_datetime.split("T")[1]
        start_hour = start_time.split(":")[0]
        #time when the last timelog was finished:
        last_end_datetime = time_list[index]
        last_end_date = last_end_datetime.split("T")[0]
        last_end_time = last_end_datetime.split("T")[1]
        last_end_hour = last_end_time.split(":")[0]
        print(start_hour)
        print(last_end_hour)
        #creating the automatic export csv file:
        if start_hour != last_end_hour or start_date != last_end_date:
            #creating new file with header if there is no file with this date yet:
            if not os.path.exists(last_end_date + ".csv"):
                exp_file = open((last_end_date + ".csv"),"a")
                exp_file.write("hour; LMB; RMB")
                for i in range(int(last_end_hour)):
                    exp_file.write("\n{0}; 0; 0".format(str(i)))
                exp_file.close()
            #appending another line with the click counts of the last active hour:
            exp_file = open((last_end_date + ".csv"),"a")
            exp_file.write("\n{0}; {1}; {2}".format(last_end_hour, str(self.click_count_l_temp), str(self.click_count_r_temp)))

            #for the case that the last active hour is more than one hour ago, the inactive hours in between fill be added with 0; 0:
            if last_end_date == start_date:
                time_diff = int(start_hour) - int(last_end_hour)
                for i in range(time_diff)[1:]:
                    inactive_hours = int(last_end_hour) + i
                    exp_file.write("\n{0}; 0; 0".format(str(inactive_hours)))
            #in case one (or more) days have passed since the last active hour, the csv.file for the last active day will be filled up to hour 23 with 0; 0:
            else:
                time_diff = 24 - int(last_end_hour)
                for i in range(time_diff)[1:]:
                    inactive_hours = int(last_end_hour) + i
                    exp_file.write("\n{0}; 0; 0".format(str(inactive_hours)))
                #also a new file for today is being created with 0; 0 until the time right now (is if not os.path.exists(start_date + ".csv") actually necessary in this case???)
                if not os.path.exists(start_date + ".csv"):
                    exp_file_today = open((start_date + ".csv"),"a")
                    exp_file_today.write("hour; LMB; RMB")
                    for i in range(int(start_hour)):
                        exp_file_today.write("\n{0}; 0; 0".format(str(i)))
                    exp_file_today.close()

            exp_file.close()
            self.reset_click_counter_temp()
            self.new_start_datetime = datetime.now().isoformat(timespec='seconds')

    def click_counter(self, activated):
        self.stop_loop = False

        if activated:
            print("activated!!!")
            self.click.setText("Deactivate Click Counter")
            self.click.setStyleSheet("QPushButton {background-color: rgb(125, 45, 76);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(125, 45, 76); color: rgb(0, 0, 0)}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(125, 45, 76), color: rgb(0, 0, 0)}")
            self.statusbar.showMessage("All your clicks are being counted")
            self.cb_auto_export.setEnabled(True)
            if self.cb_auto_export.isChecked():
                self.log_time()

        else:

            print("deactivated!!!")
            self.click.setText("Activate Click Counter")
            self.click.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(41, 96, 125);\n"
    "color:rgb(0, 0, 0)}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
            self.statusbar.showMessage("")
            self.click_count_l -= 1
            self.lcd_lmb.display(self.click_count_l)
            self.store_click_count()
            self.cb_auto_export.setChecked(False)
            file3 = open("state.txt","w")
            file3.write(str([self.cb_start_active.isChecked(), self.cb_auto_start.isChecked(), self.cb_auto_export.isChecked(), self.cb_hide.isChecked()]))
            file3.close()
            self.cb_auto_export.setEnabled(False)
            self.stop_loop = True

        self.clickcounter_thread = ClickCounterThread(self)
        self.clickcounter_thread.start()


    def reset_click_counter(self):
        self.click_count_l = 0
        self.click_count_r = 0
        self.lcd_lmb.display(self.click_count_l)
        self.lcd_rmb.display(self.click_count_r)
        self.reset_click_counter_temp()

    def reset_click_counter_temp(self):
        self.click_count_l_temp = 0
        self.click_count_r_temp = 0
        self.label_6.setText("temporary click count: "+ str(self.click_count_l_temp) + " " + str(self.click_count_r_temp))
        self.store_click_count()

    def reset_all(self):
        self.click_count_l = 0
        self.click_count_r = 0
        self.lcd_lmb.display(self.click_count_l)
        self.lcd_rmb.display(self.click_count_r)
        self.reset_click_counter_temp()

        self.profile_dict = {}
        self.file = open("profile_dict.txt","w")
        self.file.write(str(self.profile_dict))
        self.file.close()

        self.profiles = {}

        for title in self.frame_dict.keys():
            self.frame_dict[title].profile_frame_widget.deleteLater()
        self.frame_dict = {}

        self.cb_start_active.setChecked(False)
        self.cb_auto_start.setChecked(False)
        self.cb_auto_export.setChecked(False)
        self.cb_hide.setChecked(False)

        file3 = open("state.txt","w")
        file3.write(str([self.cb_start_active.isChecked(), self.cb_auto_start.isChecked(), self.cb_auto_export.isChecked(), self.cb_hide.isChecked()]))
        file3.close()

        now_datetime = datetime.now().isoformat(timespec='seconds')

        file_time = open("timelog.txt", "w")
        file_time.write(now_datetime + "\n" + now_datetime)
        file_time.close()


    def click_export_ok(self):

        def write_exp_file_txt():
            exp_file = open((self.export_entry.toPlainText()+".txt"),"w")
            exp_file.write("LMB: "+str(self.click_count_l)+" RMB: "+str(self.click_count_r))
            exp_file.close()
            self.Export_Dialog.close()

        def write_exp_file_csv():
            exp_file = open((self.export_entry.toPlainText()+".csv"),"w")
            exp_file.write("LMB; RMB\n{0}; {1}".format(str(self.click_count_l), str(self.click_count_r)))
            exp_file.close()
            self.Export_Dialog.close()


        if self.dropdown.currentIndex() == 0:
            write_exp_file_txt()
        if self.dropdown.currentIndex() == 1:
            write_exp_file_csv()

    def click_export(self):

        self.Export_Dialog = QtWidgets.QDialog()
        self.Export_Dialog.setStyleSheet("background-color: rgb(52, 61, 54);")

        export_layout = QtWidgets.QHBoxLayout(self.Export_Dialog)
        self.Export_Dialog.resize(400, 30)
        export_layout.setContentsMargins(10, 10, 10, 10)
        export_layout.setObjectName("box_layout")

        export_text = QtWidgets.QLabel(self.Export_Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        export_text.setFont(font)
        export_text.setStyleSheet("color: rgb(79, 103, 81);\n"
    "border-width: 0px;\n")

        export_text.setText("Filename:")

        self.export_entry = MyEntry(parent=self.Export_Dialog, master=self, function=self.click_export_ok)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(75)
        self.export_entry.setFont(font)
        self.export_entry.setFixedHeight(30)
        self.export_entry.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color: rgb(79, 103, 81);"
"border-color: rgb(79, 103, 81);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;")

        self.dropdown = QtWidgets.QComboBox(self.Export_Dialog)
        self.dropdown.addItems([".txt", ".csv"])
        self.dropdown.setStyleSheet("background-color: rgb(55, 72, 57);\n"
    "border-width: 1px;\n"
    "border-color: rgb(55, 72, 57);\n"
    )
        self.dropdown.setFixedHeight(30)
        self.dropdown.setFixedWidth(50)

        export_button = QtWidgets.QPushButton(self.Export_Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        export_button.setFont(font)
        export_button.setText("Export")
        export_button.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(55, 72, 57);}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        export_button.setFixedHeight(30)
        export_button.setFixedWidth(60)
        export_button.setDefault(True)
        export_button.clicked.connect(self.click_export_ok)
        export_button.clicked.connect(self.Export_Dialog.close)

        export_layout.addWidget(export_text)
        export_layout.addWidget(self.export_entry)
        export_layout.addWidget(self.dropdown)
        export_layout.addWidget(export_button)

        self.Export_Dialog.show()
        self.Export_Dialog.exec()

    def store_click_count(self):
        file2 = open("click_count.txt","w")
        file2.write(str(self.click_count_l) + " " + str(self.click_count_r) + " " + str(self.click_count_l_temp) + " " + str(self.click_count_r_temp))
        file2.close()

    def call_profile(self, title):
        call_profile = self.profiles[title](self, title)

    def add_profile_wrap(self):
        self.add_profile(self.entry.toPlainText())
        self.entry.clear()

    def add_profile(self, title):
        if title in self.profile_dict:
            self.error_2()
            return

        self.create_profile(title, 0)
        self.profile_dict[title] = self.profiles[title].counter

        self.add_frame(title)
        self.update_profile_count(title)

    def create_profile(self, title, counter):
        self.profiles[title] = CounterProfile(self, title, counter)

    def add_frame(self, title):
        self.frame_dict[title] = ProfileFrame(self, title)
        self.scroll.setWidget(self.group_box)
        self.form_layout.addRow(self.frame_dict[title].profile_frame_widget)

    def update_profile_count(self, title):
        self.profile_dict[title] = self.profiles[title].counter
        print(self.profile_dict)

        self.frame_dict[title].change_frame()

        self.file = open("profile_dict.txt","w")
        self.file.write(str(self.profile_dict))
        self.file.close()

    def del_frame(self, title):
        print(self.frame_dict[title])
        self.frame_dict[title].profile_frame_widget.deleteLater()
        self.frame_dict.pop(title)

    def del_profile(self, title):
        self.profile_dict.pop(title)
        self.profiles.pop(title)
        self.del_frame(title)

        self.file = open("profile_dict.txt","w")
        self.file.write(str(self.profile_dict))
        self.file.close()

    def sure(self):
        Sure_Dialog = QtWidgets.QDialog(self.centralwidget)
        Sure_Dialog.resize(400, 126)

        verticalLayout = QtWidgets.QVBoxLayout(Sure_Dialog)
        horizontalLayout = QtWidgets.QHBoxLayout(Sure_Dialog)

        button_ok = QtWidgets.QPushButton(Sure_Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        button_ok.setFont(font)
        button_ok.setFixedSize(80, 31)
        button_ok.setText("Yes")
        button_ok.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(41, 96, 125);\n"
"color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
        button_ok.clicked.connect(self.reset_all)
        button_ok.clicked.connect(Sure_Dialog.close)

        button_no = QtWidgets.QPushButton(Sure_Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        button_no.setFont(font)
        button_no.setFixedSize(80, 31)
        button_no.setText("No")
        button_no.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(41, 96, 125);\n"
"color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
        button_no.setDefault(True)
        button_no.clicked.connect(Sure_Dialog.close)

        sure_text = QtWidgets.QLabel(Sure_Dialog)
        sure_text.setGeometry(QtCore.QRect(0, 0, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        sure_text.setFont(font)
        sure_text.setStyleSheet("border-width: 0px;\n")
        sure_text.setAlignment(QtCore.Qt.AlignCenter)
        sure_text.setText("Are you sure you want to reset the click counter?")

        verticalLayout.addWidget(sure_text)
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout.addWidget(button_ok)
        horizontalLayout.addWidget(button_no)
        horizontalLayout.setAlignment(Qt.AlignCenter)
        Sure_Dialog.setWindowTitle("Sure?")

        Sure_Dialog.show()

    def sure_2(self):
        Sure_Dialog = QtWidgets.QDialog(self.centralwidget)
        Sure_Dialog.resize(400, 126)

        verticalLayout = QtWidgets.QVBoxLayout(Sure_Dialog)
        horizontalLayout = QtWidgets.QHBoxLayout(Sure_Dialog)

        button_ok = QtWidgets.QPushButton(Sure_Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        button_ok.setFont(font)
        button_ok.setFixedSize(80, 31)
        button_ok.setText("Yes")
        button_ok.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(41, 96, 125);\n"
"color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
        button_ok.clicked.connect(self.reset_all)
        button_ok.clicked.connect(Sure_Dialog.close)

        button_no = QtWidgets.QPushButton(Sure_Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        button_no.setFont(font)
        button_no.setFixedSize(80, 31)
        button_no.setText("No")
        button_no.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(41, 96, 125);\n"
"color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
        button_no.setDefault(True)
        button_no.clicked.connect(Sure_Dialog.close)

        sure_text = QtWidgets.QLabel(Sure_Dialog)
        sure_text.setGeometry(QtCore.QRect(0, 0, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        sure_text.setFont(font)
        sure_text.setStyleSheet("border-width: 0px;\n")
        sure_text.setAlignment(QtCore.Qt.AlignCenter)
        sure_text.setText("You are about to reset all your counts to 0!\nAre you sure you want to do that?")

        verticalLayout.addWidget(sure_text)
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout.addWidget(button_ok)
        horizontalLayout.addWidget(button_no)
        horizontalLayout.setAlignment(Qt.AlignCenter)
        Sure_Dialog.setWindowTitle("Sure?")

        Sure_Dialog.show()

    def error_2(self):

        Error_2_Dialog = QtWidgets.QDialog(self.centralwidget)
        Error_2_Dialog.resize(400, 126)

        verticalLayout = QtWidgets.QVBoxLayout(Error_2_Dialog)
        horizontalLayout = QtWidgets.QHBoxLayout(Error_2_Dialog)

        button_ok = QtWidgets.QPushButton(Error_2_Dialog)
        button_ok.setGeometry(QtCore.QRect(120, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        button_ok.setFont(font)
        button_ok.setFixedSize(QtCore.QSize(80, 31))
        button_ok.setText("OK")
        button_ok.setStyleSheet("QPushButton {background-color: rgb(41, 96, 125);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(41, 96, 125);\n"
"color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(30, 121, 177); color:rgb(0, 0, 0)}")
        button_ok.setDefault(True)
        button_ok.clicked.connect(Error_2_Dialog.close)

        error_2_text = QtWidgets.QLabel(Error_2_Dialog)
        error_2_text.setGeometry(QtCore.QRect(0, 0, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        error_2_text.setFont(font)
        error_2_text.setStyleSheet("border-width: 0px;\n")
        error_2_text.setAlignment(QtCore.Qt.AlignCenter)
        error_2_text.setText("Can't add! The Profile name already exists.\nChoose another name.")
        verticalLayout.addWidget(error_2_text)
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout.addWidget(button_ok)
        horizontalLayout.setAlignment(Qt.AlignCenter)
        Error_2_Dialog.setWindowTitle("Error!")

        Error_2_Dialog.show()

    #def dolphin(self):

    #    self.scroll.setStyleSheet("border-style: solid;\n"
#"border-width: 2px;\n"
#"border-radius: 10px;\n"
#"background-image: url(dolphin.png)")
    #    self.resize(776, 800)


    def info_window(self):
        info_Dialog = QtWidgets.QDialog(self.centralwidget)
        info_Dialog.resize(160, 80)
        info_Dialog.setWindowTitle("Info")
        print("Info")
        verticalLayout = QtWidgets.QVBoxLayout(info_Dialog)
        info_label = QtWidgets.QLabel(info_Dialog)
        info_label.move(10,10)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        info_label.setFont(font)
        info_label.setText("StuffCounter\nVersion: Qt-0.321\n2020-01-05")
        verticalLayout.addWidget(info_label)
        info_Dialog.show()

    def options(self, action):
        if action.text() == "Quit":
            self.hide()
            app.quit()
        if action.text() == "Info":
            self.info_window()
        if action.text() == "Reset all":
            self.sure_2()
        if action.text() == "Dolphin":
            self.dolphin()


app = QtWidgets.QApplication(sys.argv)
main_window = CounterApp()
main_window.trayIcon.show()
if main_window.cb_hide.isChecked():
    main_window.hide()
else:
    main_window.show()
main_window.setWindowTitle("Stuff Counter")

sys.exit(app.exec_())
