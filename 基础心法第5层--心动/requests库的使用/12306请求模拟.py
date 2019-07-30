import requests

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-06-19&leftTicketDTO.from_station=WHN&leftTicketDTO.to_station=CDW&purpose_codes=ADULT'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=9EAE79D6E3C62B6CAA7A0F293A4F585A; BIGipServerotn=1977155850.24610.0000; RAIL_EXPIRATION=1561264922306; RAIL_DEVICEID=V9w9eHaf1tkJXE7b2761lN5-uH3UMAQ1qV_G8hcy6_NI5CLf4SzxJ4pmVs1nT_tzri3LReqkTYjf_HGqz45qBsLsTL92NFh4DaEVjzAuB8Y9H8UsWNt-ZX3Lbsr6qIhoh09FC0yP8iBgWqZ-eZN-H_AhtYkK5aKp; BIGipServerpassport=837288202.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u6B66%u6C49%2CWHN; _jc_save_toStation=%u6210%u90FD%2CCDW; _jc_save_fromDate=2019-06-19; _jc_save_toDate=2019-06-19; _jc_save_wfdc_flag=dc',
    'Host': 'kyfw.12306.cn',
    'If-Modified-Since': '0',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

r = requests.get(url, headers=headers)
for k, v in r.json().items():
    print(k, v)
# print(requests.codes.ok)

