def main():
    f = open('cat.jpg', 'rb')
    data = f.read()
    f2 = open('cat1.jpg', 'wb')
    f2.write(data)


if __name__ == '__main__':
    main()
