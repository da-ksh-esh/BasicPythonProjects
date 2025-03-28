import math

def add(a,b):
    addition = a + b
    return addition

def sub(a,b):
    subtraction = a - b
    return subtraction

def multi(a,b):
    multiplication = a * b
    return multiplication

def div(a,b):
    try:
        division = a / b
        return division
    except ZeroDivisionError:
        ans1 = 'Division by zero is not possible'
        return ans1

def sqrt(a):
    sqrt = math.sqrt(a)
    return sqrt

print('''=======WELCOME TO CALCULATOR=======
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Sqaure Root ''')

while True:

    userInput = int(input('Select from [1, 2, 3, 4, 5]: '))

    if userInput == 1:
        a = float(input('Enter First Number: '))
        b = float(input('Enter Second Number: '))
        ans = add(a,b)
        print(ans)
    elif userInput == 2:
        a = float(input('Enter First Number: '))
        b = float(input('Enter Second Number: '))
        ans = sub(a,b)
        print(ans)
    elif userInput == 3:
        a = float(input('Enter First Number: '))
        b = float(input('Enter Second Number: '))
        ans = multi(a,b)
        print(ans)
    elif userInput == 4:
        a = float(input('Enter First Number: '))
        b = float(input('Enter Second Number: '))
        ans = div(a,b)
        print(ans)
    elif userInput == 5:
        a = float(input('Enter a Number: '))
        ans = sqrt(a)
        print(ans)

    x = input("If you want to continue enter 'Y' else press ENTER: ")
    if x.lower() == 'y':
        continue
    else:
        break
