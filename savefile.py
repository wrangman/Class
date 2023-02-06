import json


def save_to_file(filename):                       # Saves to JSON
    with open(filename, 'w') as f:
            json_string = json.dumps(save_this)
            f.write(json_string)
        
def load_from_file(filename):                     # Loads the cars from a JSON file
        try:
            with open(filename, "r") as file:
                return json.load(file)
                
        except FileNotFoundError:               # if File not found return False.
            return False
        
        

loaded_text = load_from_file("test.json")       # loads previous inputs
print(loaded_text)

save_this = input("Spara detta: ")              # input something to save...

save_to_file("test.json")                       # saves what you wrote


