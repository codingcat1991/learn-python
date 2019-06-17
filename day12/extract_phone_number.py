import re


def main():
    # 让下一代天策府v光看不回了你就1234567890scs13698765432adasdcas
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    text = input('请输入文字：')
    print(re.findall(pattern, text))
    for temp in pattern.finditer(text):
        print(temp.group())
    m = pattern.search(text)
    while m:
        print(m.group())
        m = pattern.search(text, m.end())


if __name__ == '__main__':
    main()
