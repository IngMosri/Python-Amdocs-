from petro_car import Car
class ElectricCar(Car):


    def __init__(self, make, model, year):
#"""Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
