from PyQt5 import QtCore, QtGui, QtWidgets
from coursePlanParser import *
from selenium import webdriver

class Parsing_Form(object):
    def setupUi(self, Form, QMainWindow):
        self.windoObj=QMainWindow
        self.ParsingWindow=Form
        
        Form.setObjectName("Form")
        Form.resize(425, 360)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 60, 80, 20))
        self.label.setObjectName("label")        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 80, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 80, 20))
        self.label_3.setObjectName("label_3")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 280, 100, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pasing)#
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 280, 100, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.mainPageGo)#
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 260, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 110, 260, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) 
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 170, 260, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Stu_ID :"))
        self.label_2.setText(_translate("Form", "PW :"))
        self.label_3.setText(_translate("Form", "url :"))
        self.pushButton.setText(_translate("Form", "parsing"))
        self.pushButton_2.setText(_translate("Form", "Back"))
    
    def mainPageGo(self):
        self.ParsingWindow.hide()
        self.windoObj.show()
    def pasing(self):
        url=self.lineEdit_3.text()
        stu_id=self.lineEdit.text()
        stu_pw=self.lineEdit_2.text()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        browser=login(driver,stu_id,stu_pw)
        parsingWithURL(browser,url)
        browser.implicitly_wait(5)
        driver.quit()
        self.mainPageGo()


