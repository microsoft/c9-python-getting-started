# Ask for a name and return the initials
first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]

middle_name = input('Enter your middle name: ')
middle_name_initial = middle_name[0:1]

last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial \
	+ middle_name_initial + last_name_initial)

