# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.


##
# Compute the area of a room
#

# Read the input from the user
width = float(input("Please input the width of the room in centimeter: "))
length = float(input("Please input the length of the room in centimeter: "))

# Compute the area of the room
area = width * length
print('The area of the room is', area, 'square centimeter')
