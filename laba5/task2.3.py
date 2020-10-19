class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Dolphin(Animal):
    def get_name_age(self):
        return print("I'm a dolphin %s and I'm %s years old" % (self.name,self.age))


class Zebra(Animal):
    def get_name_age(self):
        return print("I'm a zebra %s and I'm %s years old " % (self.name,self.age))




