#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import sys
import smtplib
import getopt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.Utils import COMMASPACE, formatdate
reload(sys)

smtp_server = "smtp_server"
mail_from = "mail_from"
mail_user = "mail_user"
mail_pwd = "mail_password"
mail_to = ['mail_to']


def send_mail(to, subject, text, from_mail, mail_user, mail_password, server):
    message = MIMEMultipart()
    message['From'] = from_mail
    message['To'] = COMMASPACE.join(to)
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = subject
    message.attach(MIMEText(text, _charset='utf-8'))
    smtp = smtplib.SMTP(host=server, port=587)
    smtp.login(mail_user, mail_password)
    smtp.sendmail(from_mail, to, message.as_string())
    smtp.close()


if __name__ == "__main__":
    opts,args = getopt.getopt(sys.argv[1:], "h", ["orig_master_host=", "new_master_host=", "new_slave_hosts=", "conf=", "subject=","body="])
    for lines in opts:
        key,values = lines
        if key == '--orig_master_host':
            orig_master_host = values
        if key == '--new_master_host':
            new_master_host = values
        if key == '--new_slave_hosts':
            new_slave_hosts = values
        if key == '--subject':
            subject = values
        if key == '--body':
            body = values
    mail_list = mail_to
    send_mail(mail_list, subject.encode("utf8"), body, mail_from, mail_user, mail_pwd, server=smtp_server)