#!/usr/bin/env python3
import time
from multiprocessing import Process, Value, Lock

# 该函数运行在子进程中,参数 val 是一个 Value对象, 是全局变量
def func(val, lock):
    # 将 val 这个全局变量的值进行 50 次 +1 操作
    for i in range(50):
        time.sleep(0.01)
        # with lock 语句是对下面语句的简写:
        '''
        lock.acquire()
        val.value += 1
        lock.release()
        '''
        # 为 val 变量加锁, 结果就是任何时刻只有一个进程可以获得 lock 锁
        # 自然 val 的值就不会同时被多个进程改变
        with lock:
            val.value += 1

def main():
    # 多进程无法使用全局变量, multiprocessing 提供的 Value 是一个代理器, 可以实现在多进程中共享这个变量
    # val 是一个 Value 对象, 他是全局变量, 数据类型为 int, 初始值为 0
    val = Value('i', 0)
    # 初始化锁
    # Lock 和 Value 一样, 是一个函数或者叫方法, Lock 的返回值就是一把全局锁
    # 注意这把全局锁的使用范围就是当前主进程及其子进程, 也就是在运行当前这个 Python 文件过程中有效
    lock = Lock()
    # 创建 10 个任务, 备用
    processes = [Process(target=func, args=(val, lock)) for i in range(10)]
    # 启动 10 个子进程来运行 proce 中的任务, 对 Value 对象进行 +1 操作
    for p in processes:
        p.start()
    # join 方法使主进程挂起, 直至所有子进程运行完毕
    for p in processes:
        p.join()
    print(val.value)

if __name__ == '__main__':
    for i in range(5):
        main()
