x="yellow"
print(x)
print(type(x))
print(len(x))
print(x[3])
for i in x:
    print(i)
y="   python, is a, object, oriented, programing, language    "
print(y)
print("language" in y)
print("rahul" not in y)
print(y[2:5])
print(y[:3])
print(y[-5])
print(y[-5:-3])
print(y.upper())
print(y.lower())
print(y.strip())
print(y.replace("p","z"))
print(y.split(","))
print(x+y)
print(x+"    "+y)
day=7
text="ramesh works {} days in a week"
print(text.format(day))
x="messi is a great footballer and messi is a nice person"
print(x.count("messi"))