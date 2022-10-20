import requests

BASE = "http://127.0.0.1:5000/"

number_1 = 12345
response = requests.put(BASE + "account/" + str(number_1), {"account_number": number_1, "balance": 900})
print(response.json())

# response = requests.put(BASE + "account/54321", {"balance": 300})
# print(response.json())

response = requests.get(BASE + "account/12345")
print(response.json())

# response = requests.delete(BASE + "account/2")
# print(response.json())

# response = requests.get(BASE + "account/2")
# print(response.json())
