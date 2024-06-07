from oop.Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, company, owner, color, speed, matricule):
        super().__init__(company, owner, color, speed)
        self.matricule = matricule
    def get_info(self):
        return f"{self.company} {self._get_owner()} {self.color} {self.speed} {self.matricule}"


car1 = Car('jeep','rayen','black', 1000,5748219)
print(car1.get_info())
car1.set_owner("rayen123")
print(car1.get_info())
