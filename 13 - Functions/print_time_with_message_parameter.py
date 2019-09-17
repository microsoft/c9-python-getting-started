from datetime import datetime

# Define a function to print the current time and task name
# Function the following parameters:
#   task_name: Name of the task to display to output screen
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
# Call print_time() function to display message and current time
# pass in name of task completed
print_time('first name assigned')

for x in range(0,10):
	print(x)
# Call print_time() function to display message and current time
# pass in name of task completed
print_time('loop completed')
