# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

# PERCENT = 0.04
# money = float(input('Enter the amount of money deposited into the account: '))
# money_after_1_year = money * (1 + PERCENT)
# money_after_2_year = money * (1 + PERCENT) * (1 + PERCENT)
# money_after_3_year = money * (1 + PERCENT) * (1 + PERCENT) * (1 + PERCENT)
# print('The amount in the saving account after 2 year is %.2f' % money_after_2_year)
# print('The amount in the saving account after 3 year is %.2f' % money_after_3_year)
# print('The amount in the saving account after 1 year is %.2f' % money_after_1_year)

PERCENT = 0.04
years = 3
money = float(input('Enter the amount of money deposited into the account: '))
for year in range(1, years + 1):
    money_after_year = money * pow((1 + PERCENT), year)
    print('The amount in the saving account after %d year is %.2f' % (year, money_after_year))
