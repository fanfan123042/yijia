import datetime


def f_str(x):
    """
    返回 None 或 原字符，即过滤 空格等符号
    :param x:
    :return:
    """
    if x in ([0, '0', '', None] + [' '*i for i in range(1, 10)]):
        x = None
    return x


def f_str_blank(x):
    if x in ([0, '0', '', None, '0.0', '0.00', 'None', 'ne'] + [' '*i for i in range(1, 10)]):
        x = ''
    return x


def f_date2str_blank(x):
    if x in ([0, '0', '', None, '0.0', '0.00', 'None'] + [' ' * i for i in range(1, 10)]):
        x = ''
    else:
        x = str(x)[:10]
    return x


def f_float(x):
    if x in ([0, '0', '', None] + [' '*i for i in range(1, 10)]):
        x = 0
    return x


def f_float_1(x):
    if x in ([0, '0', '', None] + [' '*i for i in range(1, 10)]):
        x = 1
    return x


def f_returnFloat(x):
    if x in ([0, '0', '', None] + [' '*i for i in range(1, 10)]):
        x = 0
    else:
        x = float(x)
    return x


def f_date(x):
    if x in ([0, '0', '', None, 'ne'] + [' '*i for i in range(1, 10)]):
        x = None
    return x


def isFloat(x):
    """
    仅仅判断是否是float, 这个函数有问题，不建议使用
    :param x:
    :return:
    """
    x = str(x)
    result = 0
    xList = x.split('.')
    if len(xList) > 2:
        result = '错误数据'
    else:
        for i in xList:
            if not i.isdigit():
                result = '错误数据'
    return result


def f_floatStr(x):
    strList1 = ['None', '--', 'ne', None]
    strList2 = [' '*i for i in range(10)]
    strList = strList1 + strList2
    if x in strList:
        x = 0
    elif isFloat(x) == '错误数据':
        x = '错误数据'
    else:
        x = float(x)
    return x


def f_dateStr(x):
    xList = str(x).strip().split('-')
    if len(xList) == 3:
        if (len(str(xList[1])) > 2
                or len(str(xList[2])) > 2
                or not str(xList[1]).isdigit()
                or not str(xList[2]).isdigit()
                or not str(xList[0]).isdigit()
                or len(str(xList[0])) > 4):
            result = '错误数据'
        else:
            if int(xList[1]) > 12 or int(xList[2]) > 31:
                result = '错误数据'
            else:
                if len(str(xList[0])) == 2:
                    xList[0] = '20' + str(xList[0])
                if len(str(xList[1])) == 1:
                    xList[1] = '0' + str(xList[1])
                if len(str(xList[2])) == 1:
                    xList[2] = '0' + str(xList[2])
                result = datetime.datetime.fromisoformat('-'.join(xList))
    else:
        result = '错误数据'
    return result


def f_QtStr2Int(x):
    """
    如果数据无效, 返回 0
    :param x: 输入的值必须为整数型
    :return: int
    """
    x1 = str(x)
    if x1.startswith('-'):
        x1 = str(x)[1:]
    if not str(x1).isdigit():
        return 0
    else:
        return int(x)


def f_Qt2FloatStr(x, afterDecimalPoint=2):
    """
    常用函数, 单个取值写入, 规定小数点
    :param x: 数值 或 str
    :param afterDecimalPoint: 小数点后几位, None 代表不限制, 0 代表int
    :return: 小数点后几位的值的 str
    """
    x = str(x)
    xList = x.split('.')
    if len(xList) > 2:
        return ''
    else:
        for i in xList:
            if xList.index(i) == 0 and str(i).startswith('-'):
                i = i[1:]
            if not i.isdigit():
                result = ''
                return result
        result = float(x)
        if result == 0:
            return ''
        elif afterDecimalPoint is None:
            return str(result)
        elif int(afterDecimalPoint) == 0:
            return str(round(result))
        else:
            return str(round(result, afterDecimalPoint))


def f_Qt2DateStr(x):
    """
    符合规定数据返回 datetime 的字符格式, 自己取段 2022-01-31 00:01:02 共19个字符, 正常取[:10], [2:10], [2:19], [:19]等
    :param x: [datetime.date, datetime.datetime, str]
    :return: str
    """
    if type(x) in [datetime.datetime, datetime.date]:
        return str(x)
    else:
        xList = str(x).strip().split('-')
        if len(xList) == 3:
            if (len(str(xList[1])) > 2
                    or len(str(xList[2])) > 2
                    or not str(xList[1]).isdigit()
                    or not str(xList[2]).isdigit()
                    or not str(xList[0]).isdigit()
                    or len(str(xList[0])) > 4):
                result = ''
            else:
                if int(xList[1]) > 12 or int(xList[2]) > 31:
                    result = ''
                else:
                    if len(str(xList[0])) == 2:
                        xList[0] = '20' + str(xList[0])
                    if len(str(xList[1])) == 1:
                        xList[1] = '0' + str(xList[1])
                    if len(str(xList[2])) == 1:
                        xList[2] = '0' + str(xList[2])
                    result = datetime.datetime.fromisoformat('-'.join(xList))
        else:
            result = ''
        return str(result)


def f_QtStr2Folat(x):
    """
    返回能被float的值, 不能被float的值为 0
    :param x:
    :return:
    """
    x = str(x)
    xList = x.split('.')
    if len(xList) > 2:
        result = 0
    else:
        for i in xList:
            if xList.index(i) == 0 and str(i).startswith('-'):
                i = i[1:]
            if not i.isdigit():
                result = 0
                return result
        result = float(x)
    return result


def f_QtSumList2Float(list_str):
    """
    返回一组数值的总值, 返回值为 float
    :param list_str:
    :return: float
    """
    listFloat = [f_QtStr2Folat(i) for i in list_str]
    return sum(listFloat)


def f_QtSumList2Str(list_str, afterDecimalPoint=None):
    """
    返回一组值的求和值， 返回为 str
    :param list_str:
    :param afterDecimalPoint: 代表长度
    :return:
    """
    listFloat = [f_QtStr2Folat(i) for i in list_str]
    if sum(listFloat) == 0:
        return ''
    else:
        if afterDecimalPoint is None:
            return str(sum(listFloat))
        elif afterDecimalPoint == 0:
            return str(round((sum(listFloat))))
        else:
            return str(round(sum(listFloat), int(afterDecimalPoint)))


def f_Qt2Date(date):
    if type(date) in [datetime.datetime, datetime.date]:
        result = date
    else:
        xList = str(date).strip().split('-')
        if len(xList) == 3:
            if str(xList[2]).isdigit():
                if (len(str(xList[1])) > 2
                        or len(str(xList[2])) > 2
                        or not str(xList[1]).isdigit()
                        or not str(xList[0]).isdigit()
                        or len(str(xList[0])) > 4):
                    result = None
                else:
                    if int(xList[1]) > 12 or int(xList[2]) > 31:
                        result = None
                    else:
                        if len(str(xList[0])) == 2:
                            xList[0] = '20' + str(xList[0])
                        if len(str(xList[1])) == 1:
                            xList[1] = '0' + str(xList[1])
                        if len(str(xList[2])) == 1:
                            xList[2] = '0' + str(xList[2])
                        result = datetime.datetime.fromisoformat('-'.join(xList))
            else:
                if str(xList[2]).count(' ') != 1:
                    result = None
                else:
                    day = str(xList[2]).split(' ')[0]
                    time = str(xList[2]).split(' ')[1]
                    if str(day).isdigit():
                        if (len(str(day)) > 2
                                or len(str(xList[1])) > 2
                                or not str(xList[1]).isdigit()
                                or not str(xList[0]).isdigit()
                                or len(str(xList[0])) > 4):
                            result = None
                        else:
                            if int(xList[1]) > 12 or int(day) > 31:
                                result = None
                            else:
                                if len(str(xList[0])) == 2:
                                    xList[0] = '20' + str(xList[0])
                                if len(str(xList[1])) == 1:
                                    xList[1] = '0' + str(xList[1])
                                if len(str(day)) == 1:
                                    xList[2] = '0' + str(day) + ' ' + str(time)
                                else:
                                    xList[2] = str(day) + ' ' + str(time)
                                result = datetime.datetime.fromisoformat('-'.join(xList))
                    else:
                        result = None
        else:
            result = None
    return result




if __name__ == '__main__':
    a = datetime.datetime.today()
    a1 = f_Qt2DateStr(a)
    print(a1, type(a1))

    a = None
    a1 = f_Qt2Date(a)
    print('a1:', a1, type(a1))

    a = '21-03-24 09:12:12'
    a2 = f_Qt2Date(a)
    print('a2:', a2, type(a2))

    a = '21-02-28'
    a3 = f_Qt2Date(a)
    print('a3:', a3, type(a3))

    a = str(datetime.datetime.today())
    a4 = f_Qt2Date(a)
    print('a4:', a4, type(a4))





