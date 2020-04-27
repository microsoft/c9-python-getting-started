# Python has to guess what datatype a variable should be

# since the input function returns a string, the variables it populates
# will hold string values
first_num = input('Enter first number ')
second_num = input('Enter second number ')

# Because first_num and second_num are string variables the + operator
# concatenates them just like concatenating first_name and last_name
print(first_num + second_num)