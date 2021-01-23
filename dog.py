class Dog:
    def __init__(self, name, age, weight, length=5):
        """initialize the profile/attribute """
        self.name = name
        self.age = age
        self.weight = weight
        self.length = length

    def sit(self):
        print(f"one {self.age} years old and {self.length}m long dog named {self.name:<8} is sitting now")


class Cat:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
