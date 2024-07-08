## generators,coroutines and pipelines concept implementation
load_file = r"C:\Users\saitr\OneDrive\Documents\GitHub\python-advanced-concepts\generators\techcrunch.csv"

generator_object_to_read_each_line = (line for line in open(load_file))
list_of_generator_object_line = (line.rstrip().split(",") for line in generator_object_to_read_each_line)

#colum values for the top of the table
values_list = next(list_of_generator_object_line)

#creation of list of dictionaries and empty dictionaries to fill up
list_of_dictionaries = []
empty_dictionaries = {}

#column value extracted from the generators for the bottom values
for i in list_of_generator_object_line:
    empty_dictionaries = {}
    colmns_values = i
    for i in range(10):
        empty_dictionaries[values_list[i]] = colmns_values[i]
    list_of_dictionaries.append(empty_dictionaries)

#create a new txtfile import all this data line by line
with open("newtxt.txt","w") as file: # type: ignore
    for i in list_of_dictionaries:
         string_formation = i["permalink"] +" "+i["company"]+" "+i["numEmps"]+" "+i["category"]+" "+i["city"]+" "+i["state"]+" "+i["fundedDate"]+" "+i["raisedAmt"]+" "+i["raisedCurrency"]+" "+i["round"]+"\n"
         file.writelines(string_formation)
            
        