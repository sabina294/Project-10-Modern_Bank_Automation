for i in range(50):
    if i == 2:
        break
    print(i,"Hello World!!")

username = ["admin","super admin", "customer", "manager"]

if "admin123" in username:
    print("Username Found.")
else:
    print('Username not found.')

password_list = [12345,123456,1111,123]
for my_password in password_list:
    if my_password == 12345000:
        print("Password Found", my_password)
        break


expected_name = "David"

api_response = [
    {"id":1, "name": "Alice", "role": "admin"},
    {"id":2, "name": "Michael", "role": "manager"},
    {"id":3, "name": "David", "role": "customer"}
]

# verify if a user named "Alice" exists in response or not
found = False

for user in api_response:
    if user["name"] == expected_name:
        found = True
        print(f"{expected_name} User exists. Role:", user["role"])
        break

if not found:
    print(f"{expected_name}User does not exist!")


test_result_status = ["pass", "pass", "pass", "pass", "fail", "fail"]

# verify if any test failed
if "fail" in test_result_status:
    print("At least one test failed.")
else:
    print("All tests passed.")

# count total test executed, pass and fail
total_test_executed = len(test_result_status)
total_pass = test_result_status.count("pass")
total_fail = test_result_status.count("fail")

print("Total Test Executed:", total_test_executed)
print("Total Pass:", total_pass)
print("Total Fail:", total_fail)


expected_login_test_result = ["login", "error", "login", "error", "login", "login"]
actual_login_test_result   = ["error", "login", "login", "error", "error", "login"]

# Verify any mismatch
"""
Test 1: Mismatch
Test 2: Mismatch
Test 3: Match
Test 4: Match
Test 5: Mismatch
Test 6: Match
"""

for i in range(len(expected_login_test_result)):
    if actual_login_test_result[i] == expected_login_test_result[i]:
        print(f"Test {i+1}: Match")
    else:
        print(f"Test {i+1}: Mismatch")

