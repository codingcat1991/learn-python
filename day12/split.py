import re


def main():
    text = input('')
    pattern = re.compile('[,.;]')
    ls = re.split(pattern, text)
    print(ls)


if __name__ == '__main__':
    main()
