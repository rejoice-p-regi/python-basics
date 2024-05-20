colour={"name":"rejoice","age":24,"job":"data analyst"}
print(colour)
print(type(colour))
print(len(colour))
colour=dict(name="rejoice",age=24,job="data analyst")
print(colour)
print(colour["age"])
print(colour.get("name"))
print(colour.keys())
print(colour.values())
print(colour.items())
print("name" in colour)
print("height" not in colour)
colour["name"]="raj"
print(colour)
colour.update({"name":"akhil"})
print(colour)
colour.update({"height": 170})
print(colour)
colour["weight"]=70
print(colour)
colour.pop("name")
print(colour)
colour.popitem()
print(colour)
del colour["age"]
print(colour)
# colour.clear()
# print(colour)
# del colour
# for i in colour:
#     print(i)
for i in colour:
    print(i)
for i in colour:
    print(colour[i])
for i in colour.keys():
    print(i)
for i in colour.values():
    print(i)
for i in colour.items():
    print(i)
y=colour.copy()
print(y)
y=dict(colour)
print(y)
family={"child1":{"name":"rahul","age":23},"child2":{"name":"christin","age":23},"child3":{"name":"anaga","age":22}}
print(family)
print(family["child3"]["name"])
print(family["child2"]["age"])