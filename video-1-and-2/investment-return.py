'''
your_float = input("Enter a float: ")
your_float = float(your_float)
 print("Round to 2 decimas : {:.2f}".format(your_float))
'''

# Have the user enter their investment amount and expected intetrest
amount = input("Investment amount: ")
amount = float(amount)

interest = input("Interest rate (percent): ")
interest = float(interest)*.01

# Each year their investment will increase by their investment + their investment * interest tare is
for i in range(10):
    amount=amount+amount*interest
# Print out the earnings after a 10 year period
print ("After 10 years your capital will be: {:.2f}".format(amount))
