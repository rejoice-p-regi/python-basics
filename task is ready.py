x="orange"
print(x)
print(type(x))
print(len(x))
print(x[2])
for i in x:
    print(i)
y=" python, is, a, interpt "
print(y)
print("interpt" in y)
print("remo" not in y)
print(y[2:5])
print(y[:2])
print(y[5])
print(y[-5])
print(y[-6:-2])
print(y.upper())
print(y.lower())
print(y.strip())
print(y.replace("p","m"))
print(y.split(","))
print(x+y)
print(x+" "+y)
price=50
text="the orange has {} rs in market"
print(text.format(price))
x="i love orange and orange is very sweet"
print(x.count("orange"))