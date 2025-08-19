"""
tuple : ordered and unchangeable (immutable)

- when we want to slice a tuple (i1,i2,i3) tuple[0:2] the item at index 2 is not included!

(  i1  ,  i2  ,  i3  )
   0       1      2    # positive indexing
  -3      -2     -1    # negative indexing

"""

# changing tuple to a list and vice versa:
tpl = (1 , 13, 45)
lst = list(tpl)
lst.append(2)
retpl = tuple(lst)
print(tpl, lst,retpl)

# joining tuples 
tpl1 = (1,2,3)
tpl2 = (4,5,6)
tpl3 = tpl1 + tpl2
print(tpl3)

# deleting tuples 
del tpl3
# print(tpl3) THROWS A NAME ERROR CZ WE DEL TPL3 NO MORE TPL3


#### exercise tiiiime letsgooo  ###########
my_tpl = tuple()
brothers = ("mohamed","younes")
sisters =("rabia" , "montaha")
siblings = brothers + sisters
print(f"i have {len(siblings)} siblings")
family = ("mama","dad") + siblings
print(f"family is {family}")

(my_mom , my_dad , *my_siblings) = family #this is called unpacking a tuple, * is used to unpack it inside a sous-tuple
print(f"my mom is {my_mom}, my dad is {my_dad}, and my siblings are {my_siblings}")  

fruits = ("banana","orange","apple")
veggies = ("carrot","potato")
animals = ("chicken","eggs")
food_stuff = fruits + veggies + animals
food_stuff_lst = list(food_stuff)
print(f"{food_stuff} -> {food_stuff_lst}")
n = len(food_stuff_lst)
no_carrots = food_stuff_lst[:n//2] + food_stuff_lst[n//2 +1 :]
print(f"oh no, i have carrots allergie : my new foods are {no_carrots}")
del food_stuff
#print(f"{food_stuff}") now it gives NameError yay!

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"is Iceland a nordic country? {"Iceland" in nordic_countries}")