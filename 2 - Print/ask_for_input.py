# The input funciton allows you to prompt the user for a value
# You need to declare a variable to hold the value entered by the user


# Number of Inputs
n = int(input("Enter the Number of Inputs : "))
sum = 0 
for i in range(0, n):
	# Take Inputs
    number = int(input("Enter the Number : "))
    print ("\n")
    # Add the Inputs
    sum += number

print (sum)