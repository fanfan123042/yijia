import add_path_for_bat
import datetime
from baseClass225.CustomInfo import CustomOrder
from func.f_change import f_date, f_float
from func.get_data import get_column_data


def unionCustomData(customName):
    """
    输入客户名, 查找对应的客户, 给出组合数据
    :param customName: 客户名, 此为内部函数
    :return: 1 rate -频率, 数据多，最多容纳 105个数字, 做调整
             2 numMax - 范围内的最大下单数
             3 amountMax - 范围内的最大金额值
             4 data_need - 组合数据, 分别为 （货期距今天数, 下单数量范围内合并, 下单金额范围内合并）
    """
    dictCustom = {'21年中球': ['21年中球', '中球'],
                  '中球': ['21年中球', '中球'],
                  'CAMILLA AND MARC': ['CAMILLA AND MARC', '丽丝'],
                  '丽丝': ['CAMILLA AND MARC', '丽丝'],
                  'PF': ['PF', 'PF2104'],
                  'PF2104': ['PF', 'PF2104'],
                  'Sandwich': ['SANDWICH-1', 'Sandwich'],
                  'SANDWICH-1': ['Sandwich', 'SANDWICH-1'],
                  'WJJ': ['WJJ', 'WJJ2103', 'WJJ2106', 'WJJ2107'],
                  'WJJ2103': ['WJJ2106', 'WJJ2107', 'WJJ', 'WJJ2103'],
                  'WJJ2106': ['WJJ2107', 'WJJ', 'WJJ2103', 'WJJ2106'],
                  'WJJ2107': ['WJJ', 'WJJ2103', 'WJJ2106', 'WJJ2107'],
                  '十二篮': ['十二篮线下', '小音儿', '影儿-诗篇', '诗篇', '音儿', '十二篮'],
                  '十二篮线下': ['小音儿', '影儿-诗篇', '诗篇', '音儿', '十二篮', '十二篮线下'],
                  '小音儿': ['影儿-诗篇', '诗篇', '音儿', '十二篮', '十二篮线下', '小音儿'],
                  '影儿-诗篇': ['诗篇', '音儿', '十二篮', '十二篮线下', '小音儿', '影儿-诗篇'],
                  '诗篇': ['音儿', '十二篮', '十二篮线下', '小音儿', '影儿-诗篇', '诗篇'],
                  '音儿': ['十二篮', '十二篮线下', '小音儿', '影儿-诗篇', '诗篇', '音儿'],
                  '富鈿': ['富钿', '富鈿'],
                  '富钿': ['富鈿', '富钿'],
                  '江南2022春夏': ['江南2022春夏男装', '江南21春女装', '江南21春男装', '江南21秋冬男装',
                               '江南女装', '江南男装', '蓬马', '江南2022春夏'],
                  '江南2022春夏男装': ['江南21春女装', '江南21春男装', '江南21秋冬男装', '江南女装',
                                 '江南男装', '蓬马', '江南2022春夏', '江南2022春夏男装'],
                  '江南21春女装': ['江南21春男装', '江南21秋冬男装', '江南女装', '江南男装', '蓬马',
                              '江南2022春夏', '江南2022春夏男装', '江南21春女装'],
                  '江南21春男装': ['江南21秋冬男装', '江南女装', '江南男装', '蓬马', '江南2022春夏',
                              '江南2022春夏男装', '江南21春女装', '江南21春男装'],
                  '江南21秋冬男装': ['江南女装', '江南男装', '蓬马', '江南2022春夏', '江南2022春夏男装',
                               '江南21春女装', '江南21春男装', '江南21秋冬男装'],
                  '江南女装': ['江南男装', '蓬马', '江南2022春夏', '江南2022春夏男装', '江南21春女装',
                           '江南21春男装', '江南21秋冬男装', '江南女装'],
                  '江南男装': ['蓬马', '江南2022春夏', '江南2022春夏男装', '江南21春女装', '江南21春男装',
                           '江南21秋冬男装', '江南女装', '江南男装'],
                  '蓬马': ['江南2022春夏', '江南2022春夏男装', '江南21春女装', '江南21春男装', '江南21秋冬男装',
                         '江南女装', '江南男装', '蓬马'],
                  '碧臣MM': ['碧臣SS', '碧臣VERDE', '碧臣MM'],
                  '碧臣SS': ['碧臣VERDE', '碧臣MM', '碧臣SS'],
                  '碧臣VERDE': ['碧臣MM', '碧臣SS', '碧臣VERDE']}
    info = dictCustom.get(customName)
    if info is None:
        customList = [customName, ]
    else:
        customList = info
    print(customList)

    data = []
    for i in customList:
        c = CustomOrder(i, 20000)
        if c.orderDataToNow:
            data = data + c.orderDataToNow
    # print(len(data), data)
    data_fixed = [[datetime.datetime.today().toordinal() - i[0].toordinal(), i[2], i[3]]
                  for i in data if f_date(i[0]) is not None]
    data_fixed.sort(reverse=True)

    rate = int((data_fixed[0][0] - data_fixed[-1][0])/105) + 1

    data_need = []
    # print('data_fixed[0][0], data_fixed[-1][0]:', data_fixed[0][0], data_fixed[-1][0])
    # print('datetime.datetime.today().toordinal():', datetime.datetime.today().toordinal())
    for i in range(data_fixed[0][0], data_fixed[-1][0] - rate, -rate):
        numOrder = 0
        amount = 0
        for j in range(len(data_fixed)):
            if rate > (i - data_fixed[j][0]) >= 0:
                numOrder = numOrder + f_float(data_fixed[j][1])
                amount = amount + f_float(data_fixed[j][2])
        data_need.append([i, numOrder, amount])
    numMax = max([i[1] for i in data_need])
    amountMax = max([i[2] for i in data_need])
    # data_need.sort(reverse=True)

    # print('rate, data_fixed:', rate, len(data_fixed), data_fixed)
    # print('rate, data_need, numMax, amountMax:', rate, numMax, amountMax, len(data_need), data_need, )
    return rate, numMax, amountMax, data_need


def allDataForPicture():

    customList = get_column_data(t_table='custom_info', t_field='name_custom')

    data = []
    for i in customList:
        c = CustomOrder(i, 20000)
        if c.orderDataToNow:
            data = data + c.orderDataToNow
    data_fixed = [[datetime.datetime.today().toordinal() - i[0].toordinal(), i[2], i[3]]
                  for i in data if f_date(i[0]) is not None]
    data_fixed.sort(reverse=True)

    rate = int((data_fixed[0][0] - data_fixed[-1][0]) / 105) + 1

    data_need = []
    for i in range(data_fixed[0][0], data_fixed[-1][0] - rate, -rate):
        numOrder = 0
        amount = 0
        for j in range(len(data_fixed)):
            if rate > (i - data_fixed[j][0]) >= 0:
                numOrder = numOrder + f_float(data_fixed[j][1])
                amount = amount + f_float(data_fixed[j][2])
        data_need.append([i, numOrder, amount])
    numMax = max([i[1] for i in data_need])
    amountMax = max([i[2] for i in data_need])

    return rate, numMax, amountMax, data_need


if __name__ == '__main__':
    unionCustomData('WJJ')
    # unionCustomData('蓬马')
