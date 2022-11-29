# Brief Crash Course for Dictionaries

my_dict = {}
my_thesaurus = {"great":["fantastic", "awesome"], "bad":["substandard", "poor", "inferior"], "medium":["average"]}

my_dict["great"] = ["fantastic", "awesome"]
#print(my_dict["bad"]) # Would cause an error!

my_dict["bad"] = ["substandard", "poor"]
my_dict["bad"] += ["inferior"]

my_dict["medium"] = ["average"]

print(my_dict == my_thesaurus) # True

if ("medium" in my_dict): # Yes
	print("Yes")

if ("brad" in my_dict): # No
	print("Nice try brad")

for key in my_dict.keys():
	print(key)
	print(my_dict[key])

for value in my_dict.values():
	print(value) # No way to get associated key

for k, v in my_dict.items():
	print(k, v)


