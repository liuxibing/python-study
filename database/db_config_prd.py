# -*- coding: utf-8 -*-

"""
数据库配置文件

Author: ainoob.cn
Email: 535334234@qq.com
"""

# 全局数据连接配置
DB_CONFIG = {
    # 本地数据库配置
    # 'DB_CONNECT_STRING': 'mysql+pymysql://root:@localhost/ainoob?charset=utf8'

    # 生产数据库配置
    'DB_CONNECT_STRING': 'mysql+pymysql://pma:pw765c64pma@106.14.127.237/ainoob?charset=utf8',
    'MYSQL':{
        'HOST':'106.14.127.237',
        'USERNAME':'pma',
        'PASSWORD':'pw765c64pma',
        'DATABASE':'ainoob',
        'CHARSET':'utf8'
    }
}