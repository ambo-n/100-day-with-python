def calculator(first_number, second_number, operator):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number/second_number
    else:
        return print("Invalid operation")

def choosing_operator():
    for operator_sign in ["+","-","*","/"]:
        print(operator_sign)
    operator_choice = input("Pick an operation: ")
    return operator_choice

print("Welcome to my calculator!")
should_continue = True

while should_continue:
    first_number = float(input("What's the first number?: "))
    operator = choosing_operator()
    second_number = float(input("What's the next number?: "))
    finish_calculating = False
    while not finish_calculating:
        result= calculator(first_number, second_number, operator)
        print(f"{first_number} {operator} {second_number} = {result}")
        new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation/to exit: ").lower()
        if new_calculation == 'y':
            first_number = result
            second_number = float(input("What's the next number?: "))
            operator = choosing_operator()
        else:
            finish_calculating = True
    continue_calculating = input("Type 'y' to continue using the calculator or 'e' to exit: ")
    if continue_calculating == 'e':
        should_continue= False
        print("Goodbye")

