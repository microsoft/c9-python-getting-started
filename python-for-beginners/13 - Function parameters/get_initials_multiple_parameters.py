# Create a function to return the first initial of a name
# Parameters:
#   name: name of person
#   force_uppercase: indicates if you always want the initial to be in upppercase
# Return value
#   first letter of name passed in
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

#Ask for someone's name and return the initial
first_name = input('Enter your first name: ')

# Call get_initial function to retrieve first letter of name
# Alwasy return initial in uppercase
first_name_initial = get_initial(first_name, False)

print('Your initial is: ' + first_name_initial)