"""
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
"""

# creating a list : 
listy = []
listyy = list()
print(len(listyy),listyy )
#Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

fruits = ["apple", "Mighty banana", "Hydromelon", "Salmon"]
first,second,*rest = fruits # the * means that this variable holds a list too, or may i say a sublist? a cute pointer like thing
print(f"frst : {first}, second : {second}, and the rest : {rest}")
fruits[3] = "Hearty Salmon"
print("Hydromelon" in fruits)
fruits.append("Wild berry") # adding items at the end of the list 
print(fruits)
fruits.insert(2,"acron") #lst.insert(index, item)
fruits.insert(2,"acron") #lst.insert(index, item)

print(fruits)

fruits.remove("acron") # removes the first? instance of the item 
print(fruits) 

fruits.pop() # removes the last item if no index as an argument
print(fruits)
fruits.append("Wild berry")
# fruits.pop(1)
print(fruits)
# The del keyword removes the specified index and it can also be used to delete items within index range.
#  It can also delete the list completely
del fruits[0]
print(fruits)
fruits.insert(0,'Apple')
print(fruits)

fruits.clear() # now thw list is empty, no fruits for me :(
print(fruits)

# you can do many more to a list but i got bored
# copy, extend with another list or simply concatenate with +, find index of an item, reverse a list
# for sorting a list, maybe it sounds intresting.. 
ages = [1,22,13,34,5,6,20,142]
ages.sort(reverse = True)
print(ages) 
other_ages = [2,1,12,5,22,10,4,23]
print(sorted(other_ages)) # this doesnt modify the original list, it just gives it sorted, cool!
print(other_ages)


# ########## EXERSICES LETSGOOOO ##########
lst = []
races = ["hylians","birds","rocks","fishman","women"]
print(len(races))
print(races[0], races[len(races)//2], races[-1])
my_info = ["doha",20,164,False,"0674.."]

it_companies = ["facebook", "google","microsoft","amazon","apple","IBM","orcle"]
print(it_companies,len(it_companies))
# print(it_companies.count(item!!!)) count needs an item, it counts how many times that item exists in the list.

it_companies[1] = "Google"
print(it_companies)
it_companies[-1] = it_companies[-1].upper()
print(it_companies)
it_companies_joined = " > ".join(it_companies)
print(it_companies_joined)
print("facebook is it company? -> ","facebook" in it_companies)
print(it_companies.count("facebook")) # i used it to check if a certain company exists
it_companies.sort(reverse= True)
print(it_companies)
it_companies.remove("facebook")
print(it_companies)
it_companies.pop()
it_companies.clear()
print(it_companies)
del it_companies
# print(it_companies) -> name error cz it_companies no longer exists, hope this happens irl too :3

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack_ = front_end + back_end
fullstack = fullstack_.copy()
fullstack.insert(5,"python")
print(fullstack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages,ages[0],ages[-1])
def get_median(lst):
    if(len(lst)%2==0):
        return (lst[len(lst)//2] + lst[(len(lst)//2)+1])//2
    else:
        return lst[len(lst)//2]
print("median ",get_median(ages))
print("average ",sum(ages)//len(ages))
print("range ",ages[-1] - ages[0] )

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china , russia, usa , *scandic = countries
print(scandic)