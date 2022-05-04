from func.getConn import getConn


class SewCode:
    def __init__(self, code_sew):
        self.code_sew = str(code_sew).strip()
        sql = 'select ' \
              'id_sew_basic, name_sew, location_sew, founding_time, contact_person, ' \
              'mobile_contact, num_sewer, num_ironing, good_category, ' \
              'attitude_boss, ability_mng, percent_major, credit, score_static, ' \
              'date_pass, date_update, updater ' \
              'from sew_basic_info ' \
              'where code_sew = "{}";'.format(self.code_sew)
        data = getConn().query1(sql)
        if data is None:
            [self.id_sew_basic, self.name_sew, self.location_sew, self.founding_time, self.contact_person,
             self.mobile_contact, self.num_sewer, self.num_ironing, self.good_category, self.attitude_boss,
             self.ability_mng, self.percent_major, self.credit, self.score_static, self.date_pass,
             self.date_update, self.updater] = [None] * 17
        else:
            [self.id_sew_basic, self.name_sew, self.location_sew, self.founding_time, self.contact_person,
             self.mobile_contact, self.num_sewer, self.num_ironing, self.good_category, self.attitude_boss,
             self.ability_mng, self.percent_major, self.credit, self.score_static, self.date_pass,
             self.date_update, self.updater] = data


class CodeSewFind:
    def __init__(self, code_sew):
        sql = 'select ' \
              'code_sew ' \
              'from sew_basic_info ' \
              'where code_sew like "%{}%";'.format(str(code_sew).strip())
        data = getConn().queryAll(sql)
        if len(data) == 0:
            self.code_sew_list = []
        else:
            self.code_sew_list = [i[0] for i in data]


if __name__ == '__main__':
    a = CodeSewFind('银')
    print(a.code_sew_list)
    b = SewCode('舒占银')
    print(b.id_sew_basic, b.name_sew, b.founding_time, b.ability_mng)
