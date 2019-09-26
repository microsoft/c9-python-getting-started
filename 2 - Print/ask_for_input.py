# The input funciton allows you to prompt the user for a value
# You need to declare a variable to hold the value entered by the user
"""
If you are having this kind of error:
What is your name?
jhon

Traceback (most recent call last):
  File "input_test.py", line 1, in <module>
    name = input("What's your name? ")
  File "<string>", line 1, in <module>
NameError: name 'Frank' is not defined

Solution:
What is your name?
"jhon"


"""
name = input('What is your name? ')

print(name)