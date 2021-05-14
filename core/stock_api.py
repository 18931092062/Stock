# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 15:57
# @Author  : wangkai
# @Email   : 18931092062@163.com
# @File    : stock_api.py
# @Software: PyCharm
"""
接口页面：
https://waditu.com/document/2
http://tushare.org/
"""

import tushare as ts


class Stock:
    def __init__(self):
        self._pro = ts.pro_api('aa5e2aa0bdc49fa1bd215823252f681cb571bcf5041e3d3e8f464041')

    def get_realtime_price(self, stock_list):
        """
        获取实时价格
        :param stock_list: 票列表
        :return: [今天最高,今天最低,票名称，当前价格]
        """
        if isinstance(stock_list, list):
            df = ts.get_realtime_quotes(stock_list)
            filter_list = df[["high", "low", "name", "price"]]
            res = {i: j for i, j in zip(stock_list, filter_list.values.tolist())}
            return res
        else:
            raise TypeError("类型错误,必须是list")

    def get_realtime_index(self):
        """获取实时指标"""
        df = ts.get_index()
        print(df)

    def get_all_stock(self):
        """获取所有的票代码"""
        df = self._pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        print(df)


sto = Stock()
