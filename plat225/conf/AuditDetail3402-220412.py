import time
import add_path_for_bat
import os
import sys
import xlwings
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QMessageBox
from func.f_change import f_date, f_str_blank, f_float, f_floatStr, f_dateStr, f_returnFloat
from func.f_change import f_QtStr2Folat, f_Qt2DateStr, f_Qt2FloatStr, f_QtSumList2Str
from baseClass225.QuotaInfo import QuoInfo
from func.getPath import getPath
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QPen, QImage
from PyQt5.QtCore import Qt
from baseClass225.ImageDeal import imgScaled
from func.StrClear import clear
import zipfile
from PIL import Image
from func.get_data import get_column_like, get_column_data
from func.getConn import getConn
from baseClass225.Order import Order
from baseClass225.CustomInfo import Custom
from core.SearchOrder3103 import SearchOrder3103
from PyQt5.Qt import QTableWidgetItem
from baseClass225.CustomInfo import CustomOrder, Custom
import datetime
from core.Ui_AuditDetail3402 import Ui_Form
from baseClass225.OrderAudit import OrderAudit
from func.OrderImage import orderImage
from baseClass225.NumOrder_Size import NumOrder_Size
from baseClass225.NumCut_Size import NumCut_Size


class AuditDetail(QWidget, Ui_Form):
    def __init__(self, staffName, remark, itemNumber, parent=None):
        super(AuditDetail, self).__init__(parent)
        self.setupUi(self)
        self.remark = str(remark).strip()
        self.item = str(itemNumber).strip()
        self.staffName = str(staffName).strip()
        self.setWindowIcon(QIcon('plat225.ico'))
        self.setWindowTitle('{:<20}{:<10}{:<25}{:<10}'
                            .format('单个物料采购审批表', self.staffName, self.remark, self.item))

        self.dataPurchase = [[self.lineEdit_8, self.lineEdit_18, self.lineEdit_79, self.lineEdit_3,
                             self.lineEdit_22, self.lineEdit_28, self.lineEdit_34, self.lineEdit_42,
                             self.lineEdit_35, self.lineEdit_46, self.lineEdit_53, self.lineEdit_66,
                             self.lineEdit_63, self.lineEdit_71, self.lineEdit_123, self.lineEdit_132,
                             self.lineEdit_167, self.lineEdit_144, self.lineEdit_138, self.lineEdit_149,
                             self.lineEdit_152, self.lineEdit_157, self.lineEdit_172],
                             [self.lineEdit_11, self.lineEdit_17, self.lineEdit_75, self.lineEdit_2,
                             self.lineEdit_23, self.lineEdit_29, self.lineEdit_30, self.lineEdit_43,
                             self.lineEdit_38, self.lineEdit_48, self.lineEdit_54, self.lineEdit_68,
                             self.lineEdit_60, self.lineEdit_74, self.lineEdit_124, self.lineEdit_130,
                             self.lineEdit_164, self.lineEdit_141, self.lineEdit_139, self.lineEdit_148,
                             self.lineEdit_153, self.lineEdit_158, self.lineEdit_171],
                             [self.lineEdit_12, self.lineEdit_19, self.lineEdit_76, self.lineEdit_5,
                             self.lineEdit_20, self.lineEdit_27, self.lineEdit_33, self.lineEdit_41,
                             self.lineEdit_37, self.lineEdit_45, self.lineEdit_52, self.lineEdit_65,
                             self.lineEdit_64, self.lineEdit_73, self.lineEdit_125, self.lineEdit_133,
                             self.lineEdit_163, self.lineEdit_143, self.lineEdit_142, self.lineEdit_146,
                             self.lineEdit_151, self.lineEdit_159, self.lineEdit_169],
                             [self.lineEdit_13, self.lineEdit_16, self.lineEdit_77, self.lineEdit_4,
                             self.lineEdit_24, self.lineEdit_25, self.lineEdit_31, self.lineEdit_44,
                             self.lineEdit_39, self.lineEdit_47, self.lineEdit_51, self.lineEdit_61,
                             self.lineEdit_69, self.lineEdit_70, self.lineEdit_126, self.lineEdit_131,
                             self.lineEdit_165, self.lineEdit_137, self.lineEdit_140, self.lineEdit_147,
                             self.lineEdit_155, self.lineEdit_160, self.lineEdit_170],
                             [self.lineEdit_14, self.lineEdit_15, self.lineEdit_78, self.lineEdit_7,
                             self.lineEdit_21, self.lineEdit_26, self.lineEdit_32, self.lineEdit_40,
                             self.lineEdit_36, self.lineEdit_49, self.lineEdit_50, self.lineEdit_67,
                             self.lineEdit_62, self.lineEdit_72, self.lineEdit_127, self.lineEdit_129,
                             self.lineEdit_166, self.lineEdit_135, self.lineEdit_136, self.lineEdit_145,
                             self.lineEdit_154, self.lineEdit_161, self.lineEdit_168]]

        self.order = Order(self.remark)
        self.audit = OrderAudit(self.remark)

        self.lineEdit_174.setText(str(self.order.remark))
        itemListAll = self.audit.bom_finished.split('】') + self.audit.bom_not_finish.split('】')
        itemList = [str(i) + '】' for i in itemListAll if f_date(i) is not None]
        self.comboBox_4.addItems(itemList + ['【e】'])
        self.comboBox_4.setCurrentText(self.item)        # 款式查找框设定

        self.lineEdit_86.setText(f_Qt2FloatStr(self.order.num_order, 0))
        self.lineEdit_87.setText(f_Qt2FloatStr(self.order.num_cut, 0))
        self.lineEdit_88.setText(f_Qt2FloatStr(self.order.num_ship, 0))
        self.lineEdit_119.setText(f_Qt2DateStr(self.order.date_order)[2:10])
        self.lineEdit_120.setText(f_Qt2FloatStr(self.order.days_from_order_date, 0))

        #  设置一系列组合
        self.items = ['【f1】', '【f2】', '【f3】', '【f4】', '【f5】',
                      '【a1】', '【a2】', '【a3】', '【a4】', '【a5】', '【a6】', '【a7】',
                      '【e】']
        self.codeQuota = ['fab_1_desc, fab_1_consume_cost, fab_1_width, fab_1_raw_material_price, '
                          'fab_1_weight, fab_1_calc_method, fab_1_cost, fab_1_remark',
                          'fab_2_desc, fab_2_consume_cost, fab_2_width, fab_2_raw_material_price, '
                          'fab_2_weight, fab_2_calc_method, fab_2_cost, fab_2_remark',
                          'fab_3_desc, fab_3_consume_cost, fab_3_width, fab_3_raw_material_price, '
                          'fab_3_weight, fab_3_calc_method, fab_3_cost, fab_3_remark',
                          'fab_4_desc, fab_4_consume_cost, fab_4_width, fab_4_raw_material_price, '
                          'fab_4_weight, fab_4_calc_method, fab_4_cost, fab_4_remark',
                          'fab_5_desc, fab_5_consume_cost, fab_5_width, fab_5_raw_material_price, '
                          'fab_5_weight, fab_5_calc_method, fab_5_cost, fab_5_remark',
                          'ass_1_item, ass_1_desc, ass_1_cost',
                          'ass_2_item, ass_2_desc, ass_2_cost',
                          'ass_3_item, ass_3_desc, ass_3_cost',
                          'ass_4_item, ass_4_desc, ass_4_cost',
                          'ass_5_item, ass_5_desc, ass_5_cost',
                          'ass_6_item, ass_6_desc, ass_6_cost',
                          'ass_7_item, ass_7_desc, ass_7_cost',
                          'extra_desc']
        self.dict_item = dict(zip(self.items, self.codeQuota))

        self.groupQuota = [(self.label_2, self.label_18, self.lineEdit_58),
                           (self.label_3, self.label_44, self.lineEdit_59),
                           (self.label_4, self.label_45, self.lineEdit_57),
                           (self.label_5, self.label_46, self.lineEdit_55),
                           (self.label_17, self.label_17, self.lineEdit_56),
                           (self.label_8, self.label_50, self.lineEdit_6),
                           (self.label_16, self.label_51, self.lineEdit_9)]

        self.labPur = [self.label_31, self.label_32, self.label_48, self.label_9, self.label_10, self.label_11,
                       self.label_12, self.label_15, self.label_36, self.label_37, self.label_41, self.label_38,
                       self.label_39, self.label_40, self.label_60, self.label_61, self.label_67, self.label_63,
                       self.label_62, self.label_64, self.label_65, self.label_66, self.label_68]

        self.labText = [['客户颜色', '物料颜色', '毛封(m)', '用料(m/件)', '裁损', '缩水', '加损', '克重(克/m*m)',
                         '物料价(元/kg)', '建议数量(kgs)', '建议金额(元)', '实际下单(kgs)', '采购金额(元)', '实到数量(kgs)',
                         '减料(kgs)', '换片', '实重(克/m*m)', '毛封(m)', '用量(m/件)', '预计裁数', '比例',
                         '实际裁数', '剩余料(kgs)'],
                        ['客户颜色', '物料颜色', '净封(m)', '用料(m/件)', '裁损', '缩水', '加损', '',
                         '物料价(元/m)', '建议数量(m)', '建议金额(元)', '实际下单(m)', '采购金额(元)', '实到数量(m)',
                         '减料(m)', '换片', '', '净封(m)', '用量(m/件)', '预计裁数', '比例', '实际裁数', '剩余料(m)'],
                        ['客户颜色', '物料颜色', '', '', '', '', '损耗', '', '物料价(元/件)', '建议数量(件)',
                         '建议金额(元)', '实际下单(件)', '采购金额(元)', '实回数量(件)', '', '', '', '', '', '', '', '', ''], ]

        self.pay = [[self.lineEdit_222, self.lineEdit_231, self.pushButton_4, self.lineEdit_121, self.lineEdit_193,
                     self.checkBox_9, self.checkBox_8, self.checkBox_10, self.pushButton_9, self.lineEdit_189,
                     self.lineEdit_199],
                    [self.lineEdit_225, self.lineEdit_233, self.pushButton_5, self.lineEdit_122, self.lineEdit_194,
                     self.checkBox_11, self.checkBox_15, self.checkBox_19, self.pushButton_10, self.lineEdit_188,
                     self.lineEdit_198],
                    [self.lineEdit_226, self.lineEdit_230, self.pushButton_6, self.lineEdit_185, self.lineEdit_195,
                     self.checkBox_12, self.checkBox_16, self.checkBox_20, self.pushButton_11, self.lineEdit_190,
                     self.lineEdit_200],
                    [self.lineEdit_227, self.lineEdit_232, self.pushButton_7, self.lineEdit_186, self.lineEdit_196,
                     self.checkBox_13, self.checkBox_17, self.checkBox_21, self.pushButton_12, self.lineEdit_191,
                     self.lineEdit_201],
                    [self.lineEdit_228, self.lineEdit_229, self.pushButton_8, self.lineEdit_187, self.lineEdit_197,
                     self.checkBox_14, self.checkBox_18, self.checkBox_22, self.pushButton_13, self.lineEdit_192,
                     self.lineEdit_202]]

        self.total = [self.label_19, self.lineEdit_82, self.label_52, self.lineEdit_80, self.lineEdit_81,
                      self.lineEdit_83, self.lineEdit_84, self.lineEdit_85, self.lineEdit_128, self.lineEdit_150,
                      self.lineEdit_156, self.lineEdit_162, self.lineEdit_173]
        self.polity = [self.label_49, self.checkBox_2, self.checkBox_23, self.checkBox_3, self.checkBox_5,
                       self.checkBox, self.checkBox_4]   # 设组合值

        self.numOrderList = [[self.lineEdit_99, self.lineEdit_100],
                             [self.lineEdit_101, self.lineEdit_102],
                             [self.lineEdit_103, self.lineEdit_104],
                             [self.lineEdit_105, self.lineEdit_106],
                             [self.lineEdit_107, self.lineEdit_108]]

        self.numCutList = [[self.lineEdit_89, self.lineEdit_94],
                           [self.lineEdit_90, self.lineEdit_93],
                           [self.lineEdit_91, self.lineEdit_92],
                           [self.lineEdit_96, self.lineEdit_95],
                           [self.lineEdit_98, self.lineEdit_97]]

        self.comboBox.addItems(['长度计算', '重量计算'])
        self.comboBox_2.addItems(['制单数', '裁数', '走货数'])
        self.comboBox_3.addItems(['--', '1%', '3%', '5%', '6%', '9%', '13%'])
        self.comboBox_7.addItems(['--', '单一总额', '整件计价', '单件用量'])
        self.comboBox_5.addItems(['--', '上料不足', '缩率偏大', '计算错误', '过程丢失', '损耗偏大', '人为造次'])
        self.comboBox_6.addItems(['--', '上料不足', '缩率偏大', '计算错误', '过程丢失', '损耗偏大', '人为造次'])  # 下拉栏内容

        for i in self.pay:
            for j in i:
                if i.index(j) > 2:
                    j.setVisible(False)

        self.sizeCode = NumOrder_Size(self.remark)
        self.cutSize = NumCut_Size(self.remark)
        self.dataResource = self.comboBox_2.currentText()
        self.vatPur = f_QtStr2Folat(self.comboBox_3.currentText())
        self.amountReal = 0      # 实际要付的付款数据，随时变动，看具体情况而定

        # 信号
        self.pushButton_16.clicked.connect(self.close)
        self.pushButton_17.clicked.connect(sys.exit)
        image = orderImage(self.remark)
        self.label_83.setPixmap(QPixmap(imgScaled(image, 118, 118)))
        self.comboBox_7.currentTextChanged.connect(self.settingDisplay)
        self.comboBox_7.currentTextChanged.connect(self.settingNumFormat)
        self.comboBox.currentTextChanged.connect(self.calculateMethodChanged)
        self.comboBox.currentTextChanged.connect(self.settingNumFormat)
        self.comboBox_4.currentTextChanged.connect(self.itemChanged)
        self.checkBox_2.toggled.connect(self.sameColor)
        self.checkBox_23.toggled.connect(self.sameConsume)
        self.checkBox_3.toggled.connect(self.sameWastage)
        self.checkBox.toggled.connect(self.sameWidth)
        self.checkBox_4.toggled.connect(self.sameWeight)
        self.checkBox_5.toggled.connect(self.samePrice)
        self.comboBox_2.currentTextChanged.connect(self.dataFromChanged)
        self.comboBox_3.currentTextChanged.connect(self.vatPurChanged)


        self.lineEdit_79.editingFinished.connect(self.autoCalculate)
        self.lineEdit_3.editingFinished.connect(self.autoCalculate)
        self.lineEdit_22.editingFinished.connect(self.autoCalculate)
        self.lineEdit_28.editingFinished.connect(self.autoCalculate)
        self.lineEdit_34.editingFinished.connect(self.autoCalculate)
        self.lineEdit_42.editingFinished.connect(self.autoCalculate)
        self.lineEdit_35.editingFinished.connect(self.autoCalculate)
        self.lineEdit_75.editingFinished.connect(self.autoCalculate)
        self.lineEdit_2.editingFinished.connect(self.autoCalculate)
        self.lineEdit_23.editingFinished.connect(self.autoCalculate)
        self.lineEdit_29.editingFinished.connect(self.autoCalculate)
        self.lineEdit_30.editingFinished.connect(self.autoCalculate)
        self.lineEdit_43.editingFinished.connect(self.autoCalculate)
        self.lineEdit_38.editingFinished.connect(self.autoCalculate)
        self.lineEdit_76.editingFinished.connect(self.autoCalculate)
        self.lineEdit_5.editingFinished.connect(self.autoCalculate)
        self.lineEdit_20.editingFinished.connect(self.autoCalculate)
        self.lineEdit_27.editingFinished.connect(self.autoCalculate)
        self.lineEdit_33.editingFinished.connect(self.autoCalculate)
        self.lineEdit_41.editingFinished.connect(self.autoCalculate)
        self.lineEdit_37.editingFinished.connect(self.autoCalculate)
        self.lineEdit_77.editingFinished.connect(self.autoCalculate)
        self.lineEdit_4.editingFinished.connect(self.autoCalculate)
        self.lineEdit_24.editingFinished.connect(self.autoCalculate)
        self.lineEdit_25.editingFinished.connect(self.autoCalculate)
        self.lineEdit_31.editingFinished.connect(self.autoCalculate)
        self.lineEdit_44.editingFinished.connect(self.autoCalculate)
        self.lineEdit_39.editingFinished.connect(self.autoCalculate)
        self.lineEdit_78.editingFinished.connect(self.autoCalculate)
        self.lineEdit_7.editingFinished.connect(self.autoCalculate)
        self.lineEdit_21.editingFinished.connect(self.autoCalculate)
        self.lineEdit_26.editingFinished.connect(self.autoCalculate)
        self.lineEdit_32.editingFinished.connect(self.autoCalculate)
        self.lineEdit_40.editingFinished.connect(self.autoCalculate)
        self.lineEdit_36.editingFinished.connect(self.autoCalculate)
        self.lineEdit_66.editingFinished.connect(self.autoCalculate)
        self.lineEdit_71.editingFinished.connect(self.autoCalculate)
        self.lineEdit_123.editingFinished.connect(self.autoCalculate)
        self.lineEdit_132.editingFinished.connect(self.autoCalculate)
        self.lineEdit_167.editingFinished.connect(self.autoCalculate)
        self.lineEdit_144.editingFinished.connect(self.autoCalculate)
        self.lineEdit_138.editingFinished.connect(self.autoCalculate)
        self.lineEdit_172.editingFinished.connect(self.autoCalculate)
        self.lineEdit_68.editingFinished.connect(self.autoCalculate)
        self.lineEdit_74.editingFinished.connect(self.autoCalculate)
        self.lineEdit_124.editingFinished.connect(self.autoCalculate)
        self.lineEdit_130.editingFinished.connect(self.autoCalculate)
        self.lineEdit_164.editingFinished.connect(self.autoCalculate)
        self.lineEdit_141.editingFinished.connect(self.autoCalculate)
        self.lineEdit_139.editingFinished.connect(self.autoCalculate)
        self.lineEdit_171.editingFinished.connect(self.autoCalculate)
        self.lineEdit_65.editingFinished.connect(self.autoCalculate)
        self.lineEdit_73.editingFinished.connect(self.autoCalculate)
        self.lineEdit_125.editingFinished.connect(self.autoCalculate)
        self.lineEdit_133.editingFinished.connect(self.autoCalculate)
        self.lineEdit_163.editingFinished.connect(self.autoCalculate)
        self.lineEdit_143.editingFinished.connect(self.autoCalculate)
        self.lineEdit_142.editingFinished.connect(self.autoCalculate)
        self.lineEdit_169.editingFinished.connect(self.autoCalculate)
        self.lineEdit_61.editingFinished.connect(self.autoCalculate)
        self.lineEdit_70.editingFinished.connect(self.autoCalculate)
        self.lineEdit_126.editingFinished.connect(self.autoCalculate)
        self.lineEdit_131.editingFinished.connect(self.autoCalculate)
        self.lineEdit_165.editingFinished.connect(self.autoCalculate)
        self.lineEdit_137.editingFinished.connect(self.autoCalculate)
        self.lineEdit_140.editingFinished.connect(self.autoCalculate)
        self.lineEdit_170.editingFinished.connect(self.autoCalculate)
        self.lineEdit_67.editingFinished.connect(self.autoCalculate)
        self.lineEdit_72.editingFinished.connect(self.autoCalculate)
        self.lineEdit_127.editingFinished.connect(self.autoCalculate)
        self.lineEdit_129.editingFinished.connect(self.autoCalculate)
        self.lineEdit_166.editingFinished.connect(self.autoCalculate)
        self.lineEdit_135.editingFinished.connect(self.autoCalculate)
        self.lineEdit_136.editingFinished.connect(self.autoCalculate)
        self.lineEdit_168.editingFinished.connect(self.autoCalculate)
        self.lineEdit_109.editingFinished.connect(self.autoCalculate)
        self.lineEdit_110.editingFinished.connect(self.autoCalculate)

        self.lineEdit_63.editingFinished.connect(self.autoCalculate)

        # 初始程序运行
        self.settingDisplay()
        self.settingNumFormat()
        self.setNumOrder()
        self.setNumCut()
        self.getBasicData()
        self.autoCalculate()

    def vatPurChanged(self):
        self.vatPur = f_QtStr2Folat(self.comboBox_3.currentText())
        self.autoCalculate()

    def dataFromChanged(self):
        self.settingNumFormat()
        auditModel = self.comboBox_7.currentText()
        self.dataResource = self.comboBox_2.currentText()
        if self.dataResource == '走货数':
            if auditModel == '单件用量':
                self.comboBox_7.setCurrentText('整件计价')
                self.settingNumFormat()
            self.checkBox_2.setChecked(True)
            self.sameColor()
            self.checkBox_2.setEnabled(False)
        else:
            self.checkBox_2.setEnabled(True)

    def autoCalculate(self):
        if self.comboBox_2.currentText() == '制单数':
            for i in range(5):
                self.dataPurchase[i][0].setText(self.numOrderList[i][0].text())
        if self.comboBox_2.currentText() in ['裁数', '走货数']:
            for i in range(5):
                self.dataPurchase[i][0].setText(self.numCutList[i][0].text())   # 款号颜色

        numPurchase1 = numPurchase2 = numPurchase3 = numPurchase4 = numPurchase5 = 0
        if self.checkBox_2.isChecked() and self.comboBox_2.currentText() == '制单数':
            numPurchase1 = f_QtStr2Folat(self.lineEdit_86.text())
        elif self.checkBox_2.isChecked() and self.comboBox_2.currentText() == '裁数':
            numPurchase1 = f_QtStr2Folat(self.lineEdit_87.text())
        elif self.checkBox_2.isChecked() and self.comboBox_2.currentText() == '走货数':
            numPurchase1 = f_QtStr2Folat(self.lineEdit_88.text())
        else:
            if self.comboBox_2.currentText() == '制单数':
                numPurchase1 = f_QtStr2Folat(self.lineEdit_100.text())
                numPurchase2 = f_QtStr2Folat(self.lineEdit_102.text())
                numPurchase3 = f_QtStr2Folat(self.lineEdit_104.text())
                numPurchase4 = f_QtStr2Folat(self.lineEdit_106.text())
                numPurchase5 = f_QtStr2Folat(self.lineEdit_108.text())
            elif self.comboBox_2.currentText() == '裁数':
                numPurchase1 = f_QtStr2Folat(self.lineEdit_94.text())
                numPurchase2 = f_QtStr2Folat(self.lineEdit_93.text())
                numPurchase3 = f_QtStr2Folat(self.lineEdit_92.text())
                numPurchase4 = f_QtStr2Folat(self.lineEdit_95.text())
                numPurchase5 = f_QtStr2Folat(self.lineEdit_97.text())

        width1 = width2 = width3 = width4 = width5 = 0
        if not self.dataPurchase[0][2].isHidden():
            width1 = f_returnFloat(self.dataPurchase[0][2].text())               # 门封

        if not self.dataPurchase[1][2].isHidden() and not self.dataPurchase[1][2].isEnabled():
            width2 = width1
            self.dataPurchase[1][2].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[1][2].isHidden() and self.dataPurchase[1][2].isEnabled():
            width2 = f_returnFloat(self.dataPurchase[1][2].text())

        if not self.dataPurchase[2][2].isHidden() and not self.dataPurchase[2][2].isEnabled():
            width3 = width1
            self.dataPurchase[2][2].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[2][2].isHidden() and self.dataPurchase[2][2].isEnabled():
            width3 = f_returnFloat(self.dataPurchase[2][2].text())

        if not self.dataPurchase[3][2].isHidden() and not self.dataPurchase[3][2].isEnabled():
            width4 = width1
            self.dataPurchase[3][2].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[3][2].isHidden() and self.dataPurchase[3][2].isEnabled():
            width4 = f_returnFloat(self.dataPurchase[3][2].text())

        if not self.dataPurchase[4][2].isHidden() and not self.dataPurchase[4][2].isEnabled():
            width5 = width1
            self.dataPurchase[4][2].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[4][2].isHidden() and self.dataPurchase[4][2].isEnabled():
            width5 = f_returnFloat(self.dataPurchase[4][2].text())

        consume1 = consume2 = consume3 = consume4 = consume5 = 0
        if not self.dataPurchase[0][2].isHidden():
            consume1 = f_returnFloat(self.dataPurchase[0][3].text())          # 用料
        if not self.dataPurchase[1][3].isHidden() and not self.dataPurchase[1][3].isEnabled():
            consume2 = consume1
            self.dataPurchase[1][3].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[1][3].isHidden() and self.dataPurchase[1][3].isEnabled():
            consume2 = f_returnFloat(self.dataPurchase[1][3].text())

        if not self.dataPurchase[2][3].isHidden() and not self.dataPurchase[2][3].isEnabled():
            consume3 = consume1
            self.dataPurchase[2][3].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[2][3].isHidden() and self.dataPurchase[2][3].isEnabled():
            consume3 = f_returnFloat(self.dataPurchase[2][3].text())

        if not self.dataPurchase[3][3].isHidden() and not self.dataPurchase[3][3].isEnabled():
            consume4 = consume1
            self.dataPurchase[3][3].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[3][3].isHidden() and self.dataPurchase[3][3].isEnabled():
            consume4 = f_returnFloat(self.dataPurchase[3][3].text())

        if not self.dataPurchase[4][3].isHidden() and not self.dataPurchase[4][3].isEnabled():
            consume5 = consume1
            self.dataPurchase[4][3].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[4][3].isHidden() and self.dataPurchase[4][3].isEnabled():
            consume5 = f_returnFloat(self.dataPurchase[4][3].text())

        wastageCut1 = wastageCut2 = wastageCut3 = wastageCut4 = wastageCut5 = 0   # 裁损
        if not self.dataPurchase[0][4].isHidden():
            wastageCut1 = f_returnFloat(self.dataPurchase[0][4].text())

        if not self.dataPurchase[1][4].isHidden() and not self.dataPurchase[1][4].isEnabled():
            wastageCut2 = wastageCut1
            self.dataPurchase[1][4].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[1][4].isHidden() and self.dataPurchase[1][4].isEnabled():
            wastageCut2 = f_returnFloat(self.dataPurchase[1][4].text())

        if not self.dataPurchase[2][4].isHidden() and not self.dataPurchase[2][4].isEnabled():
            wastageCut3 = wastageCut1
            self.dataPurchase[2][4].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[2][4].isHidden() and self.dataPurchase[2][4].isEnabled():
            wastageCut3 = f_returnFloat(self.dataPurchase[2][4].text())

        if not self.dataPurchase[3][4].isHidden() and not self.dataPurchase[3][4].isEnabled():
            wastageCut4 = wastageCut1
            self.dataPurchase[3][4].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[3][4].isHidden() and self.dataPurchase[3][4].isEnabled():
            wastageCut4 = f_returnFloat(self.dataPurchase[3][4].text())

        if not self.dataPurchase[4][4].isHidden() and not self.dataPurchase[4][4].isEnabled():
            wastageCut5 = wastageCut1
            self.dataPurchase[4][4].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[4][4].isHidden() and self.dataPurchase[4][4].isEnabled():
            wastageCut5 = f_returnFloat(self.dataPurchase[4][4].text())

        wastageShrink1 = wastageShrink2 = wastageShrink3 = wastageShrink4 = wastageShrink5 = 0             # 缩水
        if not self.dataPurchase[0][5].isHidden():
            wastageShrink1 = f_returnFloat(self.dataPurchase[0][5].text())

        if not self.dataPurchase[1][5].isHidden() and not self.dataPurchase[1][5].isEnabled():
            wastageShrink2 = wastageShrink1
            self.dataPurchase[1][5].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[1][5].isHidden() and self.dataPurchase[1][5].isEnabled():
            wastageShrink2 = f_returnFloat(self.dataPurchase[1][5].text())

        if not self.dataPurchase[2][5].isHidden() and not self.dataPurchase[2][5].isEnabled():
            wastageShrink3 = wastageShrink1
            self.dataPurchase[2][5].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[2][5].isHidden() and self.dataPurchase[2][5].isEnabled():
            wastageShrink3 = f_returnFloat(self.dataPurchase[2][5].text())

        if not self.dataPurchase[3][5].isHidden() and not self.dataPurchase[3][5].isEnabled():
            wastageShrink4 = wastageShrink1
            self.dataPurchase[3][5].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[3][5].isHidden() and self.dataPurchase[3][5].isEnabled():
            wastageShrink4 = f_returnFloat(self.dataPurchase[3][5].text())

        if not self.dataPurchase[4][5].isHidden() and not self.dataPurchase[4][5].isEnabled():
            wastageShrink5 = wastageShrink1
            self.dataPurchase[4][5].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[4][5].isHidden() and self.dataPurchase[4][5].isEnabled():
            wastageShrink5 = f_returnFloat(self.dataPurchase[4][5].text())

        wastageNormal1 = wastageNormal2 = wastageNormal3 = wastageNormal4 = wastageNormal5 = 0   # 加损
        if not self.dataPurchase[0][6].isHidden():
            wastageNormal1 = f_returnFloat(self.dataPurchase[0][6].text())  # 门封

        if not self.dataPurchase[1][6].isHidden() and not self.dataPurchase[1][6].isEnabled():
            wastageNormal2 = wastageNormal1
            self.dataPurchase[1][6].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[1][6].isHidden() and self.dataPurchase[1][6].isEnabled():
            wastageNormal2 = f_returnFloat(self.dataPurchase[1][6].text())

        if not self.dataPurchase[2][6].isHidden() and not self.dataPurchase[2][6].isEnabled():
            wastageNormal3 = wastageNormal1
            self.dataPurchase[2][6].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[2][6].isHidden() and self.dataPurchase[2][6].isEnabled():
            wastageNormal3 = f_returnFloat(self.dataPurchase[2][6].text())

        if not self.dataPurchase[3][6].isHidden() and not self.dataPurchase[3][6].isEnabled():
            wastageNormal4 = wastageNormal1
            self.dataPurchase[3][6].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[3][6].isHidden() and self.dataPurchase[3][6].isEnabled():
            wastageNormal4 = f_returnFloat(self.dataPurchase[3][6].text())

        if not self.dataPurchase[4][6].isHidden() and not self.dataPurchase[4][6].isEnabled():
            wastageNormal5 = wastageNormal1
            self.dataPurchase[4][6].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[4][6].isHidden() and self.dataPurchase[4][6].isEnabled():
            wastageNormal5 = f_returnFloat(self.dataPurchase[4][6].text())

        weight1 = weight2 = weight3 = weight4 = weight5 = 0     # 克重
        if not self.dataPurchase[0][7].isHidden():
            weight1 = f_returnFloat(self.dataPurchase[0][7].text())

        if not self.dataPurchase[1][7].isHidden() and not self.dataPurchase[1][7].isEnabled():
            weight2 = weight1
            self.dataPurchase[1][7].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[1][7].isHidden() and self.dataPurchase[1][7].isEnabled():
            weight2 = f_returnFloat(self.dataPurchase[1][7].text())

        if not self.dataPurchase[2][7].isHidden() and not self.dataPurchase[2][7].isEnabled():
            weight3 = weight1
            self.dataPurchase[2][7].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[2][7].isHidden() and self.dataPurchase[2][7].isEnabled():
            weight3 = f_returnFloat(self.dataPurchase[2][7].text())

        if not self.dataPurchase[3][7].isHidden() and not self.dataPurchase[3][7].isEnabled():
            weight4 = weight1
            self.dataPurchase[3][7].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[3][7].isHidden() and self.dataPurchase[3][7].isEnabled():
            weight4 = f_returnFloat(self.dataPurchase[3][7].text())

        if not self.dataPurchase[4][7].isHidden() and not self.dataPurchase[4][7].isEnabled():
            weight5 = weight1
            self.dataPurchase[4][7].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[4][7].isHidden() and self.dataPurchase[4][7].isEnabled():
            weight5 = f_returnFloat(self.dataPurchase[4][7].text())

        rawPrice1 = rawPrice2 = rawPrice3 = rawPrice4 = rawPrice5 = 0
        if not self.dataPurchase[0][8].isHidden():
            rawPrice1 = f_returnFloat(self.dataPurchase[0][8].text())  # 门封

        if not self.dataPurchase[1][8].isHidden() and not self.dataPurchase[1][8].isEnabled():
            rawPrice2 = rawPrice1
            self.dataPurchase[1][8].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[1][8].isHidden() and self.dataPurchase[1][8].isEnabled():
            rawPrice2 = f_returnFloat(self.dataPurchase[1][8].text())

        if not self.dataPurchase[2][8].isHidden() and not self.dataPurchase[2][8].isEnabled():
            rawPrice3 = rawPrice1
            self.dataPurchase[2][8].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[2][8].isHidden() and self.dataPurchase[2][8].isEnabled():
            rawPrice3 = f_returnFloat(self.dataPurchase[2][8].text())

        if not self.dataPurchase[3][8].isHidden() and not self.dataPurchase[3][8].isEnabled():
            rawPrice4 = rawPrice1
            self.dataPurchase[3][8].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[3][8].isHidden() and self.dataPurchase[3][8].isEnabled():
            rawPrice4 = f_returnFloat(self.dataPurchase[3][8].text())

        if not self.dataPurchase[4][8].isHidden() and not self.dataPurchase[4][8].isEnabled():
            rawPrice5 = rawPrice1
            self.dataPurchase[4][8].setText(f_Qt2FloatStr(width1))
        elif not self.dataPurchase[4][8].isHidden() and self.dataPurchase[4][8].isEnabled():
            rawPrice5 = f_returnFloat(self.dataPurchase[4][8].text())

        if self.comboBox.currentText() == '重量计算':
            numPre1 = (numPurchase1 * width1 * consume1 * weight1/1000 * (wastageCut1/100+1) *
                       (wastageShrink1/100+1) * (wastageNormal1/100+1))
            numPre2 = (numPurchase2 * width2 * consume2 * weight2 / 1000 * (wastageCut2 / 100 + 1) * (
                        wastageShrink2 / 100 + 1) * (wastageNormal2 / 100 + 1))
            numPre3 = (numPurchase3 * width3 * consume3 * weight3 / 1000 * (wastageCut3 / 100 + 1) * (
                        wastageShrink3 / 100 + 1) * (wastageNormal3 / 100 + 1))
            numPre4 = (numPurchase4 * width4 * consume4 * weight4 / 1000 * (wastageCut4 / 100 + 1) * (
                        wastageShrink4 / 100 + 1) * (wastageNormal4 / 100 + 1))
            numPre5 = (numPurchase5 * width5 * consume5 * weight5 / 1000 * (wastageCut5 / 100 + 1) * (
                        wastageShrink5 / 100 + 1) * (wastageNormal5 / 100 + 1))
        else:
            numPre1 = (numPurchase1 * consume1 * (wastageCut1/100+1) * (wastageShrink1/100+1) * (wastageNormal1/100+1))
            numPre2 = (numPurchase2 * consume2 * (wastageCut2 / 100 + 1) * (wastageShrink2 / 100 + 1) * (
                        wastageNormal2 / 100 + 1))
            numPre3 = (numPurchase3 * consume3 * (wastageCut3 / 100 + 1) * (wastageShrink3 / 100 + 1) * (
                        wastageNormal3 / 100 + 1))
            numPre4 = (numPurchase4 * consume4 * (wastageCut4 / 100 + 1) * (wastageShrink4 / 100 + 1) * (
                        wastageNormal4 / 100 + 1))
            numPre5 = (numPurchase5 * consume5 * (wastageCut5 / 100 + 1) * (wastageShrink5 / 100 + 1) * (
                        wastageNormal5 / 100 + 1))
        self.dataPurchase[0][9].setText(f_Qt2FloatStr(numPre1, 2))
        self.dataPurchase[0][10].setText(f_Qt2FloatStr(numPre1*rawPrice1, 2))
        self.dataPurchase[1][9].setText(f_Qt2FloatStr(numPre2, 2))
        self.dataPurchase[1][10].setText(f_Qt2FloatStr(numPre2*rawPrice2, 2))
        self.dataPurchase[2][9].setText(f_Qt2FloatStr(numPre3, 2))
        self.dataPurchase[2][10].setText(f_Qt2FloatStr(numPre3*rawPrice3, 2))
        self.dataPurchase[3][9].setText(f_Qt2FloatStr(numPre4, 2))
        self.dataPurchase[3][10].setText(f_Qt2FloatStr(numPre4*rawPrice4, 2))
        self.dataPurchase[4][9].setText(f_Qt2FloatStr(numPre5, 2))
        self.dataPurchase[4][10].setText(f_Qt2FloatStr(numPre5*rawPrice5, 2))

        purNumReal1 = f_returnFloat(self.dataPurchase[0][11].text())
        self.dataPurchase[0][12].setText(f_Qt2FloatStr(purNumReal1*rawPrice1, 2))
        purNumReal2 = f_returnFloat(self.dataPurchase[1][11].text())
        self.dataPurchase[1][12].setText(f_Qt2FloatStr(purNumReal2*rawPrice2, 2))
        purNumReal3 = f_returnFloat(self.dataPurchase[2][11].text())
        self.dataPurchase[2][12].setText(f_Qt2FloatStr(purNumReal3*rawPrice3, 2))
        purNumReal4 = f_returnFloat(self.dataPurchase[3][11].text())
        self.dataPurchase[3][12].setText(f_Qt2FloatStr(purNumReal4*rawPrice4, 2))
        purNumReal5 = f_returnFloat(self.dataPurchase[4][11].text())
        self.dataPurchase[4][12].setText(f_Qt2FloatStr(purNumReal5*rawPrice5, 2))

        for i in self.dataPurchase[19:21]:
            for j in i:
                j.clear()
        if self.comboBox_2.currentText() == '重量计算':
            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[0][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[0][16].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[0][17].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[0][18].text()) != 0):
                self.dataPurchase[0][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[0][13].text()) - f_QtStr2Folat(self.dataPurchase[0][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[0][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[0][16].text()) * 1000
                    / f_QtStr2Folat(self.dataPurchase[0][17].text())
                    / f_QtStr2Folat(self.dataPurchase[0][18].text())))
            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[1][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[1][16].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[1][17].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[1][18].text()) != 0):
                self.dataPurchase[1][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[1][13].text()) - f_QtStr2Folat(self.dataPurchase[1][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[1][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[1][16].text()) * 1000
                    / f_QtStr2Folat(self.dataPurchase[1][17].text())
                    / f_QtStr2Folat(self.dataPurchase[1][18].text())))
            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[2][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[2][16].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[2][17].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[2][18].text()) != 0):
                self.dataPurchase[2][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[2][13].text()) - f_QtStr2Folat(self.dataPurchase[2][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[2][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[2][16].text()) * 1000
                    / f_QtStr2Folat(self.dataPurchase[2][17].text())
                    / f_QtStr2Folat(self.dataPurchase[2][18].text())))
            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[3][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[3][16].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[3][17].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[3][18].text()) != 0):
                self.dataPurchase[3][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[3][13].text()) - f_QtStr2Folat(self.dataPurchase[3][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[3][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[3][16].text()) * 1000
                    / f_QtStr2Folat(self.dataPurchase[3][17].text())
                    / f_QtStr2Folat(self.dataPurchase[3][18].text())))
            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[4][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[4][16].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[4][17].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[4][18].text()) != 0):
                self.dataPurchase[4][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[4][13].text()) - f_QtStr2Folat(self.dataPurchase[4][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[4][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[4][16].text()) * 1000
                    / f_QtStr2Folat(self.dataPurchase[4][17].text())
                    / f_QtStr2Folat(self.dataPurchase[4][18].text())))
        else:
            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[0][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[0][18].text()) != 0):
                self.dataPurchase[0][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[0][13].text()) - f_QtStr2Folat(self.dataPurchase[0][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[0][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[0][18].text())))

            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[1][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[1][18].text()) != 0):
                self.dataPurchase[1][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[1][13].text()) - f_QtStr2Folat(self.dataPurchase[1][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[1][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[1][18].text())))

            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[2][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[2][18].text()) != 0):
                self.dataPurchase[2][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[2][13].text()) - f_QtStr2Folat(self.dataPurchase[2][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[2][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[2][18].text())))

            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[3][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[3][18].text()) != 0):
                self.dataPurchase[3][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[3][13].text()) - f_QtStr2Folat(self.dataPurchase[3][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[3][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[3][18].text())))

            if (self.checkBox_6.isChecked()
                    and self.checkBox_7.isChecked()
                    and f_QtStr2Folat(self.dataPurchase[4][13].text()) != 0
                    and f_QtStr2Folat(self.dataPurchase[4][18].text()) != 0):
                self.dataPurchase[4][19].setText(f_Qt2FloatStr(
                    (f_QtStr2Folat(self.dataPurchase[4][13].text()) - f_QtStr2Folat(self.dataPurchase[4][14].text()))
                    / (1 + f_QtStr2Folat(self.dataPurchase[4][15].text()) / 100)
                    / f_QtStr2Folat(self.dataPurchase[4][18].text())))

        if f_date(self.dataPurchase[0][19].text()) is not None and f_date(self.lineEdit_100.text()) is not None:
            self.dataPurchase[0][20].setText(f_Qt2FloatStr(f_QtStr2Folat(self.dataPurchase[0][19].text())
                                                           / f_QtStr2Folat(self.lineEdit_100.text()), 3))
        if f_date(self.dataPurchase[1][19].text()) is not None and f_date(self.lineEdit_102.text()) is not None:
            self.dataPurchase[1][20].setText(f_Qt2FloatStr(f_QtStr2Folat(self.dataPurchase[1][19].text())
                                                           / f_QtStr2Folat(self.lineEdit_102.text()), 3))
        if f_date(self.dataPurchase[2][19].text()) is not None and f_date(self.lineEdit_104.text()) is not None:
            self.dataPurchase[2][20].setText(f_Qt2FloatStr(f_QtStr2Folat(self.dataPurchase[2][19].text())
                                                           / f_QtStr2Folat(self.lineEdit_104.text()), 3))
        if f_date(self.dataPurchase[3][19].text()) is not None and f_date(self.lineEdit_106.text()) is not None:
            self.dataPurchase[3][20].setText(f_Qt2FloatStr(f_QtStr2Folat(self.dataPurchase[3][19].text())
                                                           / f_QtStr2Folat(self.lineEdit_106.text()), 3))
        if f_date(self.dataPurchase[4][19].text()) is not None and f_date(self.lineEdit_108.text()) is not None:
            self.dataPurchase[4][20].setText(f_Qt2FloatStr(f_QtStr2Folat(self.dataPurchase[4][19].text())
                                                           / f_QtStr2Folat(self.lineEdit_108.text()), 3))

        self.dataPurchase[0][21].setText(self.lineEdit_94.text())
        self.dataPurchase[1][21].setText(self.lineEdit_93.text())
        self.dataPurchase[2][21].setText(self.lineEdit_92.text())
        self.dataPurchase[3][21].setText(self.lineEdit_95.text())
        self.dataPurchase[4][21].setText(self.lineEdit_97.text())

        self.lineEdit_80.setText(f_QtSumList2Str([numPre1, numPre2, numPre3, numPre4, numPre5], 2))
        self.lineEdit_81.setText(f_QtSumList2Str([numPre1*rawPrice1, numPre2*rawPrice2,
                                                  numPre3*rawPrice3, numPre4*rawPrice4, numPre5*rawPrice5], 2))
        self.lineEdit_83.setText(f_QtSumList2Str([self.dataPurchase[0][11].text(),
                                                  self.dataPurchase[1][11].text(),
                                                  self.dataPurchase[2][11].text(),
                                                  self.dataPurchase[3][11].text(),
                                                  self.dataPurchase[4][11].text()]))
        self.lineEdit_84.setText(f_QtSumList2Str([self.dataPurchase[0][12].text(),
                                                  self.dataPurchase[1][12].text(),
                                                  self.dataPurchase[2][12].text(),
                                                  self.dataPurchase[3][12].text(),
                                                  self.dataPurchase[4][12].text()]))
        self.lineEdit_85.setText(f_QtSumList2Str([self.dataPurchase[0][13].text(),
                                                  self.dataPurchase[1][13].text(),
                                                  self.dataPurchase[2][13].text(),
                                                  self.dataPurchase[3][13].text(),
                                                  self.dataPurchase[4][13].text()]))
        self.lineEdit_128.setText(f_QtSumList2Str([self.dataPurchase[0][14].text(),
                                                   self.dataPurchase[1][14].text(),
                                                   self.dataPurchase[2][14].text(),
                                                   self.dataPurchase[3][14].text(),
                                                   self.dataPurchase[4][14].text()]))
        self.lineEdit_150.setText(f_QtSumList2Str([self.dataPurchase[0][19].text(),
                                                   self.dataPurchase[1][19].text(),
                                                   self.dataPurchase[2][19].text(),
                                                   self.dataPurchase[3][19].text(),
                                                   self.dataPurchase[4][19].text()]))
        self.lineEdit_156.setText(f_QtSumList2Str([self.dataPurchase[0][20].text(),
                                                   self.dataPurchase[1][20].text(),
                                                   self.dataPurchase[2][20].text(),
                                                   self.dataPurchase[3][20].text(),
                                                   self.dataPurchase[4][20].text()]))
        self.lineEdit_162.clear()
        if f_date(self.lineEdit_86.text()) is not None:
            self.lineEdit_162.setText(f_Qt2FloatStr((f_QtStr2Folat(self.dataPurchase[0][19].text()) +
                                                    f_QtStr2Folat(self.dataPurchase[0][19].text()) +
                                                    f_QtStr2Folat(self.dataPurchase[0][19].text()) +
                                                    f_QtStr2Folat(self.dataPurchase[0][19].text()) +
                                                    f_QtStr2Folat(self.dataPurchase[0][19].text()))
                                                    / f_QtStr2Folat(self.lineEdit_86.text()), 2))
        self.lineEdit_173.setText(f_QtSumList2Str([self.dataPurchase[0][22].text(),
                                                   self.dataPurchase[1][22].text(),
                                                   self.dataPurchase[2][22].text(),
                                                   self.dataPurchase[3][22].text(),
                                                   self.dataPurchase[4][22].text()]))     # 完成采购单数据的写入

        # 数据对比格
        self.lineEdit_111.clear()
        self.lineEdit_112.clear()
        self.lineEdit_113.clear()
        self.lineEdit_114.clear()
        self.lineEdit_115.clear()
        self.lineEdit_116.clear()
        self.lineEdit_117.clear()
        self.lineEdit_118.clear()
        self.lineEdit_175.clear()
        self.lineEdit_176.clear()
        self.lineEdit_177.clear()
        self.lineEdit_178.clear()
        self.lineEdit_179.clear()
        self.lineEdit_180.clear()

        self.amountRealNum = 0
        self.amountReal = 0
        if self.comboBox_7.currentText() in ['单一总额', ]:
            self.amountRealNum = f_QtStr2Folat(self.dataPurchase[0][12].text())

        elif self.comboBox_7.currentText() in ['整件计价', '单件用量']:
            if f_date(self.dataPurchase[0][8].text()) is not None:
                if f_date(self.dataPurchase[0][13].text()) is not None:
                    self.amountRealNum = (f_QtStr2Folat(self.dataPurchase[0][8].text())
                                          * f_QtStr2Folat(self.dataPurchase[0][13].text()) +
                                          f_QtStr2Folat(self.dataPurchase[1][8].text())
                                          * f_QtStr2Folat(self.dataPurchase[1][13].text()) +
                                          f_QtStr2Folat(self.dataPurchase[2][8].text())
                                          * f_QtStr2Folat(self.dataPurchase[2][13].text()) +
                                          f_QtStr2Folat(self.dataPurchase[3][8].text())
                                          * f_QtStr2Folat(self.dataPurchase[3][13].text()) +
                                          f_QtStr2Folat(self.dataPurchase[4][8].text())
                                          * f_QtStr2Folat(self.dataPurchase[4][13].text()))
                elif f_date(self.lineEdit_84.text()) is not None:
                    self.amountRealNum = f_QtStr2Folat(self.lineEdit_84.text())

                elif f_date(self.lineEdit_81.text()) is not None:
                    self.amountRealNum = f_QtStr2Folat(self.lineEdit_81.text())

        self.amountReal = (self.amountRealNum + f_QtStr2Folat(self.lineEdit_109.text()) -
                           f_QtStr2Folat(self.lineEdit_110.text()))
        self.lineEdit_111.setText(f_Qt2FloatStr(self.amountRealNum, 2))
        self.lineEdit_112.setText(f_Qt2FloatStr(self.amountReal, 2))

        if f_date(self.lineEdit_86) is not None:
            self.lineEdit_114.setText(
                f_Qt2FloatStr(f_QtStr2Folat(self.amountReal) / f_QtStr2Folat(self.lineEdit_86.text()), 2))
            self.lineEdit_113.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_114.text())/(1+f_QtStr2Folat(self.vatPur)/100), 2))

            self.lineEdit_176.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_86.text()) * f_QtStr2Folat(self.lineEdit_9.text()) - self.amountReal, 2))
            self.lineEdit_175.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_176.text()) / f_QtStr2Folat(self.lineEdit_86.text()), 2))

        if f_date(self.lineEdit_87) is not None:
            self.lineEdit_116.setText(
                f_Qt2FloatStr(f_QtStr2Folat(self.amountReal) / f_QtStr2Folat(self.lineEdit_87.text()), 2))
            self.lineEdit_115.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_116.text())/(1 + f_QtStr2Folat(self.vatPur) / 100), 2))

            self.lineEdit_178.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_87.text()) * f_QtStr2Folat(self.lineEdit_9.text()) - self.amountReal, 2))
            self.lineEdit_177.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_178.text()) / f_QtStr2Folat(self.lineEdit_87.text()), 2))

        if f_date(self.lineEdit_88) is not None:
            self.lineEdit_118.setText(
                f_Qt2FloatStr(f_QtStr2Folat(self.amountReal) / f_QtStr2Folat(self.lineEdit_88.text()), 2))
            self.lineEdit_117.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_118.text())/(1 + f_QtStr2Folat(self.vatPur) / 100), 2))

            self.lineEdit_180.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_88.text()) * f_QtStr2Folat(self.lineEdit_9.text()) - self.amountReal, 2))
            self.lineEdit_179.setText(f_Qt2FloatStr(
                f_QtStr2Folat(self.lineEdit_180.text()) / f_QtStr2Folat(self.lineEdit_88.text()), 2))

    def sameWastage(self):
        if self.checkBox_3.isChecked():
            for i in self.dataPurchase[1:]:
                for j in i[4:7]:
                    j.setText(self.dataPurchase[0][i.index(j) + 4].text())
                    j.setEnabled(False)
        else:
            for i in self.dataPurchase[1:]:
                for j in i[4:7]:
                    j.setEnabled(True)
                    j.clear()
        self.autoCalculate()

    def sameWeight(self):
        if self.checkBox_4.isChecked():
            self.lineEdit_43.setEnabled(False)
            self.lineEdit_41.setEnabled(False)
            self.lineEdit_44.setEnabled(False)
            self.lineEdit_40.setEnabled(False)
            self.lineEdit_43.setText(self.lineEdit_42.text())
            self.lineEdit_41.setText(self.lineEdit_42.text())
            self.lineEdit_44.setText(self.lineEdit_42.text())
            self.lineEdit_40.setText(self.lineEdit_42.text())
        else:
            self.lineEdit_43.setEnabled(True)
            self.lineEdit_41.setEnabled(True)
            self.lineEdit_44.setEnabled(True)
            self.lineEdit_40.setEnabled(True)
            self.lineEdit_43.clear()
            self.lineEdit_41.clear()
            self.lineEdit_44.clear()
            self.lineEdit_40.clear()
        self.autoCalculate()

    def sameWidth(self):
        if self.checkBox.isChecked():
            self.lineEdit_75.setEnabled(False)
            self.lineEdit_76.setEnabled(False)
            self.lineEdit_77.setEnabled(False)
            self.lineEdit_78.setEnabled(False)
            self.lineEdit_75.setText(self.lineEdit_79.text())
            self.lineEdit_76.setText(self.lineEdit_79.text())
            self.lineEdit_77.setText(self.lineEdit_79.text())
            self.lineEdit_78.setText(self.lineEdit_79.text())
        else:
            self.lineEdit_75.setEnabled(True)
            self.lineEdit_76.setEnabled(True)
            self.lineEdit_77.setEnabled(True)
            self.lineEdit_78.setEnabled(True)
            self.lineEdit_75.clear()
            self.lineEdit_76.clear()
            self.lineEdit_77.clear()
            self.lineEdit_78.clear()
        self.autoCalculate()

    def sameConsume(self):
        if self.checkBox_23.isChecked():
            self.lineEdit_2.setTeat(self.lineEdit_3.text())
            self.lineEdit_5.setTeat(self.lineEdit_3.text())
            self.lineEdit_4.setTeat(self.lineEdit_3.text())
            self.lineEdit_7.setTeat(self.lineEdit_3.text())
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_7.setEnabled(False)
        else:
            self.lineEdit_2.clear()
            self.lineEdit_5.clear()
            self.lineEdit_4.clear()
            self.lineEdit_7.clear()
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_7.setEnabled(True)
        self.autoCalculate()

    def samePrice(self):
        if self.checkBox_5.isChecked():
            print(self.lineEdit_35.text())
            self.lineEdit_38.setText(self.lineEdit_35.text())
            self.lineEdit_37.setText(self.lineEdit_35.text())
            self.lineEdit_39.setText(self.lineEdit_35.text())
            self.lineEdit_36.setText(self.lineEdit_35.text())
            self.lineEdit_38.setEnabled(False)
            self.lineEdit_37.setEnabled(False)
            self.lineEdit_39.setEnabled(False)
            self.lineEdit_36.setEnabled(False)

        else:
            self.lineEdit_38.clear()
            self.lineEdit_37.clear()
            self.lineEdit_39.clear()
            self.lineEdit_36.clear()
            self.lineEdit_38.setEnabled(True)
            self.lineEdit_37.setEnabled(True)
            self.lineEdit_39.setEnabled(True)
            self.lineEdit_36.setEnabled(True)

        self.autoCalculate()

    def sameColor(self):
        if self.checkBox_2.isChecked():
            self.checkBox_23.setChecked(True)
            self.checkBox_3.setChecked(True)
            self.checkBox_5.setChecked(True)
            self.checkBox.setChecked(True)
            self.checkBox_4.setChecked(True)
            self.checkBox_23.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            for i in self.dataPurchase[1:]:
                for j in i[1:]:
                    j.setEnabled(False)

        else:
            self.checkBox_23.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox.setChecked(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_23.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox_5.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            for i in self.dataPurchase[1:]:
                for j in i[1:]:
                    j.setEnabled(True)

    def itemChanged(self):
        self.item = str(self.comboBox_4.currentText()).strip()
        self.setWindowTitle('{:<20}{:<10}{:<25}{:<10}'
                            .format('单个物料采购审批表', self.staffName, self.remark, self.item))
        self.getBasicData()
        self.autoCalculate()

    def getBasicData(self):

        sql = 'select ' \
              '{} ' \
              'from plat225.quotation_info ' \
              'where remark = "{}";'.format(self.dict_item.get(self.item), self.remark)
        data_basic = getConn().query1(sql)

        custom = Custom(self.order.name_custom)
        self.vat = custom.quota_detail_with_vat

        self.lineEdit_10.clear()
        self.lineEdit.clear()


        if self.item in self.items[:5]:
            self.lineEdit_10.setVisible(True)
            self.label_7.setVisible(True)
            for i in self.groupQuota:
                i[2].clear()
                for j in i:
                    j.setVisible(True)

            if data_basic is not None:
                self.lineEdit.setText(str(data_basic[0]))
                self.lineEdit_10.setText(f_str_blank(data_basic[7]))
                self.groupQuota[0][2].setText(f_Qt2FloatStr(data_basic[1], 3))
                self.groupQuota[1][2].setText(f_Qt2FloatStr(data_basic[2], 2))
                self.groupQuota[3][2].setText(f_Qt2FloatStr(data_basic[3], 2))
                self.groupQuota[4][2].setText(f_Qt2FloatStr(self.vat, 2))
                self.groupQuota[5][2].setText(f_Qt2FloatStr(data_basic[6], 2))
                self.groupQuota[6][2].setText(f_Qt2FloatStr(
                    f_returnFloat(data_basic[6])/(1+f_returnFloat(self.vat)/100), 2))
                if data_basic[5] in ['a', 'A']:
                    self.groupQuota[2][0].setVisible(False)
                    self.groupQuota[2][1].setVisible(False)
                    self.groupQuota[2][2].setVisible(False)
                    self.groupQuota[3][1].setText('元/m')
                else:
                    self.groupQuota[2][2].setText(f_Qt2FloatStr(data_basic[4], 0))
                    self.groupQuota[3][1].setText('元/kgs')

        elif self.item in self.items[5:12]:
            self.lineEdit_10.setVisible(False)
            self.label_7.setVisible(False)
            for i in self.groupQuota:
                for j in i:
                    i[2].clear()
                    if self.groupQuota.index(i) >= 4:
                        j.setVisible(True)
                    else:
                        j.setVisible(False)
            if data_basic is not None:
                self.lineEdit.setText(str(data_basic[0] + data_basic[1]))
                self.groupQuota[4][2].setText(f_Qt2FloatStr(self.vat, 2))
                self.groupQuota[5][2].setText(f_Qt2FloatStr(data_basic[2], 2))
                self.groupQuota[6][2].setText(f_Qt2FloatStr(
                    f_returnFloat(data_basic[2])/(1+f_returnFloat(self.vat)/100), 2))
        else:
            self.lineEdit_10.setVisible(False)
            self.label_7.setVisible(False)
            for i in self.groupQuota:
                i[2].clear()
                for j in i:
                    j.setVisible(False)
        self.autoCalculate()

    def setNumCut(self):     # 设置数量表-裁数
        for i in self.numCutList:
            for j in i:
                j.clear()
                j.setVisible(True)
        if f_date(self.cutSize.color_1_num) is not None:
            i = self.numCutList[0]
            i[0].setText(str(self.cutSize.color_1_desc))
            i[1].setText(f_Qt2FloatStr(self.cutSize.color_1_num, 0))
        else:
            i = self.numCutList[0]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.cutSize.color_2_num) is not None:
            i = self.numCutList[1]
            i[0].setText(str(self.cutSize.color_2_desc))
            i[1].setText(f_Qt2FloatStr(self.cutSize.color_2_num, 0))
        else:
            i = self.numCutList[1]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.cutSize.color_3_num) is not None:
            i = self.numCutList[2]
            i[0].setText(str(self.cutSize.color_3_desc))
            i[1].setText(f_Qt2FloatStr(self.cutSize.color_3_num, 0))
        else:
            i = self.numCutList[2]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.cutSize.color_4_num) is not None:
            i = self.numCutList[3]
            i[0].setText(str(self.cutSize.color_4_desc))
            i[1].setText(f_Qt2FloatStr(self.cutSize.color_4_num, 0))
        else:
            i = self.numCutList[3]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.cutSize.color_5_num) is not None:
            i = self.numCutList[4]
            i[0].setText(str(self.cutSize.color_5_desc))
            i[1].setText(f_Qt2FloatStr(self.cutSize.color_5_num, 0))
        else:
            i = self.numCutList[4]
            i[0].setVisible(False)
            i[1].setVisible(False)

    def setNumOrder(self):      # 设置数量表-制单数
        for i in self.numOrderList:
            for j in i:
                j.clear()
                j.setVisible(True)
        if f_date(self.sizeCode.color_1_num) is not None:
            i = self.numOrderList[0]
            i[0].setText(str(self.sizeCode.color_1_desc))
            i[1].setText(f_Qt2FloatStr(self.sizeCode.color_1_num, 0))
        else:
            i = self.numOrderList[0]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.sizeCode.color_2_num) is not None:
            i = self.numOrderList[1]
            i[0].setText(str(self.sizeCode.color_2_desc))
            i[1].setText(f_Qt2FloatStr(self.sizeCode.color_2_num, 0))
        else:
            i = self.numOrderList[1]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.sizeCode.color_3_num) is not None:
            i = self.numOrderList[2]
            i[0].setText(str(self.sizeCode.color_3_desc))
            i[1].setText(f_Qt2FloatStr(self.sizeCode.color_3_num, 0))
        else:
            i = self.numOrderList[2]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.sizeCode.color_4_num) is not None:
            i = self.numOrderList[3]
            i[0].setText(str(self.sizeCode.color_4_desc))
            i[1].setText(f_Qt2FloatStr(self.sizeCode.color_4_num, 0))
        else:
            i = self.numOrderList[3]
            i[0].setVisible(False)
            i[1].setVisible(False)

        if f_date(self.sizeCode.color_5_num) is not None:
            i = self.numOrderList[4]
            i[0].setText(str(self.sizeCode.color_5_desc))
            i[1].setText(f_Qt2FloatStr(self.sizeCode.color_5_num, 0))
        else:
            i = self.numOrderList[4]
            i[0].setVisible(False)
            i[1].setVisible(False)

    def settingNumFormat(self):   # 根据 核价方式 设置显示格式后，再设置数值格式
        self.dataResource = self.comboBox_2.currentText()
        if self.comboBox_7.currentText() not in ['单一总额', '--']:

            if self.dataResource in ['裁数', '走货数']:
                if f_date(self.cutSize.color_2_num) is None:
                    for i in self.dataPurchase[1]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.cutSize.color_2_num) is not None:
                    for i in self.dataPurchase[1]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[1].index(i)].isHidden():
                            i.setVisible(True)

                if f_date(self.cutSize.color_3_num) is None:
                    for i in self.dataPurchase[2]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.cutSize.color_3_num) is not None:
                    for i in self.dataPurchase[2]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[2].index(i)].isHidden():
                            i.setVisible(True)

                if f_date(self.cutSize.color_4_num) is None:
                    for i in self.dataPurchase[3]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.cutSize.color_4_num) is not None:
                    for i in self.dataPurchase[3]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[3].index(i)].isHidden():
                            i.setVisible(True)

                if f_date(self.cutSize.color_5_num) is None:
                    for i in self.dataPurchase[4]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.cutSize.color_5_num) is not None:
                    for i in self.dataPurchase[4]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[4].index(i)].isHidden():
                            i.setVisible(True)

            if self.dataResource in ['制单数', ]:
                if f_date(self.sizeCode.color_2_num) is None:
                    for i in self.dataPurchase[1]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.sizeCode.color_2_num) is not None:
                    for i in self.dataPurchase[1]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[1].index(i)].isHidden():
                            i.setVisible(True)

                if f_date(self.sizeCode.color_3_num) is None:
                    for i in self.dataPurchase[2]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.sizeCode.color_3_num) is not None:
                    for i in self.dataPurchase[2]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[2].index(i)].isHidden():
                            i.setVisible(True)

                if f_date(self.sizeCode.color_4_num) is None:
                    for i in self.dataPurchase[3]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.sizeCode.color_4_num) is not None:
                    for i in self.dataPurchase[3]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[3].index(i)].isHidden():
                            i.setVisible(True)

                if f_date(self.sizeCode.color_5_num) is None:
                    for i in self.dataPurchase[4]:
                        if not i.isHidden():
                            i.setVisible(False)
                if f_date(self.sizeCode.color_5_num) is not None:
                    for i in self.dataPurchase[4]:
                        if i.isHidden() and not self.dataPurchase[0][self.dataPurchase[4].index(i)].isHidden():
                            i.setVisible(True)

    def calculateMethodChanged(self):
        if self.comboBox.currentText() == '长度计算':
            self.polity[6].setVisible(False)
            for i in self.labPur:
                i.setText(self.labText[1][self.labPur.index(i)])
            for i in self.dataPurchase:
                for j in i:
                    if i.index(j) in [7, 16]:
                        j.setVisible(False)
        else:
            self.polity[6].setVisible(True)
            for i in self.labPur:
                i.setText(self.labText[0][self.labPur.index(i)])
            for i in self.dataPurchase:
                for j in i:
                    if i.index(j) in [7, 16]:
                        j.setVisible(True)
        self.autoCalculate()

    def settingDisplay(self):
        self.dataResource = self.comboBox_2.currentText()
        self.comboBox_2.clear()
        self.comboBox_2.addItems(['制单数', '裁数', '走货数'])
        self.comboBox_2.setCurrentText(self.dataResource)
        if self.comboBox_7.currentText() == '--':
            for i in self.labPur:
                i.setVisible(False)
            for i in self.dataPurchase:
                for j in i:
                    j.setVisible(False)
            self.line_3.setVisible(False)
            self.line_4.setVisible(False)
            for i in self.total:
                i.setVisible(False)
            for i in self.polity:
                i.setVisible(False)
            self.label_13.setVisible(False)
            self.comboBox.setVisible(False)

        elif self.comboBox_7.currentText() == '单一总额':
            for i in self.labPur:
                if self.labPur.index(i) in [12, ]:
                    i.setVisible(True)
                else:
                    i.setVisible(False)
            for i in self.dataPurchase:
                for j in i:
                    if self.dataPurchase.index(i) == 0 and i.index(j) == 12:
                        j.setVisible(True)
                    else:
                        j.setVisible(False)
            self.line_3.setVisible(False)
            self.line_4.setVisible(False)
            for i in self.total:
                if self.total.index(i) in [0, 1, 2, 6]:
                    i.setVisible(True)
                else:
                    i.setVisible(False)
            for i in self.polity:
                i.setVisible(False)
            self.label_13.setVisible(False)
            self.comboBox.setVisible(False)

        elif self.comboBox_7.currentText() == '整件计价':
            for i in self.labPur:
                i.setText(self.labText[2][self.labPur.index(i)])
                if self.labPur.index(i) in [0, 1, 6, 8, 9, 10, 11, 12, 13]:
                    i.setVisible(True)
                else:
                    i.setVisible(False)
            for i in self.dataPurchase:
                for j in i:
                    if i.index(j) in [0, 1, 6, 8, 9, 10, 11, 12, 13]:
                        j.setVisible(True)
                    else:
                        j.setVisible(False)
            self.line_3.setVisible(True)
            self.line_4.setVisible(True)
            for i in self.total:
                if self.total.index(i) in [0, 1, 2, 3, 4, 5, 6, 7]:
                    i.setVisible(True)
                else:
                    i.setVisible(False)
            for i in self.polity:
                if self.polity.index(i) in [0, 1, 3, 4]:
                    i.setVisible(True)
                else:
                    i.setVisible(False)
            self.label_13.setVisible(False)
            self.comboBox.setVisible(False)

            if self.dataResource == '走货数':
                self.checkBox_2.setEnabled(False)
                self.checkBox_2.setChecked(True)
                self.sameColor()
            else:
                self.checkBox_2.setEnabled(True)

        elif self.comboBox_7.currentText() == '单件用量':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(['制单数', '裁数'])
            self.checkBox_2.setEnabled(True)
            if self.dataResource == '走货数':
                self.comboBox_2.setCurrentText('制单数')
            else:
                self.comboBox_2.setCurrentText(self.dataResource)
            self.label_13.setVisible(True)
            self.lineEdit.setVisible(True)
            self.comboBox.setVisible(True)
            self.line_3.setVisible(True)
            self.line_4.setVisible(True)
            if self.comboBox.currentText() == '长度计算':
                for i in self.labPur:
                    i.setText(self.labText[1][self.labPur.index(i)])
                    i.setVisible(True)
                for i in self.polity:
                    if self.polity.index(i) not in [6, ]:
                        i.setVisible(True)
                    else:
                        i.setVisible(False)
                for i in self.dataPurchase:
                    for j in i:
                        if i.index(j) in [7, 16, ]:
                            j.setVisible(False)
                        else:
                            j.setVisible(True)
                for i in self.total:
                    i.setVisible(True)
            else:
                for i in self.labPur:
                    i.setText(self.labText[0][self.labPur.index(i)])
                    i.setVisible(True)
                for i in self.polity:
                    i.setVisible(True)
                for i in self.dataPurchase:
                    for j in i:
                        j.setVisible(True)
                for i in self.total:
                    i.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AuditDetail('俞龙平', 'PF2104PF2104002', '【f1】')
    main.show()
    sys.exit(app.exec_())
