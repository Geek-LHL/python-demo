import json
import ujson

import requests
import arrow

from app import baseDao
from app import logger

# json转换工具：https://www.json.cn/

__SELECT_SQL = """
    SELECT * FROM sys_user where id < 100
    """


def query_data():
    # 查询多条数据
    datas = baseDao.query_sql(__SELECT_SQL)
    logger.info(ujson.dumps(datas))

    return ""
