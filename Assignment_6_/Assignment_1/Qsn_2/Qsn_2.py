# Q2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
states ={"Kerala":"Thiruvanandhapuram","Tamil nadu":"Chennai","Maharashtra":"Mumbai","Goa":"Panaji","Karnataka":"Bangalore","Gujarat":"Gandhinagar","Sikkim":"Gangtok"}
file = open("capital.json","w+")
json.dump(states,file)
print(states)