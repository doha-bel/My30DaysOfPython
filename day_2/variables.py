# day 2 yay
import math
first_name = "Doha"
last_name = "Belkheir"
full_name = first_name + last_name
country = "Algeria"
city = "Oran"
age = 120
year = 2025
is_married = False
is_true = True
is_light_on = False
fav_game, charachter_name, hours_played = "zelda botw","link",200

print(type(first_name))
print(type(charachter_name))
print(type(is_married))
print(type(age))

print(len(first_name))
print(len(charachter_name))

num_one = 5
num_two = 4 
total = num_one + num_two
exp = num_two ** num_one
print(total,exp)
radius = int(input("your radius is : "))
area = int(math.pi * radius**2)
circumfrance =int( math.pi * 2 * radius)
print(f"area = {area}m^2 and circumfrance = {circumfrance}m")
