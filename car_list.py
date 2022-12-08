import os
from Cars import MyCars
from bcolors import bcolors

car = MyCars()

data = car.load_from_file("cars.json")
car.cars = data
os.system('cls')


print(bcolors.YELLOW + """
FAVORITBILAR ---------------------------------------------------
- Lägg till bil genom att skriva märke och modell med mellanslag
- Ta bort genom att skriva respektive nummer.
- Avsluta genom att skriva "/q"
----------------------------------------------------------------""" + bcolors.DEFAULT)
car.list_cars()

while True:
    print(bcolors.YELLOW + "-" * 64)
    entry = input(bcolors.CYAN + "Lägg till bil (märke & modell): " + bcolors.DEFAULT)

    if entry.upper() == "/Q": 
        car.save_to_file("cars.json")
        print(bcolors.DEFAULT)
        exit()
    
    if entry.isdigit():
        car.remove_car(int(entry)-1)
    else:
        try:
            make, model = entry.split(" ",1)
            car.add_car(make, model)

        except ValueError:
            print(bcolors.RED + "Felaktig inmatning - försök igen.")
            continue
        
    os.system('cls')

    print(bcolors.DEFAULT)
    car.list_cars()
    
    