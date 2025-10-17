x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
op=input("Enter the operation you want to perform:")
if op == "+":
     print ("Your addition is", x+y)
elif  op == "-":
     print ("Your subtraction is", x-y)
elif op == "*":
     print ("Your multiplication is", x*y)
elif op == "/":
     print ("Your division is", x/y)
else:
         print ("Enter valid command")