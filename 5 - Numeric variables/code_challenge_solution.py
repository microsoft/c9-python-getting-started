# Ask a user to enter a number
first_number = input('Enter a number: ')

# Ask a user to enter a second number
second_number = input('Enter another number: ')

# Calculate the total of the two numbers added together
answer = float(first_number) + float(second_number)

# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
print(first_number + ' + ' + second_number + ' = ' + str(answer))

# If you do not want the decimal places you could round the answer
print(first_number + ' + ' + second_number + ' = ' + str(round(answer)))