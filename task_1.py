
def calculator():

    result = float(input("Enter first number: "))

    while True:

        op = input("Enter operator (+, -, *, /) or exit: ")

        if op.lower() == "exit":
            break

        if op not in ["+", "-", "*", "/"]:
            print("Invalid operator")
            continue

        num = float(input("Enter next number: "))

        if op == "+":
            result += num

        elif op == "-":
            result -= num

        elif op == "*":
            result *= num

        elif op == "/":
            if num == 0:
                print("Cannot divide by zero")
                continue
            result /= num

        print("Current Result:", result)

    print("Final Result:", result)


calculator()

