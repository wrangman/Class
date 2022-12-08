import json

class MyCars():
    def __init__(self):
        self.cars = []

    def list_cars(self):
        print("LISTA:")
        for i, car in enumerate(self.cars):
            print(f"{i+1}. {car['make']} {car['model']}")
              
    def add_car(self, make, model):
        self.cars.append({ "make": make, "model": model })
        
    def remove_car(self, index):
        del self.cars[index]
        
    def save_to_file(self, filename):
        cars_json = json.dumps(self.cars)

        f = open(filename, "w")
        f.write(cars_json)

        # Close the file
        f.close()
        
    def load_from_file(self, file_path):
        # Loads the cars from a JSON file
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
        
    