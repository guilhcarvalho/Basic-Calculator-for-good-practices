'''
My goal here is to build a basic calculator for my learning
'''

#Calculator operations functions:
def plus(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#Building an input operation
operation = input(f'Select an operator: "+"  "-"  "*" "/" -->   ')

operation_list = ['+', '-', '*', '/']
if operation not in operation_list:
    print('invalid operator')
    exit()

# X and Y values input:
x = float(input('Input a value:  '))
y = float(input('Input a value:  '))

#Conditions for operations:
if operation == '+':
    result = plus(x, y)

elif operation == '-':
    result = sub(x, y)

elif operation == '*':
    result = multiply(x, y)
    
elif operation == '/':
    if y != 0:
        result = divide(x, y)
    else:
        print(f'ERROR, Division by 0')
        exit()
        
#Print of result
print(f'Result of this operation is {result}.')
