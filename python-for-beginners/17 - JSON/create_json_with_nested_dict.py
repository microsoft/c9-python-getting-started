import json

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'

# create a staff dictionary
# assign a person to a staff position of program manager
staff_dict ={}
staff_dict['Program Manager']=person_dict
# Convert dictionary to JSON object
staff_json = json.loads(staff_dict)

# Print JSON object
print(json.dumps(staff_json))