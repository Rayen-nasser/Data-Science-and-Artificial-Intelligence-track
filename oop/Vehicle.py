class Vehicle:
    def __init__(self, company, owner, color, speed):
        self.company = company
        self.__owner = owner
        self.color = color
        self.speed = speed

    def set_owner(self, owner):
        self.__owner =owner

    def _get_owner(self):
        return self.__owner

    def get_info(self):
        return f"{self.company} {self.color} {self.speed}"