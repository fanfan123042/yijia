from func.getConn import getConn


class NumCut_Size:
    def __init__(self, remark):
        self.remark = str(remark).strip()
        sql = 'select ' \
              'id_numCut_size, num_total, size_code, ' \
              'color_1_desc, color_1_detail, color_1_num, ' \
              'color_2_desc, color_2_detail, color_2_num, ' \
              'color_3_desc, color_3_detail, color_3_num, ' \
              'color_4_desc, color_4_detail, color_4_num, ' \
              'color_5_desc, color_5_detail, color_5_num, ' \
              'create_time, update_time, creater, updater ' \
              'from plat225.numcut_size ' \
              'where remark = "{}";'.format(self.remark)
        data = getConn().query1(sql)
        if data is None:
            [self.id_numOrder_size, self.num_total, self.size_code,
             self.color_1_desc, self.color_1_detail, self.color_1_num,
             self.color_2_desc, self.color_2_detail, self.color_2_num,
             self.color_3_desc, self.color_3_detail, self.color_3_num,
             self.color_4_desc, self.color_4_detail, self.color_4_num,
             self.color_5_desc, self.color_5_detail, self.color_5_num,
             self.create_time, self.update_time, self.creater, self.updater] = [None] * 22
        else:
            [self.id_numOrder_size, self.num_total, self.size_code,
             self.color_1_desc, self.color_1_detail, self.color_1_num,
             self.color_2_desc, self.color_2_detail, self.color_2_num,
             self.color_3_desc, self.color_3_detail, self.color_3_num,
             self.color_4_desc, self.color_4_detail, self.color_4_num,
             self.color_5_desc, self.color_5_detail, self.color_5_num,
             self.create_time, self.update_time, self.creater, self.updater] = data

