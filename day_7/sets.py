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


# subset and superset 
things_id_eat = {"orange","Hylianshroom"}
print(f"are the things i'd eat a subset of food? {things_id_eat.issubset(foods)}")

# diffrence between two sets 
print(f"the diffrence between things id eat and foods is {foods.difference(things_id_eat)}")

# difference symmetrique : (A\B) ∪ (B\A)
print(f"the SYMMETRIQUE diffrence between things id eat and foods is {things_id_eat.symmetric_difference(foods)}")

# disjoint sets are sets that have no commun item : set1.isdisjoint(set2)


#### EXERCISES LETSGOOO ####

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"i have {len(it_companies)} company")
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Nintendo","Sony"])
print(it_companies)
it_companies.remove("Sony")
print(it_companies)

print(A.union(B))
print(B.union(A))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A,B

set_ages = set(age)
print(set_ages,len(set_ages),len(age))
"""
the diffrence between a string, list, tuple, and set:
a string is an array of charachters, can be changed, can be indexed
a list is a array of items or objects that can be changed and indexed, and you can add stuff to it
tuple cannot be changed once created, can be indexed tho
a set cannot be indexed cz there is no order, no item exists twice, although you treat it like a maths set
"""
sen = "I am a teacher and I love to inspire and teach people."
sen_set = set(sen)
print(sen_set) # return the unique charachters, for words :
unique_words = set(sen.split(" "))
print(len(unique_words)) # LETSGOOO I DIDNT GIVE UP 