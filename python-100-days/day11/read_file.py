import time


def main():
    with open(file='致橡树.txt', mode='r', encoding='utf8') as f:
        print(f.read())

    with open('致橡树.txt', mode='r', encoding='utf8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open('致橡树.txt', mode='r', encoding='utf8') as f:
        lines = f.readlines()
    print(lines)


def main2():
    f = open(file='致橡树.txt', mode='r', encoding='utf8')
    print(f.read())


def main3():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
