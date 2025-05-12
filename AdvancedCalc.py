def add(*args): #Do some addition yeah bruv
    return sum(args)

def subtract(*args): # Subtract n stuff
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args): #Multiply and stuff
    result = 1
    for num in args:
        result *= num
    return result

def devide(*args):
    if not args:
        return "No numbers"
    result = args[0]
    try:
        for num in args[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error!"

def modulus(x, y):
    if y == 0:
        return "Error!"
    return x % y

def floor_devide(x,y):
    if y == 0:
        return "Error!"
    return x // y

def power(x,y):
    if x < 0 or y < 0:
        return "Error!"
    return x ** y

def intro():
    return print ("Simple Calculator \n Select Mode: \n+. Addition \n-. Subtraction \n*. Multiply \n/. Division \n%. Modulus \n//. Floor Devide \n**. Power")

intro()

choice = input("Enter Choice (+,-,*,/,%,//,**): ")

if choice in ['+','-','*','/']:
    numbers = input ("Enter numbers seporated by space: ")
    nums = list(map(float, numbers.split()))
    if choice == '+':
        print("Answer:", add(*nums))
    elif choice == '-':
        print("Answer:", subtract(*nums))
    elif choice == '*':
        print("Answer:", multiply(*nums))
    elif choice == '-':
        print("Answer:", devide(*nums))
else:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '%':
        print("Answer:", modulus(x,y))
    elif choice == '//':
        print("Answer:", floor_devide(x,y))
    elif choice == '**':
        print("Answer:", power(x,y))