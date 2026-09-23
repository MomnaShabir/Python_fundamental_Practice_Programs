while True:
    print("\nWelcome to Calculator")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply") 
    print("4.Divide")
    print("5.Exit")
    choice=input("Enter your choice(1-5):")
    
    if choice =="1":
        num1=int(input("Enter firsr number:"))
        num2=int(input("Enter second number"))
        print("Result:",num1+num2)
    elif choice =="2":
        num1=int(input("Enter firsr number:"))
        num2=int(input("Enter second number:"))
        print("Result:",num1-num2)
    elif choice =="3":
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        print("Result:",num1*num2)
    elif choice =="4":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if num2 !=0:
            print("Result:",num1/num2)
        else:
            print("Cannot divide by zero!")
    elif choice =="5":
        print("Exiting Calculator.Goodbye!")
        break
