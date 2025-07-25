# class student:
#     @staticmethod
#     def method():
#         name=input("enter name")
#         id=int(input("id"))
#         print(name,id)
# student.method()

# class M:
#     @staticmethod
#     def method(a,b):
#         sum = a+b
#         print(sum)
# M.method(10,20)

class Teacher:
    def __init__(self, tname, tid, tsub):
        self.tname = tname
        self.tid = tid
        self.tsub = tsub
    class ClassRoom:
        def __init__(self, cname):
            self.cname = cname
    def assign_class(self, cname):
        self.classroom = Teacher.ClassRoom(cname)
    def show_details(self):
        print(self.tname, self.tid, self.tsub, self.classroom.cname)
obj = Teacher("Supriya", 1, "Maths")
obj.assign_class("C2")
obj.show_details()


