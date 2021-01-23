def test4class():
    """test for class"""
    class Dog:
        def __init__(self, name, age, weight, length=5):
            """initialize the profile/attribute """
            self.name = name
            self.age = age
            self.weight = weight
            self.length = length

        def sit(self):
            print(f"one {self.age} years old and {self.length}m long dog named {self.name:<8} is sitting now")

    harry = Dog('harry', 5, 40)
    harry.sit()
    other_dog = Dog('harness', 4, 20)
    other_dog.sit()

    class Battery:
        """toy dog's attribute"""
        def __init__(self, dog_model=None, size=7, model='teddy',):
            self.size = size
            self.model = model
            self.dog_model = dog_model

        def message_show(self):
            print(f"{self.dog_model}'s battery is size{self.size} and {self.model} model")

    class ToyDog(Dog):
        """子类的测试使用, 父类要位于子类前，且在同一文件中"""
        def __init__(self, name, age, weight, length,):
            super().__init__(name, age, weight, length,)
            self.dog_model = None
            self.battery = Battery()
            self.price = 0

        def price_show(self):
            print(f"{self.name}'s price is {self.price:.2f} and her length is {self.length}")

        def decision(self):
            deci = self.battery.size    # 把属性类中的数据传递到拥有类中
            if deci > 6:
                print('so big')
            elif deci == 6:
                print('appropriate')
            else:
                print('so small')

    lily = ToyDog('lily', 1, 6, 8)
    lily.price = 20
    lily.dog_model = 'iron'
    lily.price_show()
    lily.battery = Battery(lily.dog_model, 5, 'mark')   # 把类中的数据传递到属性类中
    lily.battery.message_show()
    lily.decision()


if __name__ == '__main__':
    test4class()
