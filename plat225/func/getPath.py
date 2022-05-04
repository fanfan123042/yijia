import os


def getPath(strFunc):
    """
    用于从init.txt文件里读取外部文件存储地址
    alan 21-11-11, 21-11-15
    :param strFunc: 文件名或地址 对应的作用名，需要起始位置 加 '【】'
    :return: 返回路径名 or文件名 or 值， 为 str
    """

    path_cur = os.getcwd()
    path_upper = '\\'.join(path_cur.split('\\')[:-1])
    path_need = path_upper + '\\conf\\init.txt'
    with open(path_need, 'r', encoding='utf-8') as file:
        while True:
            content = file.readline()
            title = str(content).split('=')[0].strip()
            if title == str(strFunc).strip():
                you_need = str(content).split('=')[1].strip('\n').strip()
                return you_need
