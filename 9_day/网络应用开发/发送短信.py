import urllib.parse
import http.client
import json
from random import randint

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

def send_sms(text, mobile):
    params = urllib.parse.urlencode({'account': 'C70858600', 'password': 'c81ab586f24a37bed09c3ead015bc40b',
                                'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    # print(json.loads(jsonstr))
    conn.close()
    return json.loads(jsonstr)

def random_num():
    return randint(100000, 999999)
    
if __name__ == "__main__":
    mobile = "15528231027"
    text = "您的验证码是：" + str(random_num()) + "。请不要把验证码泄露给其他人。"
    # print(text)
    print(send_sms(text, mobile))
