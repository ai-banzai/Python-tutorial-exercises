# If age is 5 Go to Kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater than 17 say go to college
# Try to complete with 10 or less lines

# Ask for the age
age = input('What is your age? ')
age = int(age)

# Handle if age < 5
if age < 5:
    print("Too Young for School")

# Special output just for age 5
if (age == 5):
    print("Go to Kindergarten.")

# Since a number is the result for ages 6 - 17 we can check them all with 1 condition
elif (age >= 6) and (age <= 17):
    print("Go to {} grade.".format(age-5))

# Handle college
elif (age > 17):
    print ("Go to college")

# Handle everything else just in case
else:
    print("Whatever you say mate.")
