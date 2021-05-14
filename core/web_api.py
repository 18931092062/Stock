# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 16:12
# @Author  : wangkai
# @Email   : 18931092062@163.com
# @File    : request_interface.py
# @Software: PyCharm
"""请求接口数据"""
import requests


def get_request(url, data={}):
    """get请求接口"""
    response = requests.get(url=url, params=data, timeout=30)
    json_data = response.json()
    if json_data["status"] == "200":
        data = json_data["data"]
    return data


def post_request(url, data):
    """post请求接口"""
    response = requests.post(url=url, data=data, timeout=30)
    json_data = response.json()
    return json_data
