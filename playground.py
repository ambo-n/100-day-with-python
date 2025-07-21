try:
    age = int(input("Enter your age: "))
    if age > 150:
        raise ValueError("Out of range")
except ValueError as wrong_type:
    print(wrong_type)
    print("Invalid number.")
else:
    print(f"You age is {age}")
