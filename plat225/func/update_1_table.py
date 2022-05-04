from func.getConn import getConn
from func.MistakeForSystem import mistake_log


def update_1_data(tab='', fields=(), new_values=(), field_constraint='', value_constraint='', sign='=', db=225):
    """
    逐行更新数据库的数据, 2021-11-13 更新, 已做过测试
    alan 21-11-12
    :param tab: 【表格名】
    :param fields: 【字段】--可以为单个，也可以为多个的 list 或 tuple
    :param new_values:  【值】--和【字段】相对应的单个或多个的 list 及 tuple
    :param field_constraint:   【查询字段】--单个
    :param sign: 比较符号，比如'>', '<', '=', 'like' 等
    :param value_constraint:   【查询值】--单个，在考虑单一性问题
    :param db 传入到 getConn 的数据库
    :return:None
    """
    if type(fields) not in [list, tuple] or type(new_values) not in [list, tuple]:
        act = '数据库{} update 时, 字段 或 更新值 数据类型不对, 只能为 list 或 tuple'.format(tab)
        print(act)
        mistake_log(act)
    elif len(fields) == 0 or len(new_values) != len(fields):
        act = '数据库{} update 时, 字段 或 更新值 为空 或 长度不相等'.format(tab)
        print(act)
        mistake_log(act)
    else:
        str2 = ''
        str1 = 'update {} set '.format(tab)
        for i in range(len(fields)):
            if new_values[i] is None:
                str2 = str2 + ', %s = Null' % (str(fields[i]))
            elif type(new_values[i]) in [int, float]:
                str2 = str2 + ', %s = %s' % (str(fields[i]), new_values[i])
            else:
                str2 = str2 + ', %s = "%s"' % (str(fields[i]), new_values[i])
        if value_constraint is None:
            str3 = ' where %s is Null;' % field_constraint
        elif type(value_constraint) in [int, float]:
            str3 = ' where %s %s %s;' % (field_constraint, sign, value_constraint)
        else:
            str3 = ' where %s %s "%s";' % (field_constraint, sign, value_constraint)
        sql_str = str1 + str2[2:] + str3
        getConn(db).update1(sql_str)


def update_1_data_many_constraint(tab='', fields=(), new_values=(),
                                  field_constraint=(), value_constraint=(), operator='and',
                                  sign='=', db=225):
    """
    逐行更新数据库的数据, 2021-11-13 更新, 已做过测试
    alan 21-12-23
    :param tab: 【表格名】
    :param fields: 【字段】--可以为单个，也可以为多个的 list 或 tuple
    :param new_values:  【值】--和【字段】相对应的单个或多个的 list 及 tuple
    :param field_constraint:   【查询字段】--单个
    :param sign: 比较符号，比如'>', '<', '=', 'like' 等
    :param value_constraint:   【查询值】--单个，在考虑单一性问题
    :param operator: 运算符 and 或 or
    :param db 传入到 getConn 的数据库
    :return:None
    """
    if type(fields) not in [list, tuple] or type(new_values) not in [list, tuple]:
        act = '数据库{} update 时, 字段 或 更新值 数据类型不对, 只能为 list 或 tuple'.format(tab)
        print(act)
        mistake_log(act)
    elif len(fields) == 0 or len(new_values) != len(fields):
        act = '数据库{} update 时, 更新字段或更新值为空或长度不相等'.format(tab)
        print(act)
        mistake_log(act)
    elif len(field_constraint) != len(value_constraint):
        act = '数据库{} 多条件update时, field_constraint和value_constraint长度不相等'.format(tab)
        print(act)
        mistake_log(act)
    else:
        str2 = ''
        str1 = 'update {} set '.format(tab)
        for i in range(len(fields)):
            if new_values[i] is None:
                str2 = str2 + ', %s = Null' % (str(fields[i]))
            elif type(new_values[i]) in [int, float]:
                str2 = str2 + ', %s = %s' % (str(fields[i]), new_values[i])
            else:
                str2 = str2 + ', %s = "%s"' % (str(fields[i]), new_values[i])

        str3 = ' where'
        str4 = ';'
        for j in range(len(field_constraint)):
            if j == 0:
                if value_constraint[j] is None:
                    str3 = str3 + ' %s is Null' % (str(field_constraint[j]))
                elif type(value_constraint[j]) in [int, float]:
                    str3 = str3 + ' %s %s %s' % (field_constraint[j], sign, value_constraint[j])
                else:
                    str3 = str3 + ' %s %s "%s"' % (field_constraint[j], sign, value_constraint[j])
            else:
                if value_constraint[j] is None:
                    str3 = str3 + ' %s %s is Null' % (operator, str(field_constraint[j]))
                elif type(value_constraint[j]) in [int, float]:
                    str3 = str3 + ' %s %s %s %s' % (operator, field_constraint[j], sign, value_constraint[j])
                else:
                    str3 = str3 + ' %s %s %s "%s"' % (operator, field_constraint[j], sign, value_constraint[j])

        sql_str = str1 + str2[2:] + str3 + str4
        # print(sql_str)
        getConn(db).update1(sql_str)


if __name__ == '__main__':
    update_1_data_many_constraint(tab='test',
                                  fields=['红', 'huang', 'gery', 'green'],
                                  new_values=[None, 2000, 90, 566],
                                  operator='and',
                                  sign='=',
                                  field_constraint=['remark', 'color', 'price'],
                                  value_constraint=['胡来', 'hua', None])
