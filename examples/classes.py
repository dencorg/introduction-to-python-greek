# δημιουργία κλάσης
class Vehicle:
    def __init__(self, number_of_wheels, fuel_type, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = fuel_type
        self.maximum_velocity = maximum_velocity

    def make_noise(self):
        print('VRUUUUUUUM')


tesla = Vehicle(4, 'electric', 250)
print(tesla.number_of_wheels)

class Vehicle:
    def __init__(self, number_of_wheels, fuel_type, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = fuel_type
        self.maximum_velocity = maximum_velocity

    def get_number_of_wheels(self):
        return self.number_of_wheels

    def set_number_of_wheels(self, number):
        self.number_of_wheels = number

bmw = Vehicle(4, 'petrol', 200)
bmw.set_number_of_wheels(2)
print(bmw.number_of_wheels)