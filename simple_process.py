#!/usr/bin/env python3
import time

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
    for i in range(5):
        io_task()
    end_time = time.time()
    # 打印运行耗时, 保留 2 位小数
    print('程序运行耗时: {:.2f}s'.format(end_time-start_time))

if __name__ == '__main__':
    main()
