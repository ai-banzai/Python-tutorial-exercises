# Ask the user to input miles and assign it to the miles variable
miles = input('Input the distance in miles: ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by mulitplying 1.60934 times miles
kilometers = miles* 1.60934

# Print results using format()
print("{} miles equals {} kilometers.".format(miles, kilometers))
