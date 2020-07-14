#Tuple is a collection of ordered items. A tuple is immutable in nature. 
#Refer https://docs.python.org/3/library/stdtypes.html?#tuples for more information 
person= ("Susan","Christopher","Bill","Susan")
print(person)
print(person[1])
x= person.count("Susan")
print("Occurrence of 'Susan' in tuple is:" + str(x))
l=['apple','oranges']
print(tuple(l))
