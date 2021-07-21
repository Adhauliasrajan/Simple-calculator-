x=float(input("Enter number 1="))
y=float(input("Enter number 2="))
ans=0
ch=input("Enter sign of any operators=")
if ch=='+':
    ans=x+y
elif ch=='-':
    ans=x-y
elif ch=='*':
    ans=x*y
elif ch=='/':
    ans=x/y
else:
     print("Enter valid operator")
print("Result=",ans)     
