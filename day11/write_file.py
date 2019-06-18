from math import sqrt


def is_prime(num):
    """
    判断是否素数
    :param num: 要判断的数
    :return: 返回True或者False
    """
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True if num != 1 else False


def main():
    filenames = ['a.txt', 'b.txt', 'c.txt']
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w'))
        for num in range(1, 10000):
            if is_prime(num):
                if num < 100:
                    fs_list[0].write(str(num) + '\n')
                elif num < 1000:
                    fs_list[1].write(str(num) + '\n')
                else:
                    fs_list[2].write(str(num) + '\n')
    except IOError as e:
        print(e)
        print('写文件错误')
    finally:
        for fs in fs_list:
            fs.close()


if __name__ == '__main__':
    main()
