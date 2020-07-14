import pip._vendor.requests
import json
from dotenv import load_dotenv

load_dotenv()
import os
from pip._vendor import requests

subskey = os.getenv('SUBSCRIPTION_KEY')
print(subskey)