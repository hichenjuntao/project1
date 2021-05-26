import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from renameWin import Ui_renameWindow
import shutil


class fileRenameMain(QMainWindow, Ui_renameWindow):
    def __init__(self, parent=None):
        super(fileRenameMain, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./images/cartoon2.ico'))
        self.pathButton.clicked.connect(self.openfile)
        self.readButton.clicked.connect(self.readfile)
        self.numberPB.clicked.connect(self.renameForNumber)  # 数字
        self.flagPB.clicked.connect(self.renameForFlag)   # 符号替换
        self.saveAsPB.clicked.connect(self.updateSaveFile)
        tip='使用方法：\n1：点击选取文件夹以选择文件所在地址\n2：后点击读取文件获取图片\n3：之后在左侧输入分隔符和索引位置\n4：完成后在右侧输入新的ID或分隔符点击按钮完成重命名操作\n'
        self.textBrowser.append(tip)

    def openfile(self):
        # global path
        self.sourceDir = QFileDialog.getExistingDirectory(self,"选取文件夹")
        if self.sourceDir != "":
            self.textBrowser.append('已选择文件所在路径为：'+self.sourceDir)
            self.textBrowser.append('请点击读取文件')
            self.saveDir = self.sourceDir
            self.saveDirShow.setText(self.sourceDir)
            print(self.sourceDir)



    def readfile(self):
        names = os.listdir(self.sourceDir)
        allSiffix = []
        self.typeCB.clear()
        self.typeCB.addItem('Dir')
        for name in names:
            siffix = name.split('.')[-1]
            if siffix not in allSiffix:
                allSiffix.append(siffix)
                self.typeCB.addItem(siffix)


    def renameNumber(self, oldName, oldFlag, oldIndex, begainID):
        oldName = oldName.split('.')[0]
        oldID = oldName.split(oldFlag)[oldIndex]
        newID = int(oldID) + begainID
        return str(newID)

    def renameForNumber(self):
        '''取新ID  新分隔符 组成新地址用于改名'''
        # 使用infomation信息框
        oldFlag = self.identifier.text()
        oldIndex = int(self.index.text())
        begainID = int(self.begainID.text())
        names = os.listdir(self.sourceDir)
        text = ''
        for name in names:
            if self.typeCB.currentText() in name:
                showname = self.renameNumber(name, oldFlag, oldIndex, begainID) + "." + self.typeCB.currentText()
                text = f'是否确认用如下格式修改文件名？\n{showname},只会修改选择的文件格式，点击YES选择输出目录'
                break
        reply = QMessageBox.information(self, "提示", text, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.textBrowser.append('确认操作')
            for name in names:
                if self.typeCB.currentText() in name:
                    print(name)
                    newname = self.renameNumber(name, oldFlag, oldIndex, begainID) + "." + self.typeCB.currentText()
                    print(newname)
                    newPath = os.path.join(self.saveDir, newname)
                    sourcePath = os.path.join(self.sourceDir, name)
                    if self.saveDir == self.sourceDir:
                        os.rename(sourcePath, newPath)
                    else:
                        shutil.copy(sourcePath, newPath)
                    # self.textBrowser.append(f'{adress[i]}已改名为{newpath}')
                # else:
                #     self.textBrowser.append(f'{adress[i]}未改名')
            self.textBrowser.append('改名完成!跳转至输出文件夹')
            # os.startfile(savepath)
        else:
            self.textBrowser.append('取消操作')

    def renamFlag(self, oldName, oldFlag, oldIndex, newFlag):
        # 需要优化
        num = 0
        for i in range(len(oldName)):
            if oldName[i] == oldFlag:
                if num == oldIndex:
                    newName = oldName[:i] + newFlag + oldName[i+1:len(oldName)]
                    print(oldName,oldFlag,oldIndex,newFlag,newName)
                    return newName
                num += 1
        return 'bug'


    def renameForFlag(self):
        # 使用infomation信息框
        oldFlag = self.identifier.text()
        oldIndex = int(self.index.text())
        newFlag = self.newFlag.text()
        names = os.listdir(self.sourceDir)
        text = ''
        for name in names:
            if self.typeCB.currentText() in name or self.typeCB.currentText() == "Dir":
                showname = self.renamFlag(name, oldFlag, oldIndex, newFlag)
                text = f'是否确认用如下格式修改文件名？\n{showname},只会修改选择的文件格式，点击YES选择输出目录'
                break
        reply = QMessageBox.information(self, "提示", text, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.textBrowser.append('确认操作')
            for name in names:
                if self.typeCB.currentText() in name or self.typeCB.currentText() == "Dir":
                    newName = self.renamFlag(name, oldFlag, oldIndex, newFlag)
                    print(newName)
                    newPath = os.path.join(self.saveDir, newName)
                    sourcePath = os.path.join(self.sourceDir, name)
                    if self.saveDir == self.sourceDir or self.typeCB.currentText() == "Dir":
                        os.rename(sourcePath, newPath)
                    else:
                        shutil.copy(sourcePath, newPath)
                    # self.textBrowser.append(f'{adress[i]}已改名为{newpath}')
                # else:
                #     self.textBrowser.append(f'{adress[i]}未改名')
            self.textBrowser.append('改名完成!跳转至输出文件夹')
            # os.startfile(savepath)
        else:
            self.textBrowser.append('取消操作')


    # def msg(self):
    #     # 使用infomation信息框
    #     id = self.ID.text()
    #     newidentifier = self.newidentifier.text()
    #     newname=id+newidentifier+number[0]+siffix[0]
    #     text=f'是否确认用如下格式修改文件名？\n{newname},只会修改选择的文件格式，点击YES选择输出目录'
    #     reply = QMessageBox.information(self, "提示", text, QMessageBox.Yes | QMessageBox.No ,  QMessageBox.No )
    #     print(reply,type(reply))
    #     if reply==QMessageBox.Yes:
    #         self.textBrowser.append('确认操作')
    #         self.rename()
    #     else:
    #         self.textBrowser.append('取消操作')


    def updateSaveFile(self):
        saveDir = QFileDialog.getExistingDirectory(self, "选取保存路径文件夹")
        if saveDir != "":
            self.saveDirShow.setText(saveDir)
            self.saveDir = saveDir





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = fileRenameMain()
    myWin.show()
    sys.exit(app.exec_())
