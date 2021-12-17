import requests

# SHEETY_PRICES_ENDPOINT=

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Type your email agin.\n")
body = {"user": {
    "First Name": first_name,
    "Last Name": last_name,
    "Email": email}}
header = {
    'Content-Type': 'application/json'
}
# if email == confirm_email:
response = requests.post(url="https://api.sheety.co/e588a0356ad7eb7694b2965ef64b23dc/flightDeals/users", json=body)
print(response.text)
