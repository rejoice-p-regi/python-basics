a=int(input("enter a value"))
b=int(input("enter a second value"))
z=input("select a operator")
if z=="+":
    sum=a+b
    print(sum)
elif z=="-":
    dif=a-b
    print(dif)
elif z=="*":
    mult=a*b
    print(mult)
elif z=="/":
    div=a/b
    print(div)
else:
    print("invalid operator")