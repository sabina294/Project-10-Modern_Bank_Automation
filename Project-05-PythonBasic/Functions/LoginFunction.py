from datetime import datetime

def login(username, password, expected_result):
    if username == "admin" and password == "123456":
        actual_result = "Login Successful"
    else:
        actual_result = "Login Failed"

    execution_date = datetime.now().strftime("%d-%m-%Y")
    execution_time = datetime.now().strftime("%I:%M %p")


    if actual_result == expected_result:
        print(f"Execution Date: {execution_date}, Execution Time: {execution_time}, Result: Test Passed")
    else:
        print(f"Execution Date: {execution_date}, Execution Time: {execution_time}, Result: Test Failed")


# login("admin", "123456", "Login Successful")
# login("admin123", "123456", "Login Failed")

test_cases = [
    ("admin", "123456", "Login Successful"),
    ("admin", "12", "Login Failed"),
    ("admin12", "123456", "Login Failed"),
    ("admin121212", "1234563223", "Login Failed")
]

for case in test_cases:
    login(*case)

test_data = [
    {
        "username": "admin",
        "password": "123456",
        "expected_result": "Login Successful"
    },
    {
        "username": "admin",
        "password": "123456222", ""
                                 "expected_result": "Login Failed"
    },
    {
        "username": "admin121",
        "password": "123456",
        "expected_result": "Login Failed"
    },
    {
        "username": "",
        "password": "",
        "expected_result": "Login Failed"
    }
]

for data in test_data:
    login(**data)


def myfunction():
    pass


myfunction()

# Execution Date: 10-07-2025, Time: 8:10 Pm, Result: Test Passed
