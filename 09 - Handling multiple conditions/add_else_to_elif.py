province = input("What province do you live in? ")
tax = 0

if province == 'Alberta':
	tax = 0.05
elif province == 'Nunavut':
	tax = 0.05
elif province == 'Ontario':
	tax = 0.13
else:
	tax = 0.15
print(tax)