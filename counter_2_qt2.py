from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import sys
from counter_main_window import Ui_MainWindow
from counterprofile1 import CounterProfile
from profile_frame_widget import ProfileFrame


class CounterApp(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        super().retranslateUi(MainWindow)

        self.add.clicked.connect(self.add_profile_wrap)

        self.click.clicked[bool].connect(self.click_counter)

        #open click counts on startup
        file2 = open("click_count.txt","r")
        click_count_list = file2.read().split(" ")
        self.click_count_l = int(click_count_list[0])
        self.click_count_r = int(click_count_list[1])
        self.click_count_l_temp = int(click_count_list[2])
        self.click_count_r_temp = int(click_count_list[3])

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
        file3 = open("state.txt","r")
        file3_str = file3.read()


    def click_counter(self, activated):
        if activated:
            print("activated!!!")
            self.click.setText("Deactivate Click Counter")
            self.click.setStyleSheet("QPushButton {background-color: rgb(125, 45, 76);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(125, 45, 76);}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(125, 45, 76)}")
            self.statusbar.showMessage("All your clicks are being counted")

        else:
            print("deactivated!!!")
            self.click.setText("Activate Click Counter")
            self.click.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(55, 72, 57);}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
            self.statusbar.showMessage("")

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

    def error_2(self):

        self.Error_2_Dialog = QtWidgets.QDialog()
        self.Error_2_Dialog.resize(400, 126)
        self.Error_2_Dialog.setStyleSheet("background-color: rgb(52, 61, 54);")

        botton_ok = QtWidgets.QPushButton(self.Error_2_Dialog)
        botton_ok.setGeometry(QtCore.QRect(120, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        botton_ok.setFont(font)
        botton_ok.setText("OK")
        botton_ok.setStyleSheet("QPushButton {background-color: rgb(55, 72, 57);\n"
    "border-style: outset;\n"
    "border-width: 1px;\n"
    "border-radius: 10px;\n"
    "border-color: rgb(55, 72, 57);}\n"
    "QPushButton:pressed {border-style: solid; background-color:  rgb(65, 85, 67)}")
        botton_ok.setDefault(True)
        botton_ok.clicked.connect(self.Error_2_Dialog.close)

        error_2_text = QtWidgets.QLabel(self.Error_2_Dialog)
        error_2_text.setGeometry(QtCore.QRect(0, 0, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        error_2_text.setFont(font)
        error_2_text.setStyleSheet("color: rgb(79, 103, 81);\n"
        "border-style: flat;\n"
        "border-width: 0px;\n"
        "border-radius: 0px;\n"
        "border-width: 0px;\n"
        "")
        error_2_text.setAlignment(QtCore.Qt.AlignCenter)
        error_2_text.setText("Can't add! The Profile name already exists.\nChoose another name.")


        self.Error_2_Dialog.show()
        self.Error_2_Dialog.exec()





app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
main_window = CounterApp(MainWindow)
#main_window.setupUi(MainWindow)
MainWindow.show()
MainWindow.setWindowTitle("Stuff Counter")


sys.exit(app.exec_())
