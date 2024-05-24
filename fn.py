def hello():
    print("rejoice")
hello()
def what(*x):
    print(x[2])
what(1,2,3,4,5)
def itsme(a,b,c):
    print(b)
itsme(a=1,b=2,c=3)
def why(**x):
    print(x["a"])
why(b=1,c=2,v=3,a=8)
def mycountry(country="india"):
    print(country)
mycountry("korea")
mycountry("iran")
mycountry()
def hell(x):
    return 10+x
print(hell(1))
def rejo(x,y):
    return x+y
print(rejo(1,2))
def raj(x):
    pass
x=lambda a:a+10
print(x(2))
x=lambda q,w,e:q+w+e
print(x(10,20,30))