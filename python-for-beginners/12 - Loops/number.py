# range() returns a sequence of numbers
# optional( by default it starts with 0) : First parameter is the starter
# Second parameter(Required) indicates where it need to stop but that number will be exculded in range()
# If you want to include the last number then just add by 1
# range(0, 2) creates [0, 1]
# Third Parameter(Optional) : This number will tell the program to take a jump(increment/decrement) in that range. By default the value for jump is +1.

for index in range(10):
	print(index)
	
#This program will print the number from 0 to 9 in new lines. Since the 10 is exculded it will not print it
