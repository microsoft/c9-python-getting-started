def sorter(item):
    return item['name']


presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]
presenters.sort(key=sorter)
print(presenters)
