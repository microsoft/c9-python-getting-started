# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name
first_name = input('Please enter your first name: ')
# Ask the user for their last name
last_name = input('Please enter your last name: ')

# if first name is < 10 characters and last name is < 10 characters 
#       print first and last name on the jersey
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only

# Check length of first name
if len(first_name) >=10:
    long_first_name = True
else:
    long_first_name = False

# Check length of last name
if len(last_name) >= 10:
    long_last_name = True
else:
    long_last_name = False
 
# Evaluate possible jersey print combinations for different lengths
if long_first_name and long_last_name:
    print(last_name)
elif long_first_name:
    print(first_name[0:1] + '. ' + last_name)
elif long_last_name:
    print(first_name + ' ' + last_name[0:1] + '.')
else:
    print(first_name + ' ' + last_name)