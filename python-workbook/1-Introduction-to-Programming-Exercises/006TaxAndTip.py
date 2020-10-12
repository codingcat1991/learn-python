# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

##
# Compute the tax and tip for a restaurant meal
#
TAX_RATE = 0.05
TIP_RATE = 0.18

# Read input from the user
cost = float(input('Enter the cost of the meal: '))

# Compute the tax and the tip
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip

# Display the result
print('The tax is %.2f and the tip is %.2f, making the total %.2f' % (tax, tip, total))
