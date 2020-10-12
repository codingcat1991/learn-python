# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

SQUARE_FEET_PER_ACRE = 43560

# Read input from the user
width = float(input('Please input the width of the field in feet: '))
length = float(input('Please input the length of the field in feet: '))

# Compute the area in acres
acres = (width * length) / SQUARE_FEET_PER_ACRE

# Display the result
print('the area of the field is', acres, 'ares')
