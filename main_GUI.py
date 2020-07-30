from PyQt5 import QtCore, QtGui, QtWidgets
from ListView_Form import ListView_Form
from Parsing_Form import Parsing_Form
import sys

class Ui_MainWindow(object):
    def setupUi(self):
        self.windoObj= QtWidgets.QMainWindow()
        self.parsing = Parsing_Form()
        self.ParsingWindow= QtWidgets.QMainWindow()
        self.list_view = ListView_Form()
        self.listWindow= QtWidgets.QMainWindow()
        
        self.windoObj.setObjectName("MainWindow")
        self.windoObj.resize(560, 260)
        self.centralwidget = QtWidgets.QWidget(self.windoObj)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(45, 80, 220, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.parsingGo)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(285, 80, 220, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.listViewGo)
        self.windoObj.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.windoObj)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 18))
        self.menubar.setObjectName("menubar")
        self.windoObj.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.windoObj)
        self.statusbar.setObjectName("statusbar")
        self.windoObj.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.windoObj)
        self.windoObj.show()
        self.listWindow.hide()
        self.ParsingWindow.hide()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.windoObj.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Parsing lecture proposal"))
        self.pushButton_2.setText(_translate("MainWindow", "show lecture score"))

    def parsingGo(self):
        self.parsing.setupUi(self.ParsingWindow, self.windoObj)
        self.windoObj.hide()
        self.listWindow.hide()
        self.ParsingWindow.show()


    def listViewGo(self):
        self.list_view.setupUi(self.listWindow, self.windoObj)
        self.windoObj.hide()
        self.listWindow.show()
        self.ParsingWindow.hide()   

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    sys.exit(app.exec_())

