# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainUI import Ui_mainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fieRenameMain import fileRenameMain
from extractFileMain import extractFileMain

class MyMainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionclose.triggered.connect(self.closeMainWin)
        self.renameButton.clicked.connect(self.renameMain)
        self.extractFileButton.clicked.connect(self.extractFileMain)
        self.setWindowIcon(QIcon('./images/cartoon1.ico'))



    def closeMainWin(self):
        self.close()


    def renameMain(self):
        #开启win2界面
        renameWindow = fileRenameMain(self)
        renameWindow.setWindowOpacity(0.9)  # 设置透明度
        renameWindow.show()


    def extractFileMain(self):
        extractFileWindow = extractFileMain(self)
        extractFileWindow.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())





