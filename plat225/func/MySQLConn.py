import pymysql


class MysqlConn:
    """
    MySQLConnection
    alan 220325
    """
    def __init__(self, host=None, user=None, password=None, database=None, port=3306):

        [self.host, self.user,
         self.password, self.database, self.port] = [host, user, password, database, port]
        self.conn = self.conn
        self.db = self.get_db()

    def get_db(self):
        db = pymysql.connect(host=self.host, user=self.user, password=self.password,
                             database=self.database, port=self.port)
        return db

    def conn(self):
        cursor = self.db.cursor()
        return cursor

    def close(self):
        self.db.close()

    def queryAllArgs(self, query_sql, dataList):
        """
        根据查询语句查询所有数据
        :param query_sql:
        :param dataList:
        :return:
        """
        try:
            cursor = self.conn()
            cursor.execute(query_sql, dataList)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as ex:
            print("query all Error:{}".format(ex))
            print(query_sql)
        finally:
            self.close()

    def query1Args(self, query_sql, dataTuple):
        """
        根据查询语言查询一条语句
        :param query_sql: 查询语句
        :param dataTuple: ”“”写入，后面加元组
        :return:
        """
        try:
            cursor = self.conn()
            cursor.execute(query_sql, dataTuple)
            results = cursor.fetchone()
            cursor.close()
            return results
        except Exception as ex:
            print("query one Error:{}".format(ex))
            print(query_sql)

    def query1(self, query_sql):
        """
        根据查询语言查询一条语句
        :param query_sql: 查询语句
        :return:
        """
        try:
            cursor = self.conn()
            cursor.execute(query_sql)
            results = cursor.fetchone()
            cursor.close()
            return results
        except Exception as ex:
            print("query one Error:{}".format(ex))
            print(query_sql)
        finally:
            self.close()

    def queryAll(self, query_sql):
        """
        根据查询语句查询所有数据
        :param query_sql:
        :return:
        """
        try:
            cursor = self.conn()
            cursor.execute(query_sql)
            results = cursor.fetchall()
            # cursor.close()
            return results
        except Exception as ex:
            print("query all Error:{}".format(ex))
            print(query_sql)
        finally:
            self.close()

    def update1Args(self, update_sql, tuple_2):
        """
        根据更新语句更新数据
        :param update_sql: “”“写入，后面%s
        :param tuple_2:  输入输出均为 元组
        :return:
        """
        try:
            cursor = self.conn()
            cursor.execute(update_sql, tuple_2)
            self.db.commit()
            cursor.close()
        except Exception as ex:
            print("update Error:{}".format(ex))
            self.db.rollback()
            print('sql语句：', update_sql)
        finally:
            self.close()

    def updateManyArgs(self, update_sql, tuple_2):
        """
        根据更新语句更新数据
        :param update_sql: “”“写入，后面%s
        :param tuple_2:  输入输出均为 元组
        :return:
        """
        try:
            cursor = self.conn()
            cursor.executemany(update_sql, tuple_2)
            self.db.commit()
            cursor.close()
        except Exception as ex:
            print("update Error:{}".format(ex))
            self.db.rollback()
        finally:
            self.close()

    def update1(self, update_sql):
        """
        根据更新语句更新数据
        :param update_sql:
        :return:
        """
        try:
            cursor = self.conn()
            cursor.execute(update_sql)
            self.db.commit()
            cursor.close()
        except Exception as ex:
            print("update Error:{}".format(ex))
            self.db.rollback()
            print(update_sql)
        finally:
            self.close()

    def updateMany(self, update_sql, tuple_2):
        """
        根据更新语句更新数据
        :param update_sql: “”“写入，后面%s
        :param tuple_2:  输入输出均为 元组
        :return:
        """
        try:
            cursor = self.conn()
            cursor.executemany(update_sql, tuple_2)
            self.db.commit()
        except Exception as ex:
            print("update Error:{}".format(ex))
            self.db.rollback()
        finally:
            self.close()
