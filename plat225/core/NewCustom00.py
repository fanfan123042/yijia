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
from core.UI_NewCustom import Ui_Form


class NewCustom00(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(NewCustom00, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('plat225.ico'))
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('新建客户')
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)

        fieldCustom = ['id_custom', 'name_custom', 'first_order', 'with_VAT', 'money_unit',
                       'quota_detail_with_vat', 'type_payment', 'remark']




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = NewCustom00()
    main.show()
    sys.exit(app.exec_())
