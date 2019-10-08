# Ask the user for their first and last name
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# Custom string formatting
# Using the + operator to concatenate strings
print ('Hello ' + first_name + ' '  + last_name)

# Using place holders to print strings 
print ('Hello, {} {} '.format(first_name, last_name)

# Using index numbers {0} and {1} to be sure the arguments are placed in the correct placeholders 
print ('Hello {0} {1}'.format(first_name, last_name)

# Reversing the index numbers to change the positions of placeholders
print ('Hello {1} {0}'.format(first_name, last_name)

# Only available in Python 3
print (f'Hello, {first_name} {last_name}')
