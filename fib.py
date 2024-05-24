x=int(input("enter a number:"))
n1=0
n2=1
print("fabinocci series")
for z in range(0,x):
    if z<=1:
        n3=z
    else:
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3,end='')