"""
the same def in algebra :unordered and unique elements
we can also find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
"""
st = set() # empty set
odds = {1,3,5,7,9}
len(odds)

##### ALEEEEEERT : We use loops to access items. NO INDEXING CZ IT IS NOT ORDERED, I GUESS!

print(f"is 7 odd? {7 in odds}") # to check if someone is a "member" in the set we use in membership operator

# we cannot change items in a set, but we can add items to it 
odds.add(11)
print(odds)
# we can add multiple items (in form of a list btw) with update 
odds.update([13,15,17,19])
print(odds)

# to remove item from a set :
# remove : 
odds.remove(1) #raises an error if the item is not found
odds.discard(2) # does not raise an error
popped = odds.pop() #removes a random item and returns it
print(odds,popped)

# to clear or empty a set 
odds.clear()
print(odds)
# to delete the set 
del odds


# Converting list <=> set 
fruits_lst = ["banana","apple","banana","orange"]
fruits_set = set(fruits_lst)
print(fruits_lst,fruits_set)
shrooms_set = {"Hylianshroom","rushroom","sunshroom"}
foods = fruits_set.union(shrooms_set) # or we can update the first set too 
print(foods)
yiga_treasures = {"rubies","banana","amber","weapons"}
print(f"i can eat from the yiga clan their {foods.intersection(yiga_treasures)}")


##### rani 7absa f super set w sub set !!!!