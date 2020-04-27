# This code will return an error because the sort method does not know
# which presenter field to use when sorting
presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort()
print(presenters)
