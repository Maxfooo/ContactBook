# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContactBook.ui'
#
# Created: Mon Sep  1 15:04:29 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ContactsTab = QtWidgets.QTabWidget(self.centralwidget)
        self.ContactsTab.setGeometry(QtCore.QRect(10, 10, 631, 181))
        self.ContactsTab.setObjectName("ContactsTab")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.contactBookComboBox = QtWidgets.QComboBox(self.tab_3)
        self.contactBookComboBox.setGeometry(QtCore.QRect(10, 40, 181, 22))
        self.contactBookComboBox.setMaxVisibleItems(5)
        self.contactBookComboBox.setObjectName("contactBookComboBox")
        self.openContactBookLabel = QtWidgets.QLabel(self.tab_3)
        self.openContactBookLabel.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.openContactBookLabel.setMouseTracking(False)
        self.openContactBookLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.openContactBookLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.openContactBookLabel.setObjectName("openContactBookLabel")
        self.addBookLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.addBookLineEdit.setGeometry(QtCore.QRect(220, 10, 181, 20))
        self.addBookLineEdit.setObjectName("addBookLineEdit")
        self.addBookBtn = QtWidgets.QPushButton(self.tab_3)
        self.addBookBtn.setGeometry(QtCore.QRect(220, 39, 91, 23))
        self.addBookBtn.setObjectName("addBookBtn")
        self.deleteBookBtn = QtWidgets.QPushButton(self.tab_3)
        self.deleteBookBtn.setGeometry(QtCore.QRect(429, 119, 91, 23))
        self.deleteBookBtn.setObjectName("deleteBookBtn")
        self.DeleteBookTextBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.DeleteBookTextBrowser.setGeometry(QtCore.QRect(430, 10, 181, 101))
        self.DeleteBookTextBrowser.setObjectName("DeleteBookTextBrowser")
        self.ContactsTab.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ContactTableView = QtWidgets.QTableView(self.tab)
        self.ContactTableView.setGeometry(QtCore.QRect(10, 10, 601, 101))
        self.ContactTableView.setObjectName("ContactTableView")
        self.DelBtn = QtWidgets.QPushButton(self.tab)
        self.DelBtn.setGeometry(QtCore.QRect(501, 119, 111, 23))
        self.DelBtn.setObjectName("DelBtn")
        self.SearchLineEdit = QtWidgets.QLineEdit(self.tab)
        self.SearchLineEdit.setGeometry(QtCore.QRect(10, 120, 181, 21))
        self.SearchLineEdit.setObjectName("SearchLineEdit")
        self.SearchBtn = QtWidgets.QPushButton(self.tab)
        self.SearchBtn.setGeometry(QtCore.QRect(199, 119, 111, 23))
        self.SearchBtn.setObjectName("SearchBtn")
        self.ContactsTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.FNameLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.FNameLineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.FNameLineEdit.setObjectName("FNameLineEdit")
        self.LNameLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.LNameLineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.LNameLineEdit.setObjectName("LNameLineEdit")
        self.PNumLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.PNumLineEdit.setGeometry(QtCore.QRect(250, 30, 113, 20))
        self.PNumLineEdit.setObjectName("PNumLineEdit")
        self.EmailLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.EmailLineEdit.setGeometry(QtCore.QRect(370, 30, 113, 20))
        self.EmailLineEdit.setObjectName("EmailLineEdit")
        self.AddressLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.AddressLineEdit.setGeometry(QtCore.QRect(490, 30, 113, 20))
        self.AddressLineEdit.setObjectName("AddressLineEdit")
        self.FNameLabel = QtWidgets.QLabel(self.tab_2)
        self.FNameLabel.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.FNameLabel.setObjectName("FNameLabel")
        self.LNameLabel = QtWidgets.QLabel(self.tab_2)
        self.LNameLabel.setGeometry(QtCore.QRect(130, 10, 111, 16))
        self.LNameLabel.setObjectName("LNameLabel")
        self.EmailLabel = QtWidgets.QLabel(self.tab_2)
        self.EmailLabel.setGeometry(QtCore.QRect(370, 10, 111, 16))
        self.EmailLabel.setObjectName("EmailLabel")
        self.PNumLabel = QtWidgets.QLabel(self.tab_2)
        self.PNumLabel.setGeometry(QtCore.QRect(250, 10, 111, 16))
        self.PNumLabel.setObjectName("PNumLabel")
        self.AddressLabel = QtWidgets.QLabel(self.tab_2)
        self.AddressLabel.setGeometry(QtCore.QRect(490, 10, 111, 16))
        self.AddressLabel.setObjectName("AddressLabel")
        self.SaveBtn = QtWidgets.QPushButton(self.tab_2)
        self.SaveBtn.setGeometry(QtCore.QRect(10, 60, 111, 23))
        self.SaveBtn.setObjectName("SaveBtn")
        self.ContactsTab.addTab(self.tab_2, "")
        self.helpWindowTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.helpWindowTextBrowser.setGeometry(QtCore.QRect(10, 200, 631, 61))
        self.helpWindowTextBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.helpWindowTextBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.helpWindowTextBrowser.setObjectName("helpWindowTextBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWritten_by = QtWidgets.QMenu(self.menuFile)
        self.menuWritten_by.setObjectName("menuWritten_by")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionMax_A_Ruiz = QtWidgets.QAction(MainWindow)
        self.actionMax_A_Ruiz.setObjectName("actionMax_A_Ruiz")
        self.menuWritten_by.addAction(self.actionMax_A_Ruiz)
        self.menuFile.addAction(self.menuWritten_by.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.ContactsTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openContactBookLabel.setText(_translate("MainWindow", "Currently Open Contact Book"))
        self.addBookBtn.setText(_translate("MainWindow", "Add Book"))
        self.deleteBookBtn.setText(_translate("MainWindow", "Delete Book"))
        self.ContactsTab.setTabText(self.ContactsTab.indexOf(self.tab_3), _translate("MainWindow", "Contact Book"))
        self.DelBtn.setText(_translate("MainWindow", "Delete"))
        self.SearchBtn.setText(_translate("MainWindow", "Search"))
        self.ContactsTab.setTabText(self.ContactsTab.indexOf(self.tab), _translate("MainWindow", "Contacts"))
        self.FNameLabel.setText(_translate("MainWindow", "First Name"))
        self.LNameLabel.setText(_translate("MainWindow", "Last Name"))
        self.EmailLabel.setText(_translate("MainWindow", "Email"))
        self.PNumLabel.setText(_translate("MainWindow", "Phone Number"))
        self.AddressLabel.setText(_translate("MainWindow", "Address"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
        self.ContactsTab.setTabText(self.ContactsTab.indexOf(self.tab_2), _translate("MainWindow", "Add"))
        self.menuFile.setTitle(_translate("MainWindow", "Contact Book"))
        self.menuWritten_by.setTitle(_translate("MainWindow", "&Written by . . ."))
        self.actionHelp.setText(_translate("MainWindow", "&Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionMax_A_Ruiz.setText(_translate("MainWindow", "Max A. Ruiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

