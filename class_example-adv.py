class Cars():
    def __init__(self):
        self.cars = []
        
    def add_car(self, make, model, year):
        self.cars.append({
            "make": make,
            "model": model,
            "year": year
        })
        
    def get_car(self, make):
        for car in self.cars:
            if car["make"] == make:
                return f"{car['make']} ({car['year']}) - {car['make']} {car['model']}"

    def get_car_feature(self, make, feature):
        for car in self.cars:
            if car["make"] == make:
                return f"{feature}: {car.get(feature)}"

    def list_cars(self):
        i=0
        for car in self.cars:
            i = i + 1
            print(f"{str(i)}) {car['make']} {car['model']} ({car['year']})")
        
        
car = Cars()

while True:
    car_input = input("\nNy bil (skriv märke, modell och år separerat med kommatecken): ")
    make, model, year = car_input.split(",")
   
    car.add_car(make, model, year)
    
    car.list_cars()
    
