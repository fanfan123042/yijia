from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMainWindow
from PyQt5.QtWidgets import QLabel, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtWidgets import QTreeWidget, QSplitter, QTreeWidgetItem, QFrame
from PyQt5.QtCore import Qt
import sys
from fun219.get_conn import get_conn



class Plat225Logo(object, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Plat225Logo, self).__init__(parent)

    def setupUi(self, Ui_MainWindow):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    logoNow = LogoIn()
    if logoNow.exec_() == QDialog.Accepted:
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())