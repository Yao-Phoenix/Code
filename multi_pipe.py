#!/usr/bin/env pythom3
# 首先引入 Pipe 类
from multiprocessing import Process, Pipe
# 创建一个管道, 注意 Pipe 的实例是一个元组, 里面有两个连接器, 可以把他们想象成通讯员
conn1, conn2 = Pipe()

def send():
    data = 'hello shiyanlou'
    conn1.send(data)
    print('Send Data: {}'.format(data))

def recv():
    data = conn2.recv()
    print('Receive Data: {}'.format(data))

def main():
    Process(target=send).start()
    Process(target=recv).start()

if __name__ == '__main__':
    main()
