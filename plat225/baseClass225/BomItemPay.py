from func.getConn import getConn


class BomItemPay:
    def __init__(self, remark, item):
        self.remark = str(remark).strip()
        self.item = str(item).strip()

        sql = 'select ' \
              'id_audit_pay, amount_all_should_pay, purchase_vat, amount_all_without_vat, ' \
              'pay_desc1, amount_suggest1, amount_for_check1, submitter1, submit_time1, ' \
              'amount_check1, account_check1, unit_price_check1, pay_assessor1, audit_time1, ' \
              'pay_desc2, amount_suggest2, amount_for_check2, submitter2, submit_time2, ' \
              'amount_check2, account_check2, unit_price_check2, pay_assessor2, audit_time2, ' \
              'pay_desc3, amount_suggest3, amount_for_check3, submitter3, submit_time3, ' \
              'amount_check3, account_check3, unit_price_check3, pay_assessor3, audit_time3, ' \
              'pay_desc4, amount_suggest4, amount_for_check4, submitter4, submit_time4, ' \
              'amount_check4, account_check4, unit_price_check4, pay_assessor4, audit_time4, ' \
              'pay_desc5, amount_suggest5, amount_for_check5, submitter5, submit_time5, ' \
              'amount_check5, account_check5, unit_price_check5, pay_assessor5, audit_time5, ' \
              'amount_quota_without_vat, amount_checked_without_vat, amount_unchecked_without_vat, audit_remark, ' \
              'account_uni_code1, account_uni_code2, account_uni_code3, account_uni_code4, account_uni_code5 ' \
              'from plat225.bom_audit_pay ' \
              'where remark = "{}" and item = "{}";'.format(self.remark, self.item)
        data = getConn().query1(sql)
        if data is None:
            [self.id_audit_pay, self.amount_all_should_pay, self.purchase_vat, self.amount_all_without_vat,
             self.pay_desc1, self.amount_suggest1, self.amount_for_check1, self.submitter1, self.submit_time1,
             self.amount_check1, self.account_check1, self.unit_price_check1, self.pay_assessor1, self.audit_time1,
             self.pay_desc2, self.amount_suggest2, self.amount_for_check2, self.submitter2, self.submit_time2,
             self.amount_check2, self.account_check2, self.unit_price_check2, self.pay_assessor2, self.audit_time2,
             self.pay_desc3, self.amount_suggest3, self.amount_for_check3, self.submitter3, self.submit_time3,
             self.amount_check3, self.account_check3, self.unit_price_check3, self.pay_assessor3, self.audit_time3,
             self.pay_desc4, self.amount_suggest4, self.amount_for_check4, self.submitter4, self.submit_time4,
             self.amount_check4, self.account_check4, self.unit_price_check4, self.pay_assessor4, self.audit_time4,
             self.pay_desc5, self.amount_suggest5, self.amount_for_check5, self.submitter5, self.submit_time5,
             self.amount_check5, self.account_check5, self.unit_price_check5, self.pay_assessor5, self.audit_time5,
             self.amount_quota_without_vat, self.amount_checked_without_vat,
             self.amount_unchecked_without_vat, self.audit_remark,
             self.account_uni_code1, self.account_uni_code2, self.account_uni_code3,
             self.account_uni_code4, self.account_uni_code5] = [None] * 63
        else:
            [self.id_audit_pay, self.amount_all_should_pay, self.purchase_vat, self.amount_all_without_vat,
             self.pay_desc1, self.amount_suggest1, self.amount_for_check1, self.submitter1, self.submit_time1,
             self.amount_check1, self.account_check1, self.unit_price_check1, self.pay_assessor1, self.audit_time1,
             self.pay_desc2, self.amount_suggest2, self.amount_for_check2, self.submitter2, self.submit_time2,
             self.amount_check2, self.account_check2, self.unit_price_check2, self.pay_assessor2, self.audit_time2,
             self.pay_desc3, self.amount_suggest3, self.amount_for_check3, self.submitter3, self.submit_time3,
             self.amount_check3, self.account_check3, self.unit_price_check3, self.pay_assessor3, self.audit_time3,
             self.pay_desc4, self.amount_suggest4, self.amount_for_check4, self.submitter4, self.submit_time4,
             self.amount_check4, self.account_check4, self.unit_price_check4, self.pay_assessor4, self.audit_time4,
             self.pay_desc5, self.amount_suggest5, self.amount_for_check5, self.submitter5, self.submit_time5,
             self.amount_check5, self.account_check5, self.unit_price_check5, self.pay_assessor5, self.audit_time5,
             self.amount_quota_without_vat, self.amount_checked_without_vat,
             self.amount_unchecked_without_vat, self.audit_remark,
             self.account_uni_code1, self.account_uni_code2, self.account_uni_code3,
             self.account_uni_code4, self.account_uni_code5] = data

if __name__ == '__main__':
    pay = BomItemPay('PF2104PF2104002', '【f1】')
    print(pay.audit_time3)