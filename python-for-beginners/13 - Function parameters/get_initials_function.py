# This function will take a name and return the 
# Create a function to return the first initial of a name
# Parameters:
#   name: name of person
# Return value
#   first letter of name passed in
def get_initial(name):
    initial = name[0:1].upper()
    return initial

# Ask for someone's name and return the initials
first_name = input('Enter your first name: ')

# Call get_initial function to retrieve first letter of name
first_name_initial = get_initial(first_name)

print('Your initial is: ' + first_name_initial)