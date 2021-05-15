import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from renameWin import Ui_renameWindow


class secondWindow(QMainWindow, Ui_renameWindow):
    def __init__(self, parent=None):
        super(secondWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./images/cartoon2.ico'))
        self.pathButton.clicked.connect(self.openfile)
        self.readButton.clicked.connect(self.readfile)
        self.sortButton.clicked.connect(self.segmentname)
        self.renameButton.clicked.connect(self.msg)
        tip='使用方法\n点击选取文件夹以选择文件所在地址，后点击读取文件获取图片，之后在左侧输入分隔符和索引位置进行文件名分割，完成后在右侧输入新的ID和分隔符点击按钮完成重命名操作'
        self.textBrowser.append(tip)

    def openfile(self):
        global path
        path = QFileDialog.getExistingDirectory(self,"选取文件夹")
        self.textBrowser.append('文件所在路径为：'+path)
        self.textBrowser.append('请点击读取文件')
        print(path)



    def readfile(self):
        global filenames,adress
        adress=[]
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                self.textBrowser.append(os.path.join(dirpath, filename))
                self.textBrowser.ensureCursorVisible()
                adress.append(os.path.join(dirpath, filename))

        self.textBrowser.clear()
        self.textBrowser.append(f'读取成功！共读取图片{len(filenames)}张')
        text='''\n示例：图片名 110104_5fbdbae0cd2de.jpg，以'_'为分隔符分割时会分割成['110104','5fbdbae0cd2de']，index从0开始，如例子中的编号的index为0\n'''
        self.textBrowser.append(text)
        self.textBrowser.append(f'第一张图像文件名为{filenames[0]}，请在左侧输入读入图像编号所在位置index和分隔符\n')
        print(filenames,type(filenames),len(filenames))
        print("adress")
        print(adress)




    def segmentname(self):
        global siffix,number
        identifier=self.identifier.text()  #获取分隔符
        #print(identifier,type(identifier))
        index=self.index.text()     #获取索引
        #print(index,type(index))
        siffix=[]#后缀
        for p in adress:
            c = os.path.splitext(p)
            siffix.append(c[1])
        print('文件后缀')
        print(siffix)
        number=[]#存序号
        for name in filenames:
            c=name.split('.')[0]
            s=c.split(identifier)
            number.append(s[int(index)])
        print('序号')#转int！！
        print(number)
        self.textBrowser.clear()
        text=f'分割成功！第一个图像编号为{number[0]},后缀为{siffix[0]} \n' \
             f'请在右侧输入初始ID和分隔符号，图片将会按照 ID+分隔符+编号 格式重新命名'
        self.textBrowser.append(text)
        self.textBrowser.ensureCursorVisible()



    def rename(self):
        '''取新ID  新分隔符 组成新地址用于改名'''
        self.textBrowser.clear()
        id = self.ID.text()
        newidentifier=self.newidentifier.text()


        for i in range(len(number)):
            newname = id + newidentifier + number[i]+siffix[i]
            print(newname)
            newpath=os.path.join(path,newname)
            os.rename(adress[i],newpath)
            self.textBrowser.append(f'{adress[i]}已改名为{newpath}')
        self.textBrowser.append('改名完成')



    def msg(self):
        # 使用infomation信息框
        id = self.ID.text()
        newidentifier = self.newidentifier.text()
        newname=id+newidentifier+number[0]+siffix[0]
        text=f'是否确认用如下格式修改文件名？\n{newname}'
        reply = QMessageBox.information(self, "提示", text, QMessageBox.Yes | QMessageBox.No ,  QMessageBox.No )
        print(reply,type(reply))
        if reply==QMessageBox.Yes:
            self.textBrowser.append('确认操作')
            self.rename()
        else:
            self.textBrowser.append('取消操作')



















if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = secondWindow()
    myWin.show()
    sys.exit(app.exec_())
