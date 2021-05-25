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
        #self.sortButton.clicked.connect(self.segmentname)
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

        # global filenames,adress,siffix_key,siffix_values,siffix
        # #文件读取
        # adress=[]
        # self.textBrowser.append('读取文件名称：')
        # for dirpath, dirnames, filenames in os.walk(self.sourceDir):
        #     for filename in filenames:
        #         #self.textBrowser.append(os.path.join(dirpath, filename))
        #         self.textBrowser.append(filename)
        #         self.textBrowser.ensureCursorVisible()
        #         adress.append(os.path.join(dirpath, filename))
        # self.textBrowser.append(f'读取成功！共读取图片{len(filenames)}张')
        # text='''分隔符与index填写提示：\n文件110104_5fbdbae0cd2de.jpg，以'_'分割时→['110104','5fbdbae0cd2de']，在index中输入其编号位置i，注意！index从0开始计数\n请根据文件名称输入分隔符和索引位置'''
        # self.textBrowser.append(text)
        # print(filenames,type(filenames),len(filenames))
        # print("adress")
        # print(adress)
        # #后缀统计
        # siffix = []  # 后缀
        # for p in adress:
        #     c = os.path.splitext(p)
        #     siffix.append(c[1])
        # print('文件后缀')
        # print(siffix)
        #
        # siffix_cnt = {}  # 统计后缀名称，将结果用一个字典存储
        # # 统计结果
        # for value in siffix:
        #     # get(value, num)函数的作用是获取字典中value对应的键值, num=0指示初始值大小。
        #     siffix_cnt[value] = siffix_cnt.get(value, 0) + 1
        # # 打印输出结果
        # siffix_key = [key for key in siffix_cnt.keys()]
        # siffix_values = [value for value in siffix_cnt.values()]
        # print(siffix_cnt)
        # print(siffix_key)
        # print(siffix_values)
        # self.comboBox.addItems(siffix_key)#将后缀输出给予选择



    # def segmentname(self):
    #     self.names = []
    #     identifier=self.identifier.text()  #获取分隔符
    #     #print(identifier,type(identifier))
    #     index=self.index.text()     #获取索引
    #     #print(index,type(index))
    #     # number=[]#存序号
    #     for name in filenames:
    #         c=name.split('.')[0]
    #         s=c.split(identifier)
    #         self.names.append(s[int(index)])
    #     print('序号')#转int！！
    #     print(number)
    #     #self.textBrowser.clear()
    #     text=f'分割成功！第一个图像编号为{number[0]},后缀为{siffix[0]} \n' \
    #          f'请在右侧输入初始ID和分隔符号，图片将会按照 ID+分隔符+编号 格式重新命名'
    #     self.textBrowser.append(text)
    #     self.textBrowser.ensureCursorVisible()


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
                    return newName
                num += 1
        return 'bug'


    def renameForFlag(self):
        '''取新ID  新分隔符 组成新地址用于改名'''
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
