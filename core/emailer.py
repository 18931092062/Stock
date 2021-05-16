# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 16:09
# @Author  : wangkai
# @Email   : 18931092062@163.com
# @File    : email_helper.py
# @Software: PyCharm

from email.mime.text import MIMEText
import smtplib
from email.header import Header


def send_emails(title, main_text, recipients):
    """
    发邮件
    :param title: 标题
    :param main_text: 内容
    :param recipients: 收件人
    :return:
    """
    msg = MIMEText(main_text, 'plain', 'utf-8')  # 设置内容
    msg['Subject'] = Header(title, 'utf-8')  # 题目
    msg['From'] = '18931092062@163.com'  # 发件人
    msg['To'] = recipients  # 收件人
    smtp = smtplib.SMTP("smtp.163.com", 25)  # SMTP协议默认端口是25
    smtp.login('18931092062@163.com', 'LAVIVEJMBXXXANTN')  # 登录
    smtp.sendmail('18931092062@163.com', recipients, msg.as_string())  # 发邮件
    smtp.quit()  # 退出
    return '邮件发送成功email has send out !'
