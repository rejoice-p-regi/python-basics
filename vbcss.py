class colour:
    x=10
# y=colour()
# print(y.x)

# class person:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
# # k=person("name","age")
# # print(k.name,k.age)
# k=person("rejoice","24")
# print(k.name,k.age)
# class flower:
#     pass

# inheritence
class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def human(self):
        print(self.name)
        print(self.age)
class student(person):
    pass
y=student("rejo",12)
y.human()
