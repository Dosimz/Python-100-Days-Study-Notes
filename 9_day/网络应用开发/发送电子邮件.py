from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    # 请自行修改下面的邮件发送者和接收者
        sender = 'yuyiyikyym@126.com'
        secretpass = 'yuyiyikyyl33'
        receivers = '921207964@qq.com'
        message = MIMEText('用 Python 发送邮件的示例代码.', 'plain', 'utf-8')
        message['From'] = sender    #Header('Richard.锦鸡娃儿', 'utf-8')
        message['To'] = receivers   #Header('余一一', 'utf-8')
        message['Subject'] = Header('示例代码实验邮件', 'utf-8')
        smtper = SMTP('smtp.126.com')
    # 请自行修改下面的登录口令
        smtper.login(sender, secretpass)
        smtper.sendmail(sender, receivers, message.as_string())
        print('邮件发送完毕!')

if __name__ == "__main__":
    main()