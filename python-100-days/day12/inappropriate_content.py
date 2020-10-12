import re


def main():
    pattern = re.compile(r'[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔')
    text = input('请输入文本：')
    text = re.sub(pattern, '*', text)
    print(text)


if __name__ == '__main__':
    main()
