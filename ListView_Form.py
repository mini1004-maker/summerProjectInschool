from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

column_idx_lookup = {'courseName': 0, 'classInfo': 1, 'professor': 2}


class ListView_Form(object):
    def __init__(self):
        self.tableMap={
            'courseName':[],
            'classInfo':[],
            'professor':[]
        }
        super().__init__()
        
    def setupUi(self, Form, QMainWindow):
        self.windoObj=QMainWindow
        self.ParsingWindow=Form
        Form.setObjectName("Form")
        Form.resize(475, 800)
        
        self.tableView = QtWidgets.QTableWidget(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 425, 720))
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(225, 750, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predict)
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(345, 750, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.mainPageGo)        

        
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.setTableWidgetData()
        self.retranslateUi(Form)
        
    def loadData(self):
        import glob 
        files = glob.glob('*.txt')
        for file in files:
            with open(file, 'r') as f:
                element_txt=f.read().split(';')
                self.tableMap['courseName'].append(element_txt[1].strip())
                self.tableMap['classInfo'].append(element_txt[7].strip())
                self.tableMap['professor'].append(element_txt[21].strip())

    def setTableWidgetData(self):
        column_headers = ['과목명', '분반', '교수']
        self.loadData()
        self.tableView.setRowCount(len(self.tableMap['courseName']))
        self.tableView.setColumnCount(3)
        self.tableView.setHorizontalHeaderLabels(column_headers)
        
        
        
        for k, v in self.tableMap.items():
            col = column_idx_lookup[k]

            for row, val in enumerate(v):
                item = QtWidgets.QTableWidgetItem(val)

                self.tableView.setItem(row, col, item)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "predict"))
        self.pushButton_2.setText(_translate("Form", "Back"))

    def mainPageGo(self):
        self.ParsingWindow.hide()
        self.windoObj.show()

    def predict(self):
        txtName=""
        cnt=0
        for r in self.tableView.selectedItems():
            if(cnt<2):
                txtName=txtName+str(r.text())
            cnt+=1
        print(txtName)
