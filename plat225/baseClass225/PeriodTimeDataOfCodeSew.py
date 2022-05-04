import add_path_for_bat
import datetime
from func.getConn import getConn
from baseClass225.SewInfo import Sew
from func.f_change import f_float, f_returnFloat


class DataCodeSew:
    """
    一段时间内工厂的各个数据, 包括很多平均数据
    """
    def __init__(self, code_sew, start=30, end=0):

        self.code_sew = str(code_sew).strip()
        if type(start) in [int, ]:
            self.checkStartDay = datetime.datetime.fromordinal(datetime.datetime.today().toordinal() - start)
        elif type(start) in [datetime.datetime, datetime.date]:
            self.checkStartDay = start
        else:
            self.checkStartDay = datetime.datetime.fromisoformat(str(start).strip())

        if type(end) in [int, ]:
            self.checkEndDay = datetime.datetime.fromordinal(datetime.datetime.today().toordinal() - end + 1)
        elif type(end) in [datetime.datetime, datetime.date]:
            self.checkStartDay = end
        else:
            self.checkStartDay = datetime.datetime.fromisoformat(str(end).strip())

        sql = 'select ' \
              'remark ' \
              'from sew_info ' \
              'where code_sew = "{}" and date_contract_sign > "{}" and date_contract_sign < "{}";'\
            .format(self.code_sew, self.checkStartDay, self.checkEndDay)
        dataRemark = getConn().queryAll(sql)
        if len(dataRemark) == 0:
            self.remarkList = []
        else:
            self.remarkList = [i[0] for i in dataRemark]

        self.num_sew_total = 0
        numSew_withNum = 0

        miniPrice_x_numSew = 0
        numSew_withMiniPrice = 0
        numMiniPrice = 0

        ratio_x_numSew = 0
        numSew_withRatio = 0
        numRatio = 0

        weightingRSP_x_numSew = 0
        numSew_withWRSP = 0
        numWRSP = 0

        sewPrice_x_numSew = 0
        numSew_withSewPrice = 0
        numSewPrice = 0

        self.sewDegreeA = self.sewDegreeB = self.sewDegreeC = self.sewDegreeD = self.sewDegreeE = self.sewDegreeNone = 0

        for i in self.remarkList:

            factory = Sew(i, self.code_sew)
            if f_float(factory.num_sew) != 0:
                self.num_sew_total += f_float(factory.num_sew)
                numSew_withNum += 1
                if f_float(factory.mini_price) != 0:
                    miniPrice_x_numSew += f_returnFloat(factory.mini_price) * f_float(factory.num_sew)
                    numSew_withMiniPrice += 1
                    numMiniPrice += f_float(factory.num_sew)
                if f_float(factory.ratio_sew_price) != 0:
                    ratio_x_numSew += f_returnFloat(factory.ratio_sew_price) * f_float(factory.num_sew)
                    numSew_withRatio += 1
                    numRatio += f_float(factory.num_sew)
                if f_float(factory.weighting_ratio_s_p) != 0:
                    weightingRSP_x_numSew += f_returnFloat(factory.weighting_ratio_s_p) * f_float(factory.num_sew)
                    numSew_withWRSP += 1
                    numWRSP += f_float(factory.num_sew)
                if f_float(factory.sew_price) != 0:
                    sewPrice_x_numSew += f_returnFloat(factory.sew_price) * f_float(factory.num_sew)
                    numSew_withSewPrice += 1
                    numSewPrice += f_float(factory.num_sew)

            if factory.sew_degree == '优秀':
                self.sewDegreeA += 1
            elif factory.sew_degree == '良好':
                self.sewDegreeB += 1
            elif factory.sew_degree == '合格':
                self.sewDegreeC += 1
            elif factory.sew_degree == '不合格':
                self.sewDegreeD += 1
            elif factory.sew_degree == '负面':
                self.sewDegreeE += 1
            else:
                self.sewDegreeNone += 1

        if numSew_withMiniPrice == 0:
            self.avgMiniPrice = None
        else:
            self.avgMiniPrice = miniPrice_x_numSew / numMiniPrice

        if numSew_withSewPrice == 0:
            self.avgSewPrice = None
        else:
            self.avgSewPrice = sewPrice_x_numSew / numSewPrice

        if numSew_withRatio == 0:
            self.avgSewRate = None
        else:
            self.avgSewRate = ratio_x_numSew / numRatio

        if numSew_withWRSP == 0:
            self.avgSewRate_weighting = None
        else:
            self.avgSewRate_weighting = weightingRSP_x_numSew / numWRSP

        if numSew_withNum == 0:
            self.avgNumSew = None
        else:
            self.avgNumSew = self.num_sew_total / numSew_withNum


if __name__ == '__main__':
    import time
    time1 = time.time()
    a = DataCodeSew('李小勇', 100)
    print(a.code_sew, '总数', a.num_sew_total, '平均件数：', a.avgNumSew, '平均单价：', a.avgSewPrice,
          '平均小工价:', a.avgMiniPrice,
          '平均加权倍率:', a.avgSewRate_weighting, '平均倍率：', a.avgSewRate,
          '款式列表:', len(a.remarkList), a.remarkList)
    a = DataCodeSew('王建组', 100)
    print(a.code_sew, '总数', a.num_sew_total, '平均件数：', a.avgNumSew, '平均单价：', a.avgSewPrice,
          '平均小工价:', a.avgMiniPrice,
          '平均加权倍率:', a.avgSewRate_weighting, '平均倍率：', a.avgSewRate,
          '款式列表:', len(a.remarkList), a.remarkList)
    print(len(a.remarkList), a.sewDegreeA, a.sewDegreeB, a.sewDegreeC, a.sewDegreeD, a.sewDegreeE, a.sewDegreeNone)
    time2 = time.time()
    print('\n用时 {} 秒'.format(round(time2-time1, 2)))


