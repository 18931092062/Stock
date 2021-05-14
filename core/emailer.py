# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 16:09
# @Author  : wangkai
# @Email   : 18931092062@163.com
# @File    : email_helper.py
# @Software: PyCharm

import email.mime.multipart
import email.mime.text
import smtplib


def send_emails(title, main_text, recipients):
    """
    发邮件
    :param title: 标题
    :param main_text: 内容
    :param recipients: 收件人
    :return:
    """
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = title  # 题目
    msg['From'] = '18931092062@163.com'  # 发件人
    msg['To'] = recipients  # 收件人
    txt = email.mime.text.MIMEText(main_text)  # 内容
    msg.attach(txt)
    smtp = smtplib.SMTP_SSL('smtp.163.com', '465')
    smtp.login('18931092062@163.com', 'a12345678')
    smtp.sendmail('18931092062@163.com', recipients, msg.as_string())
    smtp.quit()
    return '邮件发送成功email has send out !'
