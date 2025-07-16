# 1.single try / single except
try:
    result = 10 / 1
    print(result)
except ZeroDivisionError:
    print("Mathematical Exception !")

# 2. single try / multiple except:
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Value Error!! Invalid number format.")
except ZeroDivisionError:
    print("ZeroDivisionError Error.")

# Multiple Exceptions in one except
try:
    number = int("abc")
    print(number)
except(ValueError, TypeError):
    print("Caught a ValueError or TypeError !!")

# 4. Generic Exception
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except Exception as errorType:
    print("Error:", errorType)

# type error
name = "Alice"
age = 30
try:
    message = "Hello, " + name + "! You are " + age + " years old."
except TypeError:
    print("Type Error")

