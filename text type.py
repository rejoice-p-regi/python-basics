x="apple"
print(x)
print(type(x))
print(len(x))
print(x[1])
for i in x:
    print(i)
y=" python, is, a programing, language "
print(y)
print("language" in y)
print("rejoice" not in y)
print(y[2:5])
print(y[:5])
print(y[:2])
print(y[-1])
print(y[-5:-2])
print(y.upper())
print(y.lower())
print(y.strip())
print(y.replace("p","h"))
print(y.split(","))
print(x+y)
print(x+" "+y)
age=30
text="my name is john and iam {}"
print(text.format(age))
x=20
y=100
text="i have {} apples and the amount is {} for each"
print(text.format(x,y))
x="i love apple and apple is a fruit"
print(x.count("apple"))