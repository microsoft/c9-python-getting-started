country = 'CANADA'
# by converting the string entered to lowercase and comparing it to a string
# that is all lowercase letters I make the comparison case-insensitive
# If someone types in CANADA or Canada it will still be a match
if country.lower() == 'canada':
	print('Hello eh')
else:
	print('Hello')
