# # Python Functions
# Topics:
# 1. Defining and calling functions
# 2. Arguments and return values
# 3. Default arguments
# 4. Keyword arguments
# 5. Lambda functions


# 1. Defining and Calling a Function

def greet():
    print("Hello, Welcome to Python!")


greet()


# 2. Arguments and Return Values

def add(a, b):
    return a + b


result = add(10, 20)
print("Sum:", result)


# 3. Default Arguments

def greet_user(name="Student"):
    print("Hello", name)


greet_user()
greet_user("Prince")


# 4. Keyword Arguments

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student(name="Prince", age=20, course="BCA")


# 5. Lambda Function

square = lambda x: x * x

print("Square:", square(5))


# Lambda with two arguments

multiply = lambda a, b: a * b

print("Multiplication:", multiply(4, 5))