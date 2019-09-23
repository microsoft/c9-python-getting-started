price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
	# Anything that costs $1.00 or more is charged 7% tax
	# All statements indented are only executed if price is > = 1
	tax = .07
	print('Tax rate is: ' + str(tax))
else:
	# Anything else we do not charge any tax
	# All statements indented are only executed if price is NOT >= 1 
	tax = 0
	print('Tax rate is: ' + str(tax))


