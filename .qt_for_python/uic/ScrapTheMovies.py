# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Aadi\Documents\GitHub\CS261F21PID19\ScrapTheMovies.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 604)
        MainWindow.setStyleSheet("background-color:rgb(54, 54, 54)")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 30, 201, 571))
        self.frame.setStyleSheet("background-color:rgb(56, 56, 56)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 210, 70, 17))
        self.checkBox.setStyleSheet("color:white")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 210, 70, 17))
        self.checkBox_2.setStyleSheet("color:white")
        self.checkBox_2.setObjectName("checkBox_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 270, 171, 22))
        self.comboBox.setStyleSheet("color:black;\n"
"background-color:white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 310, 101, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 340, 171, 22))
        self.comboBox_2.setStyleSheet("color:black;\n"
"background-color:white;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 380, 171, 22))
        self.comboBox_3.setStyleSheet("color:black;\n"
"background-color:white;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 520, 181, 23))
        self.progressBar.setStyleSheet("color:white\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 100, 211, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 500, 211, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 550, 141, 16))
        self.label_5.setObjectName("label_5")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(210, 110, 691, 431))
        self.tableView.setStyleSheet("border:none;")
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 420, 141, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   background-color:rgb(209, 209, 209);\n"
"    border: none;\n"
"   color: black;\n"
"    border-radius:10px;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(254, 254, 254);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 470, 141, 23))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   background-color:rgb(209, 209, 209);\n"
"    border: none;\n"
"   color: black;\n"
"    border-radius:10px;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(254, 254, 254);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(0, 450, 211, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.startbutton = QtWidgets.QPushButton(self.frame)
        self.startbutton.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.startbutton.setStyleSheet("QPushButton {\n"
"   background-color:rgb(255, 242, 99);\n"
"    border: none;\n"
"   color: black;\n"
"    border-radius:10px;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(254, 254, 254);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.startbutton.setObjectName("startbutton")
        self.startbutton_2 = QtWidgets.QPushButton(self.frame)
        self.startbutton_2.setGeometry(QtCore.QRect(110, 50, 91, 23))
        self.startbutton_2.setStyleSheet("QPushButton {\n"
"   background-color:rgb(255, 242, 99);\n"
"    border: none;\n"
"   color: black;\n"
"    border-radius:10px;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(254, 254, 254);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.startbutton_2.setObjectName("startbutton_2")
        self.startbutton_3 = QtWidgets.QPushButton(self.frame)
        self.startbutton_3.setGeometry(QtCore.QRect(10, 80, 191, 23))
        self.startbutton_3.setStyleSheet("QPushButton {\n"
"   background-color:rgb(255, 242, 99);\n"
"    border: none;\n"
"   color: black;\n"
"    border-radius:10px;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(254, 254, 254);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.startbutton_3.setObjectName("startbutton_3")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(20, 150, 71, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 180, 141, 23))
        self.lineEdit_2.setStyleSheet("background-color:white;\n"
"color:black;\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 180, 41, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   background-color:rgb(85, 85, 255);\n"
"    border: none;\n"
"   color: black;\n"
"    border-radius:10px;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(254, 254, 254);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.lineEdit_6.setStyleSheet("background-color:white;\n"
"color:black;\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(20, 0, 71, 20))
        self.label_14.setObjectName("label_14")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(200, 10, 21, 621))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(210, 105, 701, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 70, 51, 41))
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(700, 80, 71, 22))
        self.comboBox_4.setStyleSheet("background-color:white;\n"
"color:black")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 80, 141, 23))
        self.lineEdit.setStyleSheet("background-color:white;\n"
"color:black;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(790, 50, 101, 22))
        self.comboBox_7.setStyleSheet("color:black;\n"
"background-color:white;")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(790, 80, 101, 22))
        self.comboBox_8.setStyleSheet("color:black;\n"
"background-color:white;")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(900, 30, 71, 51))
        self.checkBox_3.setStyleSheet("color:white")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(900, 60, 70, 31))
        self.checkBox_4.setStyleSheet("color:white")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(900, 80, 70, 31))
        self.checkBox_5.setStyleSheet("color:white")
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 10, 181, 16))
        self.label_6.setObjectName("label_6")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(460, 10, 21, 121))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 40, 41, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 70, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(400, 90, 61, 20))
        self.label_9.setObjectName("label_9")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, -10, 911, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(920, 10, 51, 23))
        self.closebutton.setStyleSheet("QPushButton {\n"
"   background-color:rgb(255, 255, 255);\n"
"    border: none;\n"
"    border-radius:10px;\n"
"    color: black;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(255, 7, 11);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.closebutton.setObjectName("closebutton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 10, 51, 23))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   background-color:rgb(255, 255, 255);\n"
"    border: none;\n"
"    border-radius:10px;\n"
"    color: black;\n"
"    font:bold-arial;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(162, 162, 162)\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(210, 130, 751, 411))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"\n"
"background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(530, 20, 181, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(690, 40, 81, 20))
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 560, 191, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
"   background-color:rgb(85, 85, 255);\n"
"    border: none;\n"
"   color: black;\n"
"    border-radius:10px;\n"
"    font:arial;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(254, 254, 254);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 68);\n"
"   color : rgb(121, 111, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 40, 141, 23))
        self.lineEdit_3.setStyleSheet("background-color:white;\n"
"color:black;\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 90, 141, 23))
        self.lineEdit_4.setStyleSheet("background-color:white;\n"
"color:black;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(540, 40, 141, 23))
        self.lineEdit_5.setStyleSheet("background-color:white;\n"
"color:black;\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Sort By:</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Ascending"))
        self.checkBox_2.setText(_translate("MainWindow", "Decending"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Selection Sort"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Insertion Sort"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Quick Sort"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Merge Sort"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Bubble Sort"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Hybird Sort"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Tree Sort"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Cocktail Sort"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Select Algorithm :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Select Columns :</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Title"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Duration"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Year"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Genre"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Rating"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Director"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Cast"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Synop"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Title"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Genre"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Rating"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Year"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Time"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Cast"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Director"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Data is Scraping</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Sort"))
        self.pushButton_5.setText(_translate("MainWindow", "View Stats"))
        self.startbutton.setText(_translate("MainWindow", "Start"))
        self.startbutton_2.setText(_translate("MainWindow", "Pause"))
        self.startbutton_3.setText(_translate("MainWindow", "Cancel"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Import_File</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Ok"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Pages to scrap</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Search :</span></p></body></html>"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Start with"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Ends with"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Title"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Genre"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Rating"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Year"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Time"))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "Cast"))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "Director"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Title"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Genre"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Rating"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Year"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "Time"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "Cast"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "Director"))
        self.checkBox_3.setText(_translate("MainWindow", "AND"))
        self.checkBox_4.setText(_translate("MainWindow", "OR"))
        self.checkBox_5.setText(_translate("MainWindow", "NOT"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Time Taken While Scrapping:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Mints</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Movies Scraped :</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Identities</span></p></body></html>"))
        self.closebutton.setText(_translate("MainWindow", "X"))
        self.pushButton_4.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Releasing Year"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Director"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cast"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Synoip"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Scrap The Movies</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Time Taken While Searching:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Mints</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Save File"))