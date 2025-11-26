def userInput():
    first_input=int(input("Enter the First Number :"))
    second_input=int(input("Enter the second Number :"))
    return first_input,second_input


def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def mult(a=0,b=0):
    return a*b

print("Welcome to Cal")
while True:
    print("select the choose :\n 1:add \n 2:sub \n 3:mult \n: 4:stop")
    choose=int(input("Enter the choose :"))

    if choose==1:
        x,y=userInput()
        print(f"Addition of two Number :{add(x,y)}")

    elif choose==2:
        x,y=userInput()
        sub(x,y)
        print(f"Subtraction of two Number :{sub(x, y)}")

    elif choose==3:
        x,y=userInput()
        mult(x,y)
        print(f"Multiplication of two Number :{mult(x, y)}")

    elif choose==4:
        print("Thank you for using calculator")
        break
