x="yellow"
print(type(x))
print(len(x))
print(x[-1])
for i in x:
    print(i)
y="Hi, iam, ready, for ,the, test"
print(y)
print(x[:2])
print(x[2:])
print(x[2:4])
print("language" in y)
print("hi" not in y)
print(y.upper())
print(y.lower())
print(y.strip())
print(y.replace("f","t"))
print(y.split(","))
print(x+y)
print(x+" "+y)
age=24
sentence="the distance between the two places are {} km"
print(sentence.format(age))
k="hi there is a cake cake on the table"
print(k.count("cake"))