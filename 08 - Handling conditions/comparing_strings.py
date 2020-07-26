country = input('Enter the name of your home country: ')
if country == 'canada':
	# string comparisons are case sensitive
	# if you typed in CANADA or Canada it will not match
	print('So you must like hockey!')
else:
	print('You are not from Canada')
