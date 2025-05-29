# class methods, para crear funciones que necesitan datos de la clase principal.

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        print(f"{self.name} {self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Raul", 6.05)
student2 = Student("Maria", 5.89)
student3 = Student("Carlos", 6.50)
student4 = Student("Ana", 5.95)
student5 = Student("Lucas", 6.20)


student1.get_info()
student2.get_info()
student3.get_info()
student4.get_info()
student5.get_info()

print()
print(Student.get_count())
print(Student.get_average_gpa())