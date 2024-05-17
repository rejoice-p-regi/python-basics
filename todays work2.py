number={1,2,3,4,5,"six","seven"}
print(number)
print(type(number))
print(len(number))
number=set((1,2,3,4,5,"six","seven"))
print(number)
for i in number:
    print(i)
print("6" in number)
print("7" not in number)
number.add(6)
print(number)
colour={"red","blue","black"}
number.update(colour)
print(colour)
age=[2,12,13,15,18]
number.update(age)
print(number)
number.remove("seven")
print(number)
number.discard(10)
print(number)
number.discard(2)
print(number)
r=number.pop()
print(number)
print(r)
# number.clear()
# print(number)
# del number
t=number.union (colour)
print(t)
p={"dog","cat","tiger"}
v={1,3,"dog"}
l=p.intersection(v)
print(l)
k=p.difference(v)
print(k)