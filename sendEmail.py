#coding=utf-8
#-*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import csv

file ='1.csv'
with open(file, "r", encoding="ISO-8859-1") as csv_file:  
    read = csv.reader(csv_file)
    for line in read:
        to_addr =line[1]
from_addr ='365295672@qq.com'
password = 'xxx'
#此处填写邮箱密码，保持隐私采用xxx代表
print('recevier:' + to_addr)
smtp_server = 'smtp.qq.com'
msg = MIMEText('PythonTest','plain','utf-8')
msg['From'] =from_addr
msg['To'] = to_addr
msg['Subject'] = Header('This is a Python Email','utf-8').encode()
server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
print('send success!')
