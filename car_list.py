import os
import time
from Cars import MyCars
from bcolors import bcolors

car = MyCars()

load_stored_cars = car.load_from_file("cars.json")

if load_stored_cars:                                #If there are stored cars add them
    car.cars = load_stored_cars    
    
os.system('cls')

print(bcolors.YELLOW + """
FAVORITBILAR ---------------------------------------------------
- Lägg till bil genom att skriva märke och modell med mellanslag
- Ta bort genom att skriva respektive nummer
- Spara & avsluta genom att skriva "/q"
----------------------------------------------------------------""" + bcolors.CYAN)

if len(car.cars) > 0: 
    car.list_cars() 
else: 
    print(bcolors.CYAN + "(Inga sparade bilar hittades)")

while True:
    print(bcolors.YELLOW + "-" * 64)
    entry = input(bcolors.DEFAULT + "Lägg till bil (märke & modell): " + bcolors.CYAN)

    if entry.upper() == "/Q": 
        print(bcolors.DEFAULT + "Sparar din billista...")
        time.sleep(1)
        car.save_to_file("cars.json")
        exit()
    
    if entry.isdigit():
        total_cars = len(car.cars)
        
        if int(entry) >= 1 and int(entry) < total_cars + 1:
            car.remove_car(int(entry)-1)
        
        else:
            print(bcolors.RED + f"Bilen finns inte - skriv ett nummer mellan 1 och {total_cars}")
            time.sleep(1)
    
    else:
        if not " " in entry:
            print(bcolors.RED + "Felaktig inmatning - skriv märke & modell")
            time.sleep(1)
    
        else:                                           # add new car                                   
            make, model = entry.split(" ",1)
            car.add_car(make, model)
        
    os.system('cls')

    print(bcolors.CYAN)
    car.list_cars()
    
    