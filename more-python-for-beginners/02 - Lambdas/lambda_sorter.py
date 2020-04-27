# Sort alphabetically
presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

# Sort by length of name (shortest to longest)
presenters.sort(key=lambda item: len(item['name']))
print('-- length --')
print(presenters)
