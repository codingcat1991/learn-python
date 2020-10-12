# Create a program that reads two integers, a and b, from the user.Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list.
from math import log10

a = int(input('Enter integer a:'))
b = int(input('Enter integer b:'))

print('The sum of a and b is', a + b)
print('The difference where b is subtracted from a is', a - b)
print('The product of a and b is', a and b)
print('The quotient when a is divided by b is', a / b)
print('The remainder when a is divided by b', a % b)
print('The result of log10a is', log10(a))
print('The result of a^b is', a ** b)
