# Fix the mistakes in this code and test based on the description below
# If I enter 2.00 I should see the message "Tax rate is: 0.07" 
# If I enter 1.00 I should see the message "Tax rate is: 0.07" 
# If I enter 0.50 I should see the message "Tax rate is: 0" 
price = input('how much did you pay? ')

if price > 1.00:
	tax = .07
	print('Tax rate is: ' + str(tax))
else
	tax = 0
print('Tax rate is: ' + str(tax))