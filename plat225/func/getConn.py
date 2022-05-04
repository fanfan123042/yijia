from func.MySQLConn import MysqlConn
from func.getPath import getPath


def getConn(database=225):
    passStr = ''
    if int(database) == 219:
        passStr = getPath('【Plat219】')
    elif int(database) == 225:
        passStr = getPath('【Plat225】')

    data = passStr.split(',')

    host = data[0].strip()
    user = data[1].strip()
    password = data[2].strip()
    database = data[3].strip()
    port = int(data[4])

    conn = MysqlConn(host, user, password, database, port)
    return conn
