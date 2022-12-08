class Cars():
    def __init__(self):
        self.cars = []
        
    def add_car(self, name):
        self.cars.append(name)
        
    def list_cars(self):
        return self.cars
        
        
car = Cars()

while True:
    entry = input("Ny bil: ")
    car.add_car(entry)
    
    print(car.list_cars())