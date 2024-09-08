#Simple Caalculator Design
input1=int(input("Enter The value="))
input2=int(input("Enter The value="))
result=0
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
choice=int(input("Enter your Choice:"))
if choice==1:
    result=input1+input2
elif choice==2:
    result=input1-input2
elif choice==3:
    result=input1*input2
elif choice==4:
    result=input1/input2
else:
    print("Enter correct choice")
print(result)
