from random import randint
from threading import Thread
from time import sleep, time


def download_task(filename):
    print('开始下载%s.....' % filename)
    download_time = randint(5, 10)
    sleep(download_time)
    print('%s下载完成，耗时：%d秒' % (filename, download_time))


def main():
    start = time()
    t1 = Thread(target=download_task, args=('Python从入门到住院.pdf',))
    t2 = Thread(target=download_task, args=('Peking Hot.avi',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总耗时%.3f ' % (end - start))


if __name__ == '__main__':
    main()
