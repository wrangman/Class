'''
CARS.PY: Bilklass

__author__  = "Johan Wrangö"
__version__ = "1.0.2"
__email__   = "johan.wrango@ntig.se"
'''

import json

class MyCars():
    def __init__(self):
        self.cars = []

    def list_cars(self):
        print("BILLISTA:")
        for i, car in enumerate(self.cars):
            print(f"{i+1}. {car['make']} {car['model']}")
              
    def add_car(self, make, model):
        self.cars.append({ "make": make, "model": model })
        
    def remove_car(self, index):
        del self.cars[index]
        
    def sort_cars(self):                                    # Sort the list of cars in place by make and model
        self.cars.sort(key=lambda car: (car["make"], car["model"]))
        
    def save_to_file(self, filename):                       # Saves to JSON
        with open(filename, 'w') as f:
            json_string = json.dumps(self.cars)
            f.write(json_string)
        
    def load_from_file(self, filename):                     # Loads the cars from a JSON file
        try:
            with open(filename, "r") as file:
                return json.load(file)
                
        except FileNotFoundError:
            return False
    