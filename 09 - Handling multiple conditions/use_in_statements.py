province = input("What province do you live in? ")
tax = 0
# If multiple values cause the same output you can combine them by listing all 
# values you want to check for with the in operator
if province in('Alberta','Nunavut','Yukon'):
	tax = 0.05
elif province == 'Ontario':
	tax = 0.13
else:
	tax = 0.15
print(tax)