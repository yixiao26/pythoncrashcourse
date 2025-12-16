from car import Car
from electric_car import ElectricCar

my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())