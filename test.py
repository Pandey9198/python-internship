# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except:
#     print("Invalid input")
# else:
#     print("Execution successful")
# finally:
#     print("Program ended")
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello!")
    
greet()
