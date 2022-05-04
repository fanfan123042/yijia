from func.getConn import getConn
from baseClass225.Order import Order


# from func.get_data import get_columns_data
# all_sew = get_columns_data(table='sew_info', fields=['remark', 'code_sew'], db=219)
# print(len(all_sew), all_sew)


class Sew(Order):
    """
    车缝订单, 从 Order 处继承, Alan 220327
    """
    def __init__(self, remark, code_sew):
        super().__init__(remark)

        self.remark = str(remark).strip()
        self.code_sew = str(code_sew).strip()

        sql = 'select ' \
              'id_sew, sew_responsible, sew_create_time, sew_remark, style_type, num_sew, process, ' \
              'status_difficulty, sew_price, ' \
              'date_contract_sign, date_contract_sew_back, date_sew_back, ' \
              'eva_delivery, eva_quality, eva_first_tie, eva_rework, ' \
              'score_delivery, score_quality, score_first_tie, score_rework, ' \
              'score_sew_price, score_sew, ' \
              'correct_process, correct_num, correct_difficulty, ' \
              'ratio_sew_price, weighting_ratio_s_p, ' \
              'date_sew_pay_submit, sew_degree, ' \
              'sew_status, sew_update_time ' \
              'from plat225.sew_info ' \
              'where remark = "{}" and code_sew = "{}";'.format(self.remark, self.code_sew)
        data_sew = getConn().query1(sql)
        if data_sew is None:
            [self.id_sew, self.sew_responsible, self.sew_create_time, self.sew_remark, self.style_type,
             self.num_sew, self.process, self.status_difficulty, self.sew_price,
             self.date_contract_sign, self.date_contract_sew_back, self.date_sew_back,
             self.eva_delivery, self.eva_quality, self.eva_first_tie, self.eva_rework,
             self.score_delivery, self.score_quality, self.score_first_tie, self.score_rework,
             self.score_sew_price, self.score_sew,
             self.correct_process, self.correct_num, self.correct_difficulty,
             self.ratio_sew_price, self.weighting_ratio_s_p,
             self.date_sew_pay_submit, self.sew_degree,
             self.sew_status, self.update_time] = [None] * 31
        else:
            [self.id_sew, self.sew_responsible, self.sew_create_time, self.sew_remark, self.style_type,
             self.num_sew, self.process, self.status_difficulty, self.sew_price,
             self.date_contract_sign, self.date_contract_sew_back, self.date_sew_back,
             self.eva_delivery, self.eva_quality, self.eva_first_tie, self.eva_rework,
             self.score_delivery, self.score_quality, self.score_first_tie, self.score_rework,
             self.score_sew_price, self.score_sew,
             self.correct_process, self.correct_num, self.correct_difficulty,
             self.ratio_sew_price, self.weighting_ratio_s_p,
             self.date_sew_pay_submit, self.sew_degree,
             self.sew_status, self.update_time] = data_sew


if __name__ == '__main__':
    a = Sew('伊美源910531286', '王东虎门')
    print(a.num_order, a.num_cut, a.sew_num_total, a.num_sew)

