import add_path_for_bat
import add_path_for_bat
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QTreeWidgetItem, QDesktopWidget
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys
from core.Ui_Menu0319 import Ui_MainWindow
from func.getConn import getConn
from baseClass225.ImageDeal import imgScaled
from baseClass225.Staff import Staff
from core.Ui_FixStaffInfo00 import Ui_Form


class FixStaffInfo00(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(FixStaffInfo00, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('修改员工个人信息')
        self.setWindowIcon(QIcon('plat225.ico'))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.lineEdit_7.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.comboBox.addItems(['--', '男', '女'])

        self.pushButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FixStaffInfo00()
    main.show()
    sys.exit(app.exec_())
