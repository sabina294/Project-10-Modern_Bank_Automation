credentials = [
    {"username": "admin", "password": "123456"},
    {"username": "user", "password": "1234567"},
    {"username": "manager", "password": "12345678"},
    {"username": "customer", "password": "1234567890"}
]

input_username = input("Enter Username:")
input_password = input('Enter Password:')

login_success = False

for user in credentials:
    if user["username"] == input_username and user["password"] == input_password:
        print("Login Success")
        login_success = True
        break

if not login_success:
    print("Login Failed !!")

