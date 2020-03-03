# -*- coding: utf-8 -*-

"""
通过SQLAlchemy访问数据库的全局封装
参考资料：http://www.ainoob.cn/bigdata/sqlalchemy/sqlalchemy-operations.html

Author: ainoob.cn
Email: 535334234@qq.com
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_config import DB_CONFIG

class DB():
    """
    把全局的数据库访问封装成公共的DB类。
    """

    _connect = None
    _session = None

    def __init__(self):
        if 'sqlite' in DB_CONFIG['DB_CONNECT_STRING']:
            connect_args = {'check_same_thread': False}
            self._connect = create_engine(DB_CONFIG['DB_CONNECT_STRING'], echo=False, connect_args=connect_args)
        else:
            self._connect = create_engine(DB_CONFIG['DB_CONNECT_STRING'], echo=False)
        DB_Session = sessionmaker(bind=self._connect)
        self._session = DB_Session()

    @property
    def connect(self):
        return self._connect

    @property
    def session(self):
        return self._session

    # 执行原生SQL，返回数据结构对象。
    def execute(self, sql):
        return self._session.execute(sql)

# 定义全局数据库访问实例
MYSQL_DB = DB()

if __name__ == "__main__":
    # 使用全局数据库访问实例，或新建数据库访问
    db = MYSQL_DB
    

    # 数据更新
    print('\n--数据更新--')
    sql = 'update ai_spider_urls set stype="blog" where id=1;'
    rs = db.execute(sql)    # 返回查询的第一条数据，row对象
    print(type(rs)) 
    print(rs)
    
    # 数据查询
    print('\n--数据查询--')
    sql = 'select * from ai_spider_urls limit 5;'
    rs_row = db.execute(sql).first()    # 返回查询的第一条数据，row对象
    print(type(rs_row)) 
    print(rs_row)
    print(rs_row[0],rs_row['url'],rs_row.title)

    # rs = db.execute(sql)    # 返回结果对象集，可用for ... in ...遍历访问。
    # print(type(rs)) 
    # for row in rs:  # row为元组，可用下标索引或列名访问
    #     print(type(row))
    #     print(row)
    #     print(row[0],row['url'])

    

    