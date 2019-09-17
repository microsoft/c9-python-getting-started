# import the datetime and timedelta modules
from datetime import datetime, timedelta

# When you ask a user for a date tell them the desired date format
birthday = input('When is your birthday (dd/mm/yyyy)? ')

# When you convert the string containing the date into a date object
# you must specify the expected date format
# if the date is not in the expected format Python will raise an exception
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print ('Birthday: ' + str(birthday_date))

# Because we converted the string into a date object
# We can use date and time functions such as timedelta with the object
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
