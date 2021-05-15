# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  pyqtSlot, pyqtSignal,Qt

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(600, 500)
        mainWindow.setMinimumSize(QtCore.QSize(600, 500))
        mainWindow.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 230, 510, 200))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 201, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.readButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.readButton.setEnabled(True)
        self.readButton.setObjectName("readButton")
        self.verticalLayout.addWidget(self.readButton)
        self.renameButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.renameButton.setObjectName("renameButton")
        self.verticalLayout.addWidget(self.renameButton)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionclose = QtWidgets.QAction(mainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionactionopen = QtWidgets.QAction(mainWindow)
        self.actionactionopen.setObjectName("actionactionopen")
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.actionactionopen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionclose)
        self.actionclose.triggered.connect(mainWindow.close)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        self.renameButton.clicked.connect(self.win2show)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "文件处理工具"))
        self.readButton.setText(_translate("mainWindow", "文件读取"))
        self.renameButton.setText(_translate("mainWindow", "批量改名"))
        self.menu.setTitle(_translate("mainWindow", "菜单"))
        self.actionclose.setText(_translate("mainWindow", "退出"))
        self.actionactionopen.setText(_translate("mainWindow", "打开文件"))
        self.actionactionopen.setToolTip(_translate("mainWindow", "打开文件"))
        self.actionactionopen.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.action.setText(_translate("mainWindow", "改名"))



