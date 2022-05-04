from func.getConn import getConn
import datetime


class Custom:
    def __init__(self, custom):
        self.name_custom = str(custom).strip()
        sql = 'select ' \
              'id_custom, first_order, with_vat, money_unit, ' \
              'quota_detail_with_vat, type_payment, remark, unit_commission ' \
              'from custom_info ' \
              'where name_custom = "{}";'.format(self.name_custom)
        data = getConn().query1(sql)
        if data is None:
            [self.id_custom, self.first_order, self.with_vat, self.money_unit,
             self.quota_detail_with_vat, self.type_payment, self.custom_remark, self.unit_commission] = [None] * 8
        else:
            [self.id_custom, self.first_order, self.with_vat, self.money_unit,
             self.quota_detail_with_vat, self.type_payment, self.custom_remark, self.unit_commission] = data

        sql_mer = 'select ' \
                  'name_mer, remark ' \
                  'from order_info ' \
                  'where name_custom = "{}";'.format(self.name_custom)
        dataMer = getConn().queryAll(sql_mer)
        if len(dataMer) == 0:
            self.mer = None
            self.remarkList = None
        else:
            self.mer = list(set([i[0] for i in dataMer]))
            self.remarkList = list(set([i[1] for i in dataMer]))


class CustomFind:
    def __init__(self, custom):
        sql = 'select ' \
              'name_custom ' \
              'from custom_info ' \
              'where name_custom like "%{}%";'.format(str(custom).strip())
        data = getConn().queryAll(sql)
        if len(data) == 0:
            self.custom_list = []
        else:
            self.custom_list = [i[0] for i in data]


class CustomOrder:
    def __init__(self, custom, days=0):
        self.name = str(custom).strip()
        sql = 'select ' \
              'date_order, price_order, num_order, price_order*num_order ' \
              'from order_info ' \
              'where name_custom = "{}";'.format(self.name)
        self.orderDataAll = getConn().queryAll(sql)
        if len(self.orderDataAll) > 0:
            self.orderDataToNow = [i for i in self.orderDataAll
                                   if (i[0].toordinal() + days) > datetime.datetime.today().toordinal()]
            self.amountOrderToNow = sum([i[3] for i in self.orderDataAll
                                         if (i[0].toordinal() + days) > datetime.datetime.today().toordinal()])
            self.numOrderToNow = sum([i[2] for i in self.orderDataAll
                                     if (i[0].toordinal() + days) > datetime.datetime.today().toordinal()])
        else:
            self.orderDataToNow = []
            self.amountOrderToNow = 0
            self.numOrderToNow = 0


if __name__ == '__main__':
    a = Custom('wjj')
    print(a.type_payment, a.unit_commission, a.quota_detail_with_vat, a.money_unit, a.first_order)
    b = CustomFind('wjj')
    print(len(b.custom_list))
    print(len(a.remarkList))
    print(a.mer)
    d = CustomOrder('wjj', days=100)
    print(d.numOrderToNow, d.amountOrderToNow, len(d.orderDataToNow))
