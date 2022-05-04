from func.MistakeForSystem import mistake_log
from func.getConn import getConn


def insert_1_data(tab='', fields=(), new_value=(), db=225):
    """
    插入一行数据到 1个表格，如有必要，后续可以改成多项表格，有报错机制
    alan 21-11-12 重新修改程序
    :param tab: 表格名
    :param fields: 字段名, 可以用 list 或 tuple
    :param new_value: 值, 可以用 list 或 tuple
    :param db 传入到 getConn 的数据库
    :return:
    """
    str2 = ''
    str4 = ''

    if type(fields) not in [list, tuple] or type(new_value) not in [list, tuple]:
        act = '数据库{} insert 时, 字段 或 插入值 数据类型不对, 只能为 list 或 tuple'.format(tab)
        print(act)
        mistake_log(act)
    elif len(fields) == 0 or len(new_value) != len(fields):
        act = '数据库{} insert 时, 字段 或 插入值 为空 或 长度不相等'.format(tab)
        print(act)
        mistake_log(act)
    else:
        str1 = 'insert into {} ('.format(tab)
        for i in range(len(fields)):
            str2 = str2 + ', {}'.format(fields[i])
            if new_value[i] is None:
                str4 = str4 + ''', Null'''
            elif type(new_value[i]) in [int, float]:
                str4 = str4 + ''', {}'''.format(new_value[i])
            else:
                str4 = str4 + ''', "{}"'''.format(new_value[i])
        str3 = ') VALUES ('
        str5 = ');'
        sql_str = str1 + str2[2:] + str3 + str4[2:] + str5
        getConn(db).update1(sql_str)
