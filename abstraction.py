
class person:
    def __init__(self,person_name: str,date_of_birth: int,ht_inches: int ):
        self.__name = person_name
        self.__date_of_birth = date_of_birth
        self.__height = ht_inches


    def get_name(self):
        return self.__neme


    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("sorry this person name can't found")
            return
        self.name = new_name


    def get_summary(self):
        return f"name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height}"

    def get_date_of_birth(self):
        return self.__date_of_birth

    def __has_any_number(self, string):
        return "0" in string


a_person = person("arman", "2001","5 feet")
print(a_person.get_summary())
a_person.set_name("abdullah al arman")
print(a_person.get_summary())

"""
person_list = [person("abdullah", 2000,72),
               person("juman",2000, 71),
               person("arman", 2001, 72),
               person("armanii", 2001)]
for person in person_list:
    if person.get_date_of_birth() is not None and person.get_date_of_birth >= 2001:
        print(person.get_summary())

"""


class student(person):
    def __init__(self, person_name: str,date_of_birth: int, email_id: str, student_id: str):
        super().__init__(person_name,date_of_birth)
        self.id = student_id
        self.email = email_id
    def get_summary(self):
        return f"Name: {self.get_name()} Email: {self.email}"
student = student("aa", 2000,"abdullahalarman00.com")
print(student.get_summary())
student.set_name("armannn")
print(student.get_summary())