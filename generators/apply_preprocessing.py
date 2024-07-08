from generator import list_of_dictionaries
import random

for i in list_of_dictionaries:
    if i["numEmps"] == "":
        i["numEmps"] = str(random.choice([0,1]))
    else:
        pass

with open("new_preprocessed_data.txt","w") as f:
    for i in list_of_dictionaries:
        string_formation = i["permalink"] +" "+i["company"]+" "+i["numEmps"]+" "+i["category"]+" "+i["city"]+" "+i["state"]+" "+i["fundedDate"]+" "+i["raisedAmt"]+" "+i["raisedCurrency"]+" "+i["round"]+"\n"
        f.writelines(string_formation)