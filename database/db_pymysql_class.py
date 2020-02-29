# -*- coding: utf-8 -*-

"""
通过PyMysql访问数据库的全局封装

Author: ainoob.cn
Email: 535334234@qq.com
"""

import pymysql
from db_config import DB_CONFIG

class DB():
    """
    把全局的数据库访问封装成公共的DB类。
    """

    _connect = None
    _cursor = None

    def __init__(self):
        self._connect = pymysql.connect(DB_CONFIG['MYSQL']['HOST'],
                                        DB_CONFIG['MYSQL']['USERNAME'],
                                        DB_CONFIG['MYSQL']['PASSWORD'],
                                        DB_CONFIG['MYSQL']['DATABASE'])
        self._cursor = self._connect.cursor()

    @property
    def connect(self):
        return self._connect

    @property
    def session(self):
        return self._cursor

    # 数据库查询，返回数据元组
    def query(self, sql):
        try:
            # 执行SQL语句
            self._cursor.execute(sql)
            # 获取所有记录列表
            results = self._cursor.fetchall()
            return results
        except:
            # 发生错误，返回空元组
            return ()

    # 数据库更新，返回成功与否的
    def execute(self, sql):
        try:
            # 执行SQL语句
            self._cursor.execute(sql)
            # 提交到数据库执行
            self._connect.commit()
            return True
        except:
            # 发生错误时回滚
            self._connect.rollback()
            return False

# 定义全局数据库访问实例
MYSQL_DB = DB()

if __name__ == "__main__":
    # 使用全局数据库访问实例，或新建数据库访问
    db = MYSQL_DB

    # 数据查询
    print('\n--数据查询--')
    sql = 'select * from ai_spider_urls limit 5;'
    rs = db.query(sql)
    print(type(rs))
    print(rs)