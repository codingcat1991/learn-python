from random import randint
from threading import Thread
from time import sleep, time


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s.....' % self._filename)
        download_time = randint(5, 10)
        sleep(download_time)
        print('%s下载完成，耗时：%d秒' % (self._filename, download_time))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t2 = DownloadTask('Peking Hot.avi')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总耗时：%.3f' % (end - start))


if __name__ == '__main__':
    main()
