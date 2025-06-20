a=int(input("enter first number"))
b=int(input("enter second number"))
print("1:addition, 2:substration, 3:multiplication, 4:division")      
choice = int(input("enter a number"))      
if(choice == 1):
    print(a+b)
if(choice == 2):
    print(a-b)
if(choice == 3):
    print(a*b)
if(choice == 4):
    print(a/b)
else:
    print("invalid choice")