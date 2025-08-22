"""
a dictionary is a collection of unordered, modifiable (mutable),
paired (key:value) data type <3
"""
# creating a dict :
my_dict = {}
# or 
dicty = dict()

my_dict = {"name" : "doha",
           "age" : 19,
           "gendre": "female"
           }
print(f"my name is {my_dict["name"]}")
# if the key doesnt exist, you get a key name error (tried it), you have to use the get methode to check if the key exists, if it doesnt it return None
print(f"my age is {my_dict.get("ages")}")

# adding an item 
my_dict["height"] = 164
print(my_dict.get("height"))
my_dict["age"] = 20
print(f"my age is {my_dict.get("age")}")
print(f"do i have a name? {"name" in my_dict}")
my_dict.pop("age")
my_dict.popitem() # removes the last item

print(my_dict)

# dict => list of items (basically a dictionary to a list of tuples.)
print(my_dict.items())
# you can copy a dictionary 
copyme = my_dict.copy()
del my_dict
print(copyme)

# getting the keys as a list
keys = copyme.keys()
print(keys) 
k1 ,k2 = copyme.keys()
print(k1,k2)
#getting the values as a list 
values = copyme.values()
print(values)
c1 ,c2 = copyme.values()
print(c1,c2)
#HE SAID : Now, you are super charged with the power of dictionaries!!!!


#### EXEERCIIIICES #####
dog = {}
dog["name"],dog["color"],dog["age"] = "otto" , "brown" , 3
print(dog)

hero = {
    "first_name" : "link",
    "last_name" : "???",
    "gender" : "male",
    "martial_status" : "no",
    "skills" : ["collecting korok seeds", "cooking", "making fire","sword fight", "climbing"],
    "country" : "Hyrule"
}

print(len(hero))
print(hero.get('skills'),type(hero.get('skills')))
hero["skills"].append(["rizz","archery"])
print(hero.values())

print(hero.keys())
print(hero.items())
del hero["skills"]
del dog
print(hero)