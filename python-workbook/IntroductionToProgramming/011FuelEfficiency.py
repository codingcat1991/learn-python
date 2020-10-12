# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
# (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPGto L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.

# 1美制加仑=3.785411784升
# 1英里(mi) = 1.60934千米bai(公里)
# 1MPG = 1.60934KM/gallon
LITERS_PER_GALLON = 3.785411784
KILOMETERS_PER_MILE = 1.60934

mpg = float(input('Enter the value in American units: '))
l_100_km = 1 / ((mpg * KILOMETERS_PER_MILE) / (LITERS_PER_GALLON * 100))

print('The equivalent fuel efficiency in Canadian units is', l_100_km)
