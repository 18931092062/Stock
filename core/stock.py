# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:10
# @Author  : wangkai
# @Email   : 18931092062@163.com
# @File    : text.py
# @Software: PyCharm
""""""
import datetime
from core.emailer import send_emails
from core.stock_api import *
from core.web_api import *
import time


def run_stock():
    """运行"""
    if is_opening():
        start = datetime.time(9, 30, 0, 0)  # 开盘时间
        end = datetime.time(19, 1, 0, 0)  # 关盘时间
        unique_code, waring_list = get_warning_data()  # 获取预警数据
        print("唯一代码：", unique_code)
        print("预警列表：", waring_list)
        while True:
            if start < datetime.datetime.now().time() < end:  # 判断时间
                price_list = sto.get_realtime_price(unique_code)  # 获取实时票数据
                print(price_list)
                monitoring_warning(price_list, waring_list)  # 检测
                time.sleep(5)
            else:
                break
    return


def monitoring_warning(price_list, result):
    """监控预警"""
    for one_res in result:
        code = one_res["stock_code"]  # 代码
        dire = one_res["direction"]  # 方向
        warning_price = one_res["warning_price"]  # 价格
        if dire == "高于":
            if float(price_list[code][0]) > warning_price:
                trigger(0, one_res, price_list[code])
        elif dire == "低于":
            if float(price_list[code][1]) < warning_price:
                trigger(1, one_res, price_list[code])


def trigger(tri_type, reach_row, price_list):
    """触发预警,0高于，1低于"""
    n_id = reach_row["id"]
    fans_id = reach_row["fans_id"]
    email = get_request("http://localhost/weixin/stock_list", {"type": "email", "user": fans_id})  # 获取email
    print(email)
    title = "%s(%s)价格预警" % (reach_row["stock_code"], price_list[2])
    #更新数据库状态
    #recipients = models.Fans.objects.values("email").filter(id=fans_id).first()  # 收件人
    if tri_type == "1":
        content = "%s(%s)价格上涨到%s元，提醒你及时关注" % (
            reach_row["stock_code"], price_list[2], reach_row["warning_price"])
    else:
        content = "%s(%s)价格下跌到%s元，提醒你及时关注" % (
            reach_row["stock_code"], price_list[2], reach_row["warning_price"])
    send_emails(title, content, email)


def get_warning_data():
    """获取预警数据"""
    # 查询数据
    result = get_request("http://localhost/weixin/stock_list", {"type": "stock"})  # 获取预警数据
    print(result)
    return result["unique_code"], result["waring_list"]


def is_opening():
    """是否是开盘日"""
    today = datetime.datetime(2021, 5, 10)
    print(today.date(), today.isocalendar(), today.time())
    week = today.isocalendar()[2]  # 周一为1…周日为7
    if week > 6:  # 是否为周末
        return False
    day_off_list = get_request("http://localhost/weixin/day_off")  # 节假日
    if today.date().strftime('%Y-%m-%d') in day_off_list:  # 是否是节假日
        return False
    return True
