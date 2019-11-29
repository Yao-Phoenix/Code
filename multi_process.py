#!/usr/bin/env python3
import time
# 引入 Process 类
from multiprocessing import Process

def io_task():
    # time.sleep 强行刮起当前进程 1 秒钟
    # 所谓 "挂起", 就是进程停滞, 后续代码无法运行, CPU无法进行工作的状态
    # 相当于进行了一个耗时 1 秒钟的 IO 操作
    # 上文提到过的, IO 操作可能会比较耗时, 但它不会占用 CPU
    # 在这一秒时间内, CPU 可能被运算器派往其他进程 / 线程中工作
    time.sleep(1)

def main():
    start_time = time.time()
    # 循环 IO 操作 5 次
    '''
    for i in range(5):
        io_task()
    end_time = time.time()
    '''
    # 创建一个列表放子任务备用
    process_list = []
    #创建 5 个多进程任务并加入到任务列表中
    for i in range(5):
        process_list.append(Process(target=io_task))
    # 启动所有子任务
    # 此时操作系统会创建 5 个子进程并派出闲置的 CPU 来运行 io_task()函数
    for process in process_list:
        process.start()
    # join 方法将主进程挂起并释放 CPU 在一旁候着, 直到所有子进程运行完毕
    for process in process_list:
        process.join()
    # 子进程运行完毕, 以下代码运行在主进程中
    end_time = time.time()
    print('程序运行耗时: {:.2f}s'.format(end_time-start_time))

if __name__ == '__main__':
    main()
