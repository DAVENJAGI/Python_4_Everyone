class Vehicle: #class
    color = "white"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passangers"
    
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)
    
    def fare(self):
        amount = super().fare()
        amount += 10/100 * amount
        return amount
    
class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12, 50)
#Personal_car = Car("Audi Q5", 240, 18)
#print("Color: ", School_bus.color, "Vehicle name: ", School_bus.name, "Speed: ", School_bus.max_speed, "Mileage: ", School_bus.mileage)
#print("Color: ", Personal_car.color, "Vehicle name: ", Personal_car.name, "Speed: ", Personal_car.max_speed, "Mileage: ", Personal_car.mileage)
#print("Total Bus fare is: ", School_bus.fare())
print(type(School_bus))
print(isinstance(School_bus, Vehicle))