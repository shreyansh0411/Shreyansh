# making a calculator 

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

choices = ("add","sub","mul","div")
choice = input("Enter your choice : ").lower()

if choice == "add":
       print(f"Addition of number is : {a+b}")
elif choice == "sub":
       print(f" Subtraction of number is : {a-b}")
elif choice == "mul":
       print(f"Multiplication of number is : {a*b}")
elif choice == "div":
        if b == 0:
            print("B cannot be 0 try again")
        else:
            print(f"Division of numbers is {a/b}")
else :
      print("Incorrect Choice")