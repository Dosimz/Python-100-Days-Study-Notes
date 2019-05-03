"""
smtplib.SMTPDataError: (554, b'DT:SPM 126 smtp1,C8mowAB3ykyWOcxcbWukBA--.12803S2 
1556887958,please see 
http://mail.163.com/help/help_spam_16.htm?ip=171.210.241.142&hostid=smtp1&time=1556887958')
"""
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('测试一下呀,附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/run/media/yuyi/068AE93F8AE92BBD/docs/RatingTable.pdf', 'rb') as f:
        pdf = MIMEText(f.read(), 'base64', 'utf-8')
        pdf['Content-Type'] = 'application/pdf'
        pdf['Content-Disposition'] = 'attachment; filename=rating-table.pdf'
        message.attach(pdf)

    with open('/run/media/yuyi/068AE93F8AE92BBD/docs/smtpText', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=smtpText.txt'
        message.attach(txt)

    # 创建 SMTP 对象
    smtper = SMTP('smtp.126.com')
    # 开启安全连接
    smtper.starttls()
    sender = 'yuyiyikyym@126.com'
    receivers = ['921207964@qq.com']
    # 登录到 SMTP 服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    secretpass = 'yuyiyikyyl33'
    smtper.login(sender, secretpass)
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')

if __name__ == "__main__":
    main()