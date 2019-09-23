# Fix the mistakes in this code and test using the following
# If I enter 2.00 I should see the message "Tax rate is: 0.07" 
# If I enter 1.00 I should see the message "Tax rate is: 0.07" 
# If I enter 0.50 I should see the message "Tax rate is: 0" 
price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
	tax = .07
	print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is: ' + str(tax))