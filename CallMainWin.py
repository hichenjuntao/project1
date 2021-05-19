# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin import Ui_mainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win2 import secondWindow

class MyMainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.readButton.clicked.connect(self.msg)
        self.actionclose.triggered.connect(self.fuc3)
        self.actionactionopen.triggered.connect(self.openfile) #无功能
        self.setWindowIcon(QIcon('./images/cartoon1.ico'))



    def fuc2(self):
        print('fuc2')
        self.textEdit.setPlainText("fuc2")

    def fuc3(self):
        self.close()


    def win2show(self):
        #开启win2界面
        window2 = secondWindow(self)
        window2.setWindowOpacity(0.9)
        window2.show()

    def openfile(self):
        path = QFileDialog.getExistingDirectory(self,
                                                "选取文件夹")
        print(path)


    def msg(self):
        reply = QMessageBox.information(self, "提示", "这个功能暂时用不到", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.No )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())





