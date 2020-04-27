# Create function get_initial to accept a name and 
# return the first letter of the name in uppercase
# Parameters:
#   name: the name of a person
# Return value:
#   first letter of name passed in as a parameter in uppercase 
def get_initial(name):
    initial = name[0:1].upper()
    return initial

#Ask for someone's name and return the initials
first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

# Call get_initial function to return first letter of a name
print('Your initials are: ' \
    + get_initial(first_name) \
    + get_initial(middle_name) \
    + get_initial(last_name))