from func.getConn import getConn


class Staff:
    def __init__(self, staff):
        if str(staff).isdigit():
            self.id = int(staff)
            sql = 'select name, gender, Mobile, e_mail, position, record_time, not_on_job, password, ifttt_code ' \
                  'from plat225.staff_info ' \
                  'where id_staff = {};'.format(self.id)
            data = getConn().query1(sql)
            if data is None:
                [self.name, self.gender, self.mobile, self.email,
                 self.position, self.startTime, self.notOnJob, self.password, self.ifttt_code] = [None] * 9
            else:
                (self.name, self.gender, self.mobile, self.email,
                 self.position, self.startTime, self.notOnJob, self.password, self.ifttt_code) = data

        else:
            self.name = staff.strip().title()
            sql = 'select id_staff, gender, Mobile, e_mail, position, record_time, not_on_job, password, ifttt_code ' \
                  'from plat225.staff_info ' \
                  'where name = "{}"'.format(self.name)
            data = getConn().query1(sql)
            if data is None:
                [self.id, self.gender, self.mobile, self.email,
                 self.position, self.startTime, self.notOnJob, self.password, self.ifttt_code] = [None] * 9
            else:
                (self.id, self.gender, self.mobile, self.email,
                 self.position, self.startTime, self.notOnJob, self.password, self.ifttt_code) = data



