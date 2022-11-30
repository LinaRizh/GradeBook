import json 

def imp (d):
    with open("database.json", "w") as write_file:
        json.dump(d,write_file)
