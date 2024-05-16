colour=["yellow","red","white","black","green","rose"]
print(colour)
print(len(colour))
print(type(colour))
x=[2,4,6,8,10]
print(colour[3])
print(colour[-2])
print(colour[:4])
print(colour[3:])
print(colour[-4])
print(colour[-5:-3])
print("blue" in colour)
print("yellow" not in colour)
colour[3]="orange"
print(colour)
colour[2:4]=["blue","purple"]
print(colour)
x.append(1)
print(x)
x.insert(0,1)
print(x)
colour.extend(x)
print(colour)
colour.remove(2)
print(colour)
colour.pop(2)
print(colour)
colour.pop()
print(colour)
del colour[2]
# print(colour)
# colour.clear()
# print(colour)
# del colour
# print(colour)
for i in colour:
    print(i)
flower=["lotus","lilly","sunflower","rose","bluebell","hibuscus","daisy","orchid"]
print(flower)
flower.sort()
print(flower)
flower.sort(reverse=True)
print(flower)
y=colour.copy()
print(y)
z=list(flower)
print(z)
r=(flower+y)
print(r)
test=["a","b","c","d","e","f","g"]
age=[20,30,30,40,50,60,70]
for i in age:
    test.append(i)
print(test)
digits=age.count(30)
print(digits)