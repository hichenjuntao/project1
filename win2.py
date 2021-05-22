import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from renameWin import Ui_renameWindow
import shutil


class secondWindow(QMainWindow, Ui_renameWindow):
    def __init__(self, parent=None):
        super(secondWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./images/cartoon2.ico'))
        self.pathButton.clicked.connect(self.openfile)
        self.readButton.clicked.connect(self.readfile)
        #self.sortButton.clicked.connect(self.check)
        self.renameButton.clicked.connect(self.msg)
        self.replaceButton.clicked.connect(self.check2)
        tip1='使用方法：\n功能①：选取文件夹以选择文件所在地址→读取文件获取图片→选择需要修改文件格式→输入分隔符和索引位置进行文件名分割获取序号→输入新的ID和分隔符点击按钮完成重命名操作\n当仅输入新ID而不输入分隔符和新名字时，功能转换为简单的图像排序输出'
        tip2='功能②:选取文件夹以选择文件所在地址→读取文件获取图片→输入需要修改的符号和新的符号→替换输出'
        self.textBrowser.append(tip1)
        self.textBrowser.append(tip2)

    def openfile(self):
        global path
        path = QFileDialog.getExistingDirectory(self,"选取文件夹")
        self.textBrowser.append('已选择文件所在路径为：'+path)
        self.textBrowser.append('请点击读取文件')
        print(path)



    def readfile(self):
        global filenames,adress,siffix_key,siffix_values,siffix
        #文件读取
        adress=[]
        self.textBrowser.append('读取文件名称：')
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                #self.textBrowser.append(os.path.join(dirpath, filename))
                self.textBrowser.append(filename)
                self.textBrowser.ensureCursorVisible()
                adress.append(os.path.join(dirpath, filename))
        self.textBrowser.append(f'读取成功！共读取图片{len(filenames)}张')
        text='''分隔符与index填写提示：\n文件110104_5fbdbae0cd2de.jpg，以'_'分割时→['110104','5fbdbae0cd2de']，在index中输入其编号位置i，注意！index从0开始计数\n请根据文件名称输入分隔符和索引位置'''
        self.textBrowser.append(text)
        print(filenames,type(filenames),len(filenames))#一个包含所有图片名称的列表
        print("adress")
        print(adress)#所有图片的原始路径
        #后缀统计
        siffix = []  # 后缀
        for p in adress:
            c = os.path.splitext(p)
            siffix.append(c[1])
        #print('文件后缀')
        #print(siffix)
        siffix_cnt = {}  # 统计后缀名称，将结果用一个字典存储
        # 统计结果
        for value in siffix:
            # get(value, num)函数的作用是获取字典中value对应的键值, num=0指示初始值大小。
            siffix_cnt[value] = siffix_cnt.get(value, 0) + 1
        # 打印输出结果
        siffix_key = [key for key in siffix_cnt.keys()]
        siffix_values = [value for value in siffix_cnt.values()]
        #print(siffix_cnt)  后缀字典
        #print(siffix_key)  统计后缀
        #print(siffix_values)统计后缀出现次数
        self.comboBox.addItems(siffix_key)#将后缀输出给予选择


    def check(self):
        #防止报错闪退
        if self.comboBox.currentText()=='文件格式选择':
            QMessageBox.information(self, "提示", "文件格式还没选择哦", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            self.rename()

    def check2(self):
        # 防止报错闪退
        if self.comboBox.currentText()=='文件格式选择':
            QMessageBox.information(self, "提示", "文件格式还没选择哦", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            self.replace_symbol()

    def segmentname(self):
        global number,sign
        identifier=self.identifier.text()  #获取分隔符
        #print(identifier,type(identifier))
        index=self.index.text()     #获取索引
        #print(index,type(index))
        number=[]#存序号
        for name in filenames:
            c=name.split('.')[0]
            s=c.split(identifier)
            number.append(s[int(index)])
        print('序号')#转int！！
        print(number)
        #self.textBrowser.clear()
        for i in range(len(number)):
            if siffix[i]==self.comboBox.currentText():
                sign=i
                break
            else:
                print('这个跳过')

        text=f'分割成功！需要修改的第一个图像编号为{number[sign]},后缀为{siffix[sign]} \n' \
             f'请在右侧输入初始ID和分隔符号，图片将会按照 ID+分隔符+编号 格式重新命名'
        self.textBrowser.append(text)
        self.textBrowser.ensureCursorVisible()




    def rename(self):
        '''取新ID  新分隔符 组成新地址用于改名'''
        #self.textBrowser.clear()
        id = self.ID.text()
        newidentifier=self.newidentifier.text()
        nm = self.nname.text()
        savepath=self.savefile()


        for i in range(len(number)):
            if siffix[i]==self.comboBox.currentText():
                newname = nm+newidentifier+str(int(id)+int(number[i]))+siffix[i]
                print(newname)
                newpath=os.path.join(savepath,newname)
                shutil.copy(adress[i],newpath)
                self.textBrowser.append(f'{adress[i]}已改名为{newpath}')
            else:
                self.textBrowser.append(f'{adress[i]}未改名')
        self.textBrowser.append('改名完成!跳转至输出文件夹')
        os.startfile(savepath)


    def msg(self):
        # 使用infomation信息框
        self.segmentname()
        id = self.ID.text()
        newidentifier = self.newidentifier.text()
        nm = self.nname.text()
        newname=nm+newidentifier+str(int(id)+int(number[sign]))+siffix[sign]
        text=f'是否确认用如下格式修改文件名？\n{newname},只会修改选择的文件格式，点击YES选择输出目录'
        reply = QMessageBox.information(self, "提示", text, QMessageBox.Yes | QMessageBox.No ,  QMessageBox.No )
        print(reply,type(reply))
        if reply==QMessageBox.Yes:
            self.textBrowser.append('确认操作')

            self.rename()
        else:
            self.textBrowser.append('取消操作')


    def savefile(self):
        path = QFileDialog.getExistingDirectory(self, "选取保存路径文件夹")
        return path

    def replace_symbol(self):
        global newnames
        oldsym = self.oldsymbol.text()
        newsym = self.newsymbol.text()
        newnames=[]
        for name in filenames:
            n=name.split(oldsym)
            nn=n[0]+newsym+n[1]
            newnames.append(nn)
        print(newnames)

        for i in range(len(filenames)):
            if siffix[i]==self.comboBox.currentText():
                sign2=i
                break
            else:
                print('这个跳过')

        text = f'是否确认用如下格式修改文件名？\n{newnames[sign2]},只会修改选择的文件格式，点击YES选择输出目录'
        reply = QMessageBox.information(self, "提示", text, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(reply, type(reply))
        if reply == QMessageBox.Yes:
            self.textBrowser.append('确认操作')
            self.rename2()
        else:
            self.textBrowser.append('取消操作')

    def rename2(self):
        savepath = self.savefile()

        for i in range(len(filenames)):
            if siffix[i] == self.comboBox.currentText():
                newname = newnames[i]
                newpath = os.path.join(savepath, newname)
                shutil.copy(adress[i], newpath)
                self.textBrowser.append(f'{adress[i]}已改名为{newpath}')
            else:
                self.textBrowser.append(f'{adress[i]}未改名')
        self.textBrowser.append('改名完成!跳转至输出文件夹')
        os.startfile(savepath)




















if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = secondWindow()
    myWin.show()
    sys.exit(app.exec_())
