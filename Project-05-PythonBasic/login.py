default_username = "admin"
default_password = "123456"

username = input("Enter Username:")
password = input('Enter Password:')

if username == default_username and password == default_password:
    print('Login Successful.')
else:
    print("Invalid Credentials !!")
