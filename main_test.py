#coding:utf-8
import os
from co_name import CoName
import time
import random
from multiprocessing import Process,Queue,Pool,Manager
path="D:/document/simple/2017-08-22-17h09m39s"
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in write_html():
        # print('Put %s to queue...' % value)
        q.put(value)
        # print q.get(True)
        # time.sleep(random.random())

def write_html():
    # 得到文件夹下的所有文件名称
    file_path = path
    for file_name in os.listdir(file_path):
        with open(os.path.join(path, file_name), 'r') as f:
            yield f.read()

def deal(html):
    try:
        co = CoName(html)
        copyright = co.get_copyright()
        # urls = co.get_url()

    except Exception as e:
        print e
    else:
        if copyright:
            print copyright

def deal_html(q):
    print('Process to read: %s' % os.getpid())
    while True:
        if not q.empty():
            value = q.get(True)
            deal(value)
        else:
            break


if __name__ == '__main__':
    manager = Manager()
    t = time.time()
    q = manager.Queue()
    p = Pool()
    pw = p.apply_async(write,args=(q,))
    for i in range(1):
        p.apply_async(deal_html, args=(q,))
    p.close()
    p.join()
    print time.time()-t




