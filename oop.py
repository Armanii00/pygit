class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = student()
student1.name = "arman"
student.marks = 84

did_pass = student1.check_pass_fail()
print(did_pass)
print(student1.name)


student2 = student()
student2.name = "karim"
student2.marks = 30
did_pass = student2.check_pass_fail()
print(did_pass)



class person:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

person1 = person("armanii", 85)
person2 = person("karim", 30)
did_pass = person1.check_pass_fail()
print(did_pass)
did_pass = person2.chck_pass_fail()
print(did_pass)