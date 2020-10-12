from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号【%d】' % getpid())
    print('开始下载%s.....' % filename)
    download_time = randint(10, 20)
    sleep(download_time)
    print('%s下载完成，耗时：%d秒' % (filename, download_time))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
