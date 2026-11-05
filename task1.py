#Task 1 :Build a Calculator CLI App.
numbers = []

# Getting numbers from user
while True:
    num = int(input("Enter a number: "))
    numbers.append(num)

    choice = input("Do you want to enter another number? (yes/no): ")

    if choice.lower() == "n":
        break

# Getting operator
op = input("Enter operator (+, -, *, /): ")


# Functions
def addition():
    result = 0
    for num in numbers:
        result += num
    return result


def subtraction():
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiplication():
    result = 1
    for num in numbers:
        result *= num
    return result


def division():
    result = numbers[0]

    for num in numbers[1:]:
        if num == 0:
            return "Cannot divide by zero"
        result /= num

    return result

#operation
if op == "+":
    print("Result:", addition())

elif op == "-":
    print("Result:", subtraction())

elif op == "*":
    print("Result:", multiplication())

elif op == "/":
    print("Result:", division())

else:
    print("Invalid operator")



