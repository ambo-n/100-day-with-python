def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

number_1 =6
number_2=8

print(operation["+"](number_1, number_2))