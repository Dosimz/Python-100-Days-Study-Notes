import requests
import re

cs_url = 'https://github.com/login'
cs_user = 'Dosimz'
cs_psw = 'Vhzixab23'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://github.com/',
    'Host': 'github.com'
}
s = requests.Session()
r = s.get(cs_url, headers=headers)
print(str(r.content))
reg = r'<input type="hidden" name="authenticity_token" value="(.*)" />'
pattern = re.compile(reg)
result = pattern.findall(r.text)
token = result[0]

post_data = {
    'commit': 'Sign in',
    # 'utf8': '',
    'authenticity_token': token,
    'login': cs_user,
    'password': cs_psw,
}
cs__url = 'https://github.com/session'
r = s.post(cs__url, headers=headers, data=post_data)
print(r.url, r.status_code, r.history)
