class Calculator:
    def __init__(self, version: int):
        self.version = version

    #instance method
    def description(self):
        print(f'Currently running calculator in version: {self.version}')

    @staticmethod
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)

class Animals:
    #class attribute/variable-- the variable is defined outside the method and inside the class
    home = "Zoo"

    #creating instance attributes
    def __init__(self, name: str , age: int):
        self.name = name
        self.age = age

    #creating a class method
    @classmethod
    def animals_home(cls, home: str):
        cls.home = home


if __name__ == '__main__':

    calc1 = Calculator(10)
    calc2 = Calculator(200)

    calc1.description()
    calc2.description()

    res = Calculator.add_numbers(20.5, 44, 55.5)
    print(f"The sum is {res}")

    #creating animal instance
    animal1 = Animals("Lion", 25)
    print(f'The orginal animal home is {animal1.home}')

    #changing class attribute using class method
    Animals.animals_home("Jungle")
    print(f'The new animal home is the {animal1.home}')
