#To get current date and time we need to use the datetime library
from datetime import datetime

current_date = datetime.now()
# The now function returns current date and time as a datetime object

# You must convert the datetime object to a string
# before you can concatenate it to another string
print('Today is: ' + str(current_date))
