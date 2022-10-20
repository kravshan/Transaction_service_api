import requests

BASE = "http://127.0.0.1:5000/"

#Creating new accounts
response = requests.put(BASE + "account/10", {"account_number": 10, "balance": 500})
print(response.json())

response = requests.put(BASE + "account/11", {"account_number": 10, "balance": 700})
print(response.json())

response = requests.put(BASE + "account/12", {"account_number": 10, "balance": 700})
print(response.json())

#Reading created accounts
response = requests.get(BASE + "account/10")
print(response.json())

response = requests.get(BASE + "account/11")
print(response.json())

response = requests.get(BASE + "account/12")
print(response.json())

#Updating some accounts
response = requests.put(BASE + "account/10", {"balance": 890})
print(response.json())

response = requests.put(BASE + "account/12", {"balance": 2400})
print(response.json())

#Deleting an account
response = requests.delete(BASE + "account/12")
print(response.json())

#Trying to read the deleted account
response = requests.get(BASE + "account/12")
print(response.json())