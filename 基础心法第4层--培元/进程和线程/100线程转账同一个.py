"""
得到错误的结果
"""

# from time import sleep
# from threading import Thread

# class Account(object):

#     def __init__(self):
#         self._balance = 0

#     def deposit(self, money):
#         # 计算存款后的余额
#         new_balance = self._balance + money
#         # 模拟受理存款业务需要0.01秒时间
#         sleep(0.01)
#         # 修改账户余额
#         self._balance = new_balance

#     @property
#     def balance(self):
#         return self._balance
    
# class AddMoneyThread(Thread):

#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
    
#     def run(self):
#         self._account.deposit(self._money)

# def main():
#     account = Account()
#     threads = []
#     # 创建100存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     # 等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print('账户余额为: $%d美元' % account.balance)

# if __name__ == "__main__":
#     main()

"""
使用 "锁"
"""

from time import sleep
from threading import Thread, Lock

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获得锁才能执行后续代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01秒时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance
    
class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # 创建100存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: $%d美元' % account.balance)

if __name__ == "__main__":
    main()