import add_path_for_bat
from func.getConn import getConn


class OrderAudit:
    def __init__(self, remark):
        sql = 'select ' \
              'id_order_audit, remark, name_mer, ' \
              'bom_not_finish, bom_finished, cm_not_finish, cm_finished, ' \
              'extra_not_finish, extra_finished, all_finished, ' \
              'create_time, update_time, updater ' \
              'from plat225.order_audit ' \
              'where remark = "{}";'.format(str(remark).strip())
        data = getConn().query1(sql)
        if data is None:
            [self.id_order_audit, self.remark, self.name_mer,
             self.bom_not_finish, self.bom_finished, self.cm_not_finish, self.cm_finished,
             self.extra_not_finish, self.extra_finished, self.all_finished,
             self.create_time, self.update_time, self.updater] = [None] * 13
        else:
            [self.id_order_audit, self.remark, self.name_mer,
             self.bom_not_finish, self.bom_finished, self.cm_not_finish, self.cm_finished,
             self.extra_not_finish, self.extra_finished, self.all_finished,
             self.create_time, self.update_time, self.updater] = data


if __name__ == '__main__':
    remark = 'PFPF2107022'
    o = OrderAudit(remark)
    print(o.all_finished, o.cm_finished, o.bom_finished, o.bom_not_finish, o.cm_not_finish)
