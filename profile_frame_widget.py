# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile_frame_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 126)
        Dialog.setStyleSheet("background-color: rgb(52, 61, 54);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 70, 151, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 30, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(79, 103, 81);\n"
"border-style: flat;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-width: 0px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sure?"))
        self.label.setText(_translate("Dialog", "Are you sure you want to delete this profile?"))

class Ui_profile_frame_widget(object):
    def setupUi(self, profile_frame_widget):
        profile_frame_widget.setObjectName("profile_frame_widget")
        profile_frame_widget.resize(540, 31)
        profile_frame_widget.setFixedHeight(31)
        profile_frame_widget.setAccessibleName("")
        profile_frame_widget.setStyleSheet("border-color: rgb(79, 103, 81);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"background-color: rgb(79, 103, 81);")
        self.label_5 = QtWidgets.QLabel(profile_frame_widget)
        self.label_5.setGeometry(QtCore.QRect(10, 4, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAccessibleName("")
        self.label_5.setStyleSheet("color: rgb(52, 61, 54);\n"
"border-style: flat;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-width: 0px;\n"
"")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.count_label = QtWidgets.QLabel(profile_frame_widget)
        self.count_label.setGeometry(QtCore.QRect(290, 4, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.count_label.setFont(font)
        self.count_label.setAccessibleName("")
        self.count_label.setStyleSheet("color: rgb(52, 61, 54);\n"
"border-style: flat;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-width: 0px;\n"
"")
        self.count_label.setTextFormat(QtCore.Qt.AutoText)
        self.count_label.setObjectName("count_label")
        self.delete = QtWidgets.QPushButton(profile_frame_widget)
        self.delete.setGeometry(QtCore.QRect(380, 4, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.delete.setFont(font)
        self.delete.setAccessibleName("")
        self.delete.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        self.delete.setObjectName("delete")
        self.open = QtWidgets.QPushButton(profile_frame_widget)
        self.open.setGeometry(QtCore.QRect(460, 4, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.open.setFont(font)
        self.open.setAccessibleName("")
        self.open.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgb(55, 72, 57);}\n"
"QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        self.open.setObjectName("open")

        self.retranslateUi(profile_frame_widget)
        QtCore.QMetaObject.connectSlotsByName(profile_frame_widget)

    def retranslateUi(self, profile_frame_widget):
        _translate = QtCore.QCoreApplication.translate
        profile_frame_widget.setWindowTitle(_translate("profile_frame_widget", "Frame"))
        self.label_5.setText(_translate("profile_frame_widget", "title"))
        self.count_label.setText(_translate("profile_frame_widget", "count"))
        self.delete.setText(_translate("profile_frame_widget", "Delete"))
        self.open.setText(_translate("profile_frame_widget", "Open"))

class ProfileFrame(Ui_profile_frame_widget):

    def __init__(self, master, title):

        self.master = master
        self.title = title
        self.profile_frame_widget = QtWidgets.QFrame(master.frame_just_count)
        super().setupUi(self.profile_frame_widget)
        super().retranslateUi(self.profile_frame_widget)
        self.change_frame()
        self.delete.clicked.connect(self.sure)
        self.open.clicked.connect(self.call_profile_wrap)


    def change_frame(self):
        self.label_5.setText(self.title)
        self.count_label.setText(str(self.master.profile_dict[self.title]))

    def call_profile_wrap(self):
        try:
            self.master.profiles[self.title].CounterWindow.close()
        except AttributeError:
            pass

        self.master.call_profile(self.title)

    def sure(self):
        self.Sure_Dialog = QtWidgets.QDialog()
        self.sure = Ui_Dialog()
        self.sure.setupUi(self.Sure_Dialog)
        self.sure.buttonBox.accepted.connect(self.del_profile_wrap)
        self.Sure_Dialog.show()
        self.Sure_Dialog.exec()


    def del_profile_wrap(self):
        self.master.del_profile(self.title)
        self.Sure_Dialog.close()
