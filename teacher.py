class Teacher:
    class Classroom:
        def __init__(self, cname):
            self.cname = cname

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.classroom = None

    def assign(self, cname):
        self.classroom = Teacher.Classroom(cname)

    def show(self):
        print(self.name, self.subject, self.classroom.cname)
t = Teacher("Sriyha", "Math")
t.assign("9A")
t.show()