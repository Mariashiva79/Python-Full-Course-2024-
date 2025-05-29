# Static methods estos metodos no necesitan tener acceso a los datos de la clase

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        print(f"{self.name} = {self.position}")

    @staticmethod
    def is_valid_position(position):
         valid_positions = ["Manager", "Cook", "Administrative", "Cashier"]
         return position in valid_positions

employee1 = Employee("Mery", "Manager")
employee2 = Employee("Jhon", "Cashier")
employee3 = Employee("Ross", "Janitor")
employee4 = Employee("Janice", "Administrative")

employee1.get_info()
employee2.get_info()
employee3.get_info()
employee4.get_info()

print(Employee.is_valid_position("Rocket"))