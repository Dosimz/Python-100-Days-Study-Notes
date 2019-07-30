import time
import requests

# class message_send(object):
#     def __init__(self, mobile):
#         self.url = "https://login.ceconline.com/thirdPartLogin.do"

#         self.header = {
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
#         "Referer": "https://login.ceconline.com/pcMobileNumberRegister.do"
#         }

#         self.mobile = mobile

#     def get_response(self):
#         time_now = int(time.time() * 1000)

#         data = {
#             "mobileNumber": self.mobile,
#             "method": "getDynamicCode",
#             "verifyType": "MOBILE_NUM_REG",
#             "captcharType": "",
#             "time": str(time_now)
#         }

#     try:
#         response = requests.post(url=self.url, data=self.data, header=self.header)
#         print()
#     except:
#         print('失败')

#     def run(self):
#         self.get_response()
# -----------------------------------------------------


class message_send_ntjxj(object):
    def __init__(self, mobile):
        self.url = "https://www.ntjxj.com/InternetWeb/SendYzmServlet"

        self.header = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
        "Referer" : "https://www.ntjxj.com/InternetWeb/regHphmToTel.jsp"
        }

        self.mobile = mobile

    def get_response(self):

        data = {
            "sjhm": self.mobile
        }
        print(data)
        print('1')
        response = requests.post(url=self.url, data=data, headers=self.header)
        print(response.content)
        print('成功')
        # except Exception:
        #     print('失败')

    def run(self):
        self.get_response()

if __name__ == "__main__":
     ntjxj = message_send_ntjxj('19983420869')
     ntjxj.get_response()