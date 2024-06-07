class Student:
    university = "iset gafsa"
    def __init__(self, id, name, age, grades):
        self.__name = name
        self.age = age
        self.id = id
        self.grades = grades
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


std1 = Student('1jdg52', "rayen",21,'2dsi')
std1.__name = "rayen nasser"

print(std1.get_name())



