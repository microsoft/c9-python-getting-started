# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python 
import requests

# We will need the json library to read the data passed back 
# by the web service
import json

# We need the address of our Computer vision service
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"
# Add the name of the function we want to call to the address
address = vision_service_address + "analyze"

# According to the documentation for the analyze image function 
# There are three optional parameters: language, details & visualFeatures
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# We need the key to access our Computer Vision Service
subscription_key = "xxxxxxxxxxxxxxxxxxxx"

# Open the image file to get a file object containing the image to analyze
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, 'rb').read()

# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': subscription_key}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the raw JSON results returned
results = response.json()
print(json.dumps(results))

# print the value for requestId from the JSON output
print()
print('requestId')
print (results['requestId'])