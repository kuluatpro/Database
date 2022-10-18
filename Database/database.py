# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:06:53 2022

@author: ADMIN
"""

from distutils.util import execute
from sqlite3 import Cursor
import mysql.connector




from PyQt5 import QtCore, QtGui, QtWidgets

class database():
    def __init__(self, method):
        self.get_database
        self.method = method

    def get_database(self):
        

        return 
    






class Ui_MainWindow(database):

    def display_database(self, MainWindow):
        # warnings = self.get_database()
        
        for  row in range(10):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem('str(warnings[0]'))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem('str(warnings[1])'))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem('str(warnings[2])'))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem('str(warnings[3])'))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem('str(warnings[4])'))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem('str(warnings[5])'))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem('str(warnings[6])'))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 808)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Search_bar = QtWidgets.QTextEdit(self.centralwidget)
        self.Search_bar.setGeometry(QtCore.QRect(30, 20, 671, 21))
        self.Search_bar.setObjectName("Search_bar")
        self.Filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Filter_btn.setGeometry(QtCore.QRect(710, 20, 75, 24))
        self.Filter_btn.setObjectName("Filter_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 1061, 651))
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
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
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Filter_btn.setText(_translate("MainWindow", "Filter"))
        item = self.tableWidget.horizontalHeaderItem(0)
        self.tableWidget.setColumnWidth(0, 100)
        item.setText(_translate("MainWindow", "Defect ID"))

        item = self.tableWidget.horizontalHeaderItem(1)
        self.tableWidget.setColumnWidth(1, 459)
        item.setText(_translate("MainWindow", "Code Line"))

        item = self.tableWidget.horizontalHeaderItem(2)
        self.tableWidget.setColumnWidth(2, 100)
        item.setText(_translate("MainWindow", "Line in Source"))

        item = self.tableWidget.horizontalHeaderItem(3)
        self.tableWidget.setColumnWidth(3, 100)
        item.setText(_translate("MainWindow", "Function Name"))

        item = self.tableWidget.horizontalHeaderItem(4)
        self.tableWidget.setColumnWidth(4, 100)
        
        item.setText(_translate("MainWindow", "Warning Prio"))

        item = self.tableWidget.horizontalHeaderItem(5)
        self.tableWidget.setColumnWidth(5, 100)
        item.setText(_translate("MainWindow", "User ID"))

        item = self.tableWidget.horizontalHeaderItem(6)
        self.tableWidget.setColumnWidth(6, 100)
        item.setText(_translate("MainWindow", "Task ID"))

        for  row in range(10):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem('str(warnings[0]'))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem('str(warnings[1])'))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem('str(warnings[2])'))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem('str(warnings[3])'))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem('str(warnings[4])'))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem('str(warnings[5])'))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem('str(warnings[6])'))
        # self.display_database(MainWindow)




if __name__ == "__main__":
    import sys

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MidNightSun2022",
            database="db"
            )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM warnings")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    

    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)

    # MainWindow.show()
    # sys.exit(app.exec_())




# insert into users(user_id, rights) values ('tlr6hc', 'write');
# insert into task(task_id, pver_name, oem) values ('A0000', 'wwwwwwwwwwwwwww', 'Audi');

# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("thi7hc", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("sadh3n", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("ajd7ds", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("chn6as", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("hsays9", "write"))
# cursor.execute("insert into users(user_id, rights) values (%s,%s)", ("akd8w2", "write"))


# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0001', 'the_lords_of_the_rings', 'BMW');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0002', 'house_of_dragons', 'Aston');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0003', 'avengers_infinity_war', 'General');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0004', 'beauty_and_the_beast', 'Ford');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0005', 'she_hulk', 'Mercedes');")
# cursor.execute("insert into task(task_id, pver_name, oem) values ('A0006', 'spider_man_far_from_home', 'Volvo');")


# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('lashdlewnsadsad', 533, 'dabong', 'low', 'tlr6hc', 'A0000');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('sauefn dvysdfnw', 551, 'bongchay', 'low', 'sadh3n', 'A0001');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('sdfnkqwfosadosd', 533, 'dabong', 'high', 'tlr6hc', 'A0002');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('cyew fovasbdsus', 674, 'dabong', 'low', 'tlr6hc', 'A0003');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asuiefr cfpsdna', 975, 'dabong', 'high', 'chn6as', 'A0000');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asd7efbwdtyqdbq', 533, 'dabong', 'low', 'tlr6hc', 'A0004');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asdojweofbdhsvj', 216, 'bongro', 'low', 'hsays9', 'A0000');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('ascoadsalskfnw7', 533, 'dabong', 'high', 'tlr6hc', 'A0005');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('wq0943ihfsfknaf', 587, 'bongbauduc', 'low', 'tlr6hc', 'A0000');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asdiq39sdfq,ljd', 533, 'dabong', 'high', 'akd8w2', 'A0006');")
# cursor.execute("insert into warnings (code_line, line_in_source, function_name, warning_prio, user_id, task_id) values ('asdhbjewgfbjw7d', 034, 'dabong', 'low', 'tlr6hc', 'A0000');")




