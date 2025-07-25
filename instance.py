# # class student:
# #     def method(self,name,id):
# #         self.name=name
# #         self.id=id
# #         print(name,id)
# # obj=student()
# # obj.method("priya",2)

# # class student1:
# #     def method(self,name,id,phoneno):
# #         self.name=name
# #         self.id=id
# #         self.phoneno=phoneno
# #         print(self.name,self.id,self.phoneno)
# # obj=student1()
# # obj.method("priya",2,3333333333)

# class student:
#     def __init__(self):
#         self.name1="priya"
#         self.name2="aaksh"
#         # self.name1="sriya"
#         # self.name2="milky"
        
#     # def method(self):
#     #     self.name1="sriya"
#     #     self.name2="milky"
#     def details(self):
#         print(self.name1)
#         print(self.name2)
          
# obj=student()
# # obj.method()
# obj.details()
# del obj.name2
# print(obj.name2)

class parent:
    def par1(self,name,age):
        self.name=name
        self.age=age
class parent1(parent):
    def par2(self,address):
        self.address=address
class child(parent1):
    def chi(self,name,age,address,childname):
        self.par1(name, age)     
        self.par2(address) 
        print(self.name,self.age,self.address)
        print(childname)
obj=child()
obj.chi("supriya",23,"ap","akansha")
        