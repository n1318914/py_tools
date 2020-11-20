# -*- coding:utf-8 -*-
import mysql.connector


class MySQLConnect(object):
    """ mysqldb 操作类"""

    def __init__(self, **params):
        """ 数据库初始化 """
        self.conn = mysql.connector.connect(**params)
        self.cursor = self.conn.cursor()  # 使用cursor方法获取操作游标

    def close(self):
        """ 关闭数据库 """
        self.cursor.close()
        self.conn.close()

    def select(self, cmd):
        """ 用于查询返回所有结果 """
        results = []
        try:
            self.cursor.execute(cmd)
            results = self.cursor.fetchall()
        except Exception as e:
            print("mysql selct error: %s" % e)
        return results

    def select_one(self, cmd):
        """ 查询一条结果 """
        try:
            self.cursor.execute(cmd)
            result = self.cursor.fetchone()
        except Exception as e:
            print("mysql select one error: %s" % e)
        return result

    def inner_execute(self, cmd):
        """ 进行修改，插入，更新基本操作 """
        try:
            self.cursor.execute(cmd)
            self.commit()
        except Exception as e:
            print("mysql insert error: %s" % e)

    def insert(self, cmd):
        """ 执行插入mysql 操作 """
        self.inner_execute(cmd)

    def update(self, cmd):
        """ 执行更新mysql操作 """
        self.inner_execute(cmd)

    def delete(self, cmd):
        """ 执行删除mysql操作 """
        self.inner_execute(cmd)

    def commit(self):
        """ 事务提交操作 """
        self.conn.commit()

    def rollback(self):
        """ 事务回滚操作 """
        self.conn.rollback()


def test():
    """ 测试case """
    pass

if __name__ == '__main__':
    test()
