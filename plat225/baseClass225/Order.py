from baseClass225.QuotaInfo import QuoInfo
from func.getConn import getConn
from func.update_1_table import update_1_data
import datetime
from func.f_change import f_Qt2Date


class Order(QuoInfo):
    def __init__(self, remark):
        super().__init__(remark)
        self.remark = str(remark).strip()

        sql = 'select ' \
              'id_order, name_mer, name_custom, name_order, price_order, num_order, ' \
              'date_order, date_mer, num_cut, num_ship, date_ship_finish, amount_deduction, ' \
              'desc_deduction, amount_addition, desc_addition, ' \
              'date_1_ship, num_1_ship, amount_1_ship, date_1_pay, ship_1_remark, ' \
              'date_2_ship, num_2_ship, amount_2_ship, date_2_pay, ship_2_remark, ' \
              'date_3_ship, num_3_ship, amount_3_ship, date_3_pay, ship_3_remark, ' \
              'date_4_ship, num_4_ship, amount_4_ship, date_4_pay, ship_4_remark, ' \
              'date_5_ship, num_5_ship, amount_5_ship, date_5_pay, ship_5_remark, ' \
              'date_6_ship, num_6_ship, amount_6_ship, date_6_pay, ship_6_remark, ' \
              'date_7_ship, num_7_ship, amount_7_ship, date_7_pay, ship_7_remark, ' \
              'date_8_ship, num_8_ship, amount_8_ship, date_8_pay, ship_8_remark, ' \
              'percent_1_order, pay_1_order, date_pay1_order, desc_pay1, ' \
              'percent_2_order, pay_2_order, date_pay2_order, desc_pay2, ' \
              'percent_3_order, pay_3_order, date_pay3_order, desc_pay3, ' \
              'sew_as_fob, amount_total_collected, order_stage_for_mer, days_from_order_date, ' \
              'flag_collect_finish, flag_all_finish, month_product, ' \
              'date_ship_up90, date_cut, data_code_sew, num_process, date_sew_plan_finish, ' \
              'order_update_time, cm_only, sew_num_total, date_sew_last_all_back, ' \
              'amount_shipment, amount_should_collect_now ' \
              'from plat225.order_info ' \
              'where remark = "{}";'.format(self.remark)
        data = getConn().query1(sql)

        if data is None:
            [self.id_order, self.name_mer, self.name_custom, self.name_order, self.price_order, self.num_order,
             self.date_order, self.date_mer, self.num_cut, self.num_ship, self.date_ship_finish, self.amount_deduction,
             self.desc_deduction, self.amount_addition, self.desc_addition,
             self.date_1_ship, self.num_1_ship, self.amount_1_ship, self.date_1_pay, self.ship_1_remark,
             self.date_2_ship, self.num_2_ship, self.amount_2_ship, self.date_2_pay, self.ship_2_remark,
             self.date_3_ship, self.num_3_ship, self.amount_3_ship, self.date_3_pay, self.ship_3_remark,
             self.date_4_ship, self.num_4_ship, self.amount_4_ship, self.date_4_pay, self.ship_4_remark,
             self.date_5_ship, self.num_5_ship, self.amount_5_ship, self.date_5_pay, self.ship_5_remark,
             self.date_6_ship, self.num_6_ship, self.amount_6_ship, self.date_6_pay, self.ship_6_remark,
             self.date_7_ship, self.num_7_ship, self.amount_7_ship, self.date_7_pay, self.ship_7_remark,
             self.date_8_ship, self.num_8_ship, self.amount_8_ship, self.date_8_pay, self.ship_8_remark,
             self.percent_1_order, self.pay_1_order, self.date_pay1_order, self.desc_pay1,
             self.percent_2_order, self.pay_2_order, self.date_pay2_order, self.desc_pay2,
             self.percent_3_order, self.pay_3_order, self.date_pay3_order, self.desc_pay3,
             self.sew_as_fob, self.amount_total_collected, self.order_stage_for_mer, self.days_from_order_date,
             self.flag_collect_finish, self.flag_all_finish, self.month_product,
             self.date_ship_up90, self.date_cut, self.data_code_sew, self.num_process,
             self.date_sew_plan_finish, self.order_update_time, self.cm_only, self.sew_num_total,
             self.date_sew_last_all_back, self.amount_shipment, self.amount_should_collect_now] = [None] * 85

        else:
            [self.id_order, self.name_mer, self.name_custom, self.name_order, self.price_order, self.num_order,
             self.date_order, self.date_mer, self.num_cut, self.num_ship, self.date_ship_finish, self.amount_deduction,
             self.desc_deduction, self.amount_addition, self.desc_addition,
             self.date_1_ship, self.num_1_ship, self.amount_1_ship, self.date_1_pay, self.ship_1_remark,
             self.date_2_ship, self.num_2_ship, self.amount_2_ship, self.date_2_pay, self.ship_2_remark,
             self.date_3_ship, self.num_3_ship, self.amount_3_ship, self.date_3_pay, self.ship_3_remark,
             self.date_4_ship, self.num_4_ship, self.amount_4_ship, self.date_4_pay, self.ship_4_remark,
             self.date_5_ship, self.num_5_ship, self.amount_5_ship, self.date_5_pay, self.ship_5_remark,
             self.date_6_ship, self.num_6_ship, self.amount_6_ship, self.date_6_pay, self.ship_6_remark,
             self.date_7_ship, self.num_7_ship, self.amount_7_ship, self.date_7_pay, self.ship_7_remark,
             self.date_8_ship, self.num_8_ship, self.amount_8_ship, self.date_8_pay, self.ship_8_remark,
             self.percent_1_order, self.pay_1_order, self.date_pay1_order, self.desc_pay1,
             self.percent_2_order, self.pay_2_order, self.date_pay2_order, self.desc_pay2,
             self.percent_3_order, self.pay_3_order, self.date_pay3_order, self.desc_pay3,
             self.sew_as_fob, self.amount_total_collected, self.order_stage_for_mer, self.days_from_order_date,
             self.flag_collect_finish, self.flag_all_finish, self.month_product,
             self.date_ship_up90, self.date_cut, self.data_code_sew, self.num_process,
             self.date_sew_plan_finish, self.order_update_time, self.cm_only, self.sew_num_total,
             self.date_sew_last_all_back, self.amount_shipment, self.amount_should_collect_now] = data

            days_from_order_date = self.days_from_order_date

            if f_Qt2Date(self.date_order) is not None and self.flag_all_finish != 1:
                self.days_from_order_date = self.date_order.toordinal() - datetime.datetime.today().toordinal()
            else:
                self.days_from_order_date = None
            if days_from_order_date != self.days_from_order_date:
                update_1_data(tab='order_info',
                              fields=['days_from_order_date', ],
                              new_values=[self.days_from_order_date, ],
                              field_constraint='remark',
                              value_constraint=self.remark)


if __name__ == '__main__':
    a = Order('CH210303 ')
    print(a.mini_price, a.remark, a.id_quotation)
    print(a.percent_1_order, a.mini_price, a.id_quotation, a.remark, a.cm_only,
          a.num_order, a.sew_num_total, a.num_process, a.num_cut, a.date_sew_last_all_back, a.quota_create_time)
