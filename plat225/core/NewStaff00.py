import add_path_for_bat
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QTreeWidgetItem, QDesktopWidget
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys,re
# from core.Ui_Menu0319 import Ui_MainWindow
from func.getConn import getConn
from baseClass225.ImageDeal import imgScaled
from baseClass225.Staff import Staff
from core.Ui_NewStaff00 import Ui_Form
from func.f_change import f_str_blank, f_QtStr2Folat


class NewStaff00(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(NewStaff00, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('plat225.ico'))
        self.setWindowTitle('创建新用户')
        self.rightLab = [self.label_11, self.label_17, self.label_12, self.label_13,
                         self.label_14, self.label_15, self.label_16]
        self.setMaximumSize(502, 222)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.comboBox.clear()
        self.comboBox.addItems(['--', '男', '女'])
        for i in self.rightLab:
            i.setText('*')
            # i.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.submitNewStaff)
        self.lineEdit_7.editingFinished.connect(self.confirmData)

    def submitNewStaff(self):
        ret = {'status':True,'data':None,'message':None}
        staffName = f_str_blank(self.lineEdit_7.text())
        staffsex = f_str_blank(self.comboBox.currentText())
        staffphone = f_str_blank(self.lineEdit_6.text())
        staffemail = f_str_blank(self.lineEdit_8.text())
        staffposition = f_str_blank(self.lineEdit_10.text())
        staffpassword = f_str_blank(self.lineEdit_5.text())
        staffconfirmpassword = f_str_blank(self.lineEdit_9.text())
        staffsingle = f_str_blank(self.lineEdit_11.text())
        # staffxxxxx = f_str_blank(self.lineEdit_18.text())
        # print(staffName, staffsex)
        # print(staffphone, staffemail, staffposition)
        # print(staffpassword, staffconfirmpassword)
        # print(staffsingle)
        if staffName:
            if re.search('\d+',staffName):
                ret['status'] = False
                ret['data'] = '姓名不能包含数字'
                print(ret['data'])
            else:
                ret['data'] = '姓名正确'
                print(ret['data'])
                self.label_11.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
        else:
            ret['status'] = False
            ret['data'] = '姓名不能为空'
            print(ret['data'])

        if staffsex == '--':
            ret['status'] = False
            ret['data'] = '性别必选'
            print(ret['data'])
        else:
            ret['data'] = '性别正确'
            print(ret['data'])
            self.label_17.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))

        if staffphone.isdigit() and len(staffphone) == 11 and re.search('^1',staffphone):
            ret['data'] = '手机正确'
            print(ret['data'])
            self.label_12.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
        else:
            ret['status'] = False
            ret['data'] = '手机格式不正确'
            print(ret['data'])

        if re.search('\w+@\w+.com$',staffemail):
            ret['data'] = '邮箱格式正确'
            print(ret['data'])
            self.label_13.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
        else:
            ret['status'] = False
            ret['data'] = '邮箱格式不正确'
            print(ret['data'])

        if staffposition:
            if re.search('\d+', staffName):
                ret['status'] = False
                ret['data'] = '职位不能包含数字'
                print(ret['data'])
            else:
                ret['data'] = '职位正确'
                print(ret['data'])
                self.label_14.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
        else:
            ret['status'] = False
            ret['data'] = '职位不能为空'
            print(ret['data'])

        if staffpassword and staffconfirmpassword:
            if staffpassword == staffconfirmpassword:
                ret['data'] = '密码确认'
                print(ret['data'])
                self.label_15.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
                self.label_16.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
            else:
                ret['status'] = False
                ret['data'] = '两次输入不一致'
                print(ret['data'])
        else:
            ret['status'] = False
            ret['data'] = '密码不能为空'
            print(ret['data'])

        if staffsingle:
            if re.search('\d+',staffsingle):
                ret['status'] = False
                ret['data'] = '师傅跟单不能包含数字'
                print(ret['data'])
            else:
                ret['data'] = '正确'
                print(ret['data'])
                self.label_11.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
        else:
            ret['status'] = False
            ret['data'] = '不能为空'
            print(ret['data'])


        if ret['status']:
            print('成功')
        else:
            pass

        # print('添加成功')

    def confirmData(self):

        if len(self.lineEdit_7.text()) >= 2:
            self.label_11.setPixmap(QPixmap(imgScaled('right.jpg', 20, 20)))
        else:
            self.label_11.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = NewStaff00()
    main.show()
    sys.exit(app.exec_())
