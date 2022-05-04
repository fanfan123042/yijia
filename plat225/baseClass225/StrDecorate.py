import datetime


class StrDe:
    def __init__(self, arg):
        self.arg = arg
        time = datetime.datetime.now()
        str1 = '您于 {} 输入 {} ,  现匹配内容如下:\n'.format(str(time)[10:], self.arg)
        str2 = '-' * 100
        self.text = str1 + str2


if __name__ == '__main__':
    a = StrDe('18')
    print(a.arg)

