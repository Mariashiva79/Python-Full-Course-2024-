# object = en una clase se crean atributos(variables) y metodos(funciones)
#          para un objeto, por ejemplo, teléfono, copa, libro
#          se necesita la "clase" para crear muchos objetos


class Dog:

    dog_list = []

    def __init__(self, name, age, size, is_adopt):
        self.name = name
        self.age = age
        self.size = size
        self.is_adopt = is_adopt
        Dog.dog_list.append(self)

    def wait(self):
        print(f"{self.name} with {self.age} years old, is wating for you!! {self.name} is a {self.size} friend!!")
    def adopt(self):
        print(f"{self.name} is in his new home!! with {self.age} years old, this {self.size} dog found happiness!!")

    def show_info(self):
        print(f"\n=== 🐕 INFO {self.name.upper()} 🐕 ===")
        print(f"Age: {self.age} years old")
        print(f"Size: {self.size}")
        print(f"Status: {'Adopt' if self.is_adopt else 'In adoption'}")
        print("------------------------")

    def in_adoption(self):

        if not self.is_adopt:
            print("\n=== 🐕 DOGS IN ADOPTION 🐕 ===")
            for dog in Dog.dog_list:
                if not dog.is_adopt:
                    print(f"Name: {self.name}")
                    print(f"Age: {self.age} years old")
                    print(f"Size: {self.size}")
                    print("------------------------")

