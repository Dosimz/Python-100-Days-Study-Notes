
# import math
# """将这个任务分解到 8 个进程中执行"""

from multiprocessing import Process, Queue
from time import time

def is_prime(n):
    count =  0
    prime = []
    for _ in range(n+1):
        prime.append(True)
    for i in range(2, n+1):
        if prime[i]:
            print(i)
            count += 1
            j = i + i
            while j <= n:
                prime[j] = False
                j += i
    print(count)
is_prime(90990000)

#
# def is_prime(num):
#     if num < 2: return False
#     if num % 2 == 0: return False
#     for i in range(3, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
#
# def task_handler(curr_list, result_queue):
#     total = 0
#     for number in curr_list:
#         if is_prime(number):
#             total += 1
#     result_queue.put(total)
#
# def main():
#     processes = []
#     number_list = [x for x in range(1, 90000000)]
#     result_queue = Queue()
#     index = 0
#     # 启动8个进程将数据切片后进行运算
#     for _ in range(8):
#         p = Process(target = task_handler, args = (number_list[index: index + 11250000], result_queue))
#         index += 11250000
#         processes.append(p)
#         p.start()
#     # 开始记录所有进程执行完成花费的时间
#     start = time()
#     for p in processes:
#         p.join()
#     # 合并执行结果
#     total = 0
#     while not result_queue.empty():
#         total += result_queue.get()
#     print(total)
#     end = time()
#     print('Execution time: ', (end - start), 's', sep='')
#
# if __name__ == "__main__":
#     main()


# l = math.log(1000000)
# res = 10000000/l
# print(res)

# l = math.log(x)
# x = 5209527*l
# print(x)

