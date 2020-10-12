# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1)/2


n = int(input('Enter a positive integer: '))
s = (n * (n + 1)) / 2
print('The sum of the integers from 1 to %d is: %d' % (n, s))

# 方法二，不是最优，时间复杂度比上一个方法高
# sm = 0
# for i in range(1, n + 1):
#     sm += i
# print(sm)
