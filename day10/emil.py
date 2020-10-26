#!/usr/bin/python3
#-*- coding: utf-8 -*-
from email.mime.text import MIMEText
import smtplib
msg = MIMEText('hello,send by Python...','plain','utf-8')
## 输入Email地址和口令
from_addr = input('From:')
#password = input('Password:')
mail_pass = 'DWNADOMHWMIZKKO'
## 输入收件人地址
to_addr = input('To:')
#输入SMTP服务器地址
smtp_server = input('SMTP server:')
server = smtplib.SMTP(smtp_server,25) ##SMTP默认端口号为25
server.set_debuglevel(1) ##打印出和SMTP服务器交互的所有信息
server.login(from_addr,mail_pass) ##用于登录SMTP服务器
server.sendmail(from_addr,[to_addr],msg.as_string()) ## 发送邮件，一次可以发送多个人，所以传入list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.quit()

