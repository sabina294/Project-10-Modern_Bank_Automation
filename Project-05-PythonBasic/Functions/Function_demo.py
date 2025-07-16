def myFunction():
    print("Hello World!!")

myFunction()

def summation(number1, number2):
    print(number1 + number2)

summation(10,20)

def subtraction(number1, number2):
    return number1 - number2

result = subtraction(100, 50)
print(result)

print(subtraction(100,60))

def multiplication(number1, number2):
    return number1 * number2

result2 = multiplication(20,5) - subtraction(20,10)
print(result2)


def division(number1 = 10, number2=5):
    return number1 / number2

print(division()) # 2.0
print(division(100,20)) # 5.0

def calculation_sum(*args):
    return sum(args)

print(calculation_sum(10,50,10))


def user_details(name, email):
    print(f"Name: ",name)
    print(f"Email: ", email)

user_info = {
    "name": "Alice",
    "email": "alice@gmail.com"
}

# user_details(user_info["name"],user_info["email"])
user_details(**user_info)
