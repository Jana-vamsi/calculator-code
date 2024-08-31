
print("select an operation to perform :")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

operation = input()

if operation=="1":
    num1=input("enter the first number : ")
    num2=input("enterthe second number : ")
    print("sum is = "+ str(int(num1)+int(num2)))
elif operation =="2":
    num1=input("enter the first number : ")
    num2=input("enterthe second number : ")
    print("sum is = "+ str(int(num1)-int(num2)))
elif operation =="3":
    num1=input("enter the first number : ")
    num2=input("enterthe second number : ")
    print("sum is = "+ str(int(num1)*int(num2)))
elif operation =="4":
    num1=input("enter the first number : ")
    num2=input("enterthe second number : ")
    print("sum is = "+ str(int(num1)/int(num2)))
else:
    print("THE NUMBER IS INVALID NUMBER : ")
    print("PLEASE ENTER THE ABOVE NUMBERS : ")