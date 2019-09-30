import threading
from queue import Queue
import time
import os

def set_value(qu):
    '''生成元素放入列队'''
    index = 0
    while True:
        qu.put(index)
        index += 1
        start = time.time()
        time.sleep(2)  # 每隔三秒放入一个
        end = time.time()
        print('阻塞时间为：',end-start,'秒threading.Thread')


def get_value(qu):
    while True:
        print('数据：',qu.get())  # 列队中有数据就取出来，没有就等待


if __name__ == '__main__':
    qu = Queue(4)
    t1 = threading.Thread(target=set_value,args=[qu])
    t2 = threading.Thread(target=get_value,args=[qu])

    t1.start()
    t2.start()
    os.system("pause")