#Calculate the tax
# Anything purchased for more than $1.00 is charged a 7% tax
price = input('how much did you pay? ')

# Convert the string to a number
price = float(price)

# Check if the price is greater than 1.00
if price >= 1.00:
	# Everything over $1.00 is charged 7% tax
	tax = .07
	print('Tax rate is: ' + str(tax))
