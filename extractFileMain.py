import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from extractFileUI import Ui_MainWindow
import shutil


class extractFileMain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(extractFileMain, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./images/cartoon2.ico'))
        self.chooseDirButton.clicked.connect(self.chooseDir)
        self.updateFileButton.clicked.connect(self.updateFileList)
        self.getSaveDirButton.clicked.connect(self.getSaveDir)
        self.extractButton.clicked.connect(self.extractMain)



    def chooseDir(self):
        sourceDir = QFileDialog.getExistingDirectory(self,"选取文件夹")
        if sourceDir != "":
            self.sourceDir = sourceDir
            self.updateProjectList()
            print(self.sourceDir)

    def updateProjectList(self):
        projects = os.listdir(self.sourceDir)
        self.projectWidgets = []
        for project in projects:
            print(project)
            path = self.sourceDir + "/" + project
            if os.path.isdir(path):
                item = QListWidgetItem()
                widget = QCheckBox(project)
                self.projectWidgets.append(widget)
                self.ProjectList.addItem(item)
                self.ProjectList.setItemWidget(item, widget)

    def updateFileList(self):
        self.fileWidgets = []
        for i in range(len(self.projectWidgets)):
            widget = self.projectWidgets[i]
            if widget.isChecked():
                path = self.sourceDir + "/%s" % widget.text()
                fileNames = os.listdir(path)
                for fileName in fileNames:
                    item = QListWidgetItem()
                    widget = QCheckBox(fileName)
                    self.fileWidgets.append(widget)
                    self.fileList.addItem(item)
                    self.fileList.setItemWidget(item, widget)
                break

    def getSaveDir(self):
        saveDir = QFileDialog.getExistingDirectory(self, "选取保存文件夹")
        if saveDir != "":
            self.saveDir = saveDir
            self.saveDirShow.setText(self.saveDir)
            self.saveDirShow.update()

    def extractMain(self):
        for i in range(len(self.projectWidgets)):
            if self.projectWidgets[i].isChecked():
                saveDir = self.saveDir + "/%s" % self.projectWidgets[i].text()
                print(saveDir)
                os.makedirs(saveDir, exist_ok=True)
                for j in range(len(self.fileWidgets)):
                    if self.fileWidgets[j].isChecked():
                        sourcePath = self.sourceDir + "/%s/%s" % (self.projectWidgets[i].text(), self.fileWidgets[j].text())
                        targetPath = saveDir + "/%s" % self.fileWidgets[j].text()
                        print(sourcePath)
                        print(targetPath)
                        shutil.copy(sourcePath, targetPath)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = extractFileMain()
    myWin.show()
    sys.exit(app.exec_())
