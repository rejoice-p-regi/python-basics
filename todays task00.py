identity={"name":"akhil","age":25,"job":"ui desiner"}
print(identity)
print(type(identity))
print(len(identity))
identity=dict(name="akhil",age=25,job="ui desiner")
print(identity)
print(identity["age"])
print(identity.get("name"))
print(identity.keys())
print(identity.values())
print(identity.items())
print("height" in identity)
print("name" not in identity)
identity["name"]="rahul"
print(identity)
identity.update({"name":"mahesh"})
print(identity)
identity.update({"hobby":"dancing"})
print(identity)
identity["weight"]=80
print(identity)
identity.pop("name")
print(identity)
identity.popitem()
print(identity)
del identity["age"]
print(identity)
# identity.clear()
# print(identity)
# del identity
# for i in identity:
#     print(i)
for i in identity:
    print(i)
for i in identity:
    print(identity[i])
for i in identity.keys():
    print(i)
for i in identity.values():
    print(i)
for i in identity.items():
    print(i)
y=identity.copy()
print(y)
y=dict(identity)
print(y)
family={"child1":{"name":"akhil","age":21},"child2":{"name":"angel","age":23},"child3":{"name":"amal","age":22}}
print(family)
print(family["child3"]["name"])
print(family["child2"]["age"])