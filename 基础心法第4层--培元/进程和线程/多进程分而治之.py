# from time import time

# def main():
#     total = 0
#     number_list = [x for x in range(1, 90000000)]
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print('Exception time: %.3fs' % (end - start))

# if __name__ == "__main__":
#     main()

"""将这个任务分解到 8 个进程中执行"""

from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1, 90000000)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target = task_handler, args = (number_list[index: index + 11250000], result_queue))
        index += 11250000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')

if __name__ == "__main__":
    main()