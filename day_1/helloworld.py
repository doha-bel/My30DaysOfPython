from math import sqrt

############## TYPES ###############
# list is ordered like arrays, can contain a single type or diffrent types. the content can be changed



mylist = ['Banana', 10, False, 9.81]
# A Python dictionary object is an unordered collection of data in a key value pair format.
mydictionary  = {
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
# tuple is like an array and lists but it is unmutable: the content is fixed can't be changed
mytuple = ('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya')
# a set is unordered, holds oly unique values no redunduncy
myset = {2, 4, 3, 5,2,5}

# # Checking data types
# print(type(10))          # Int
# print(type(3.14))        # Float
# print(type(1 + 3j))      # Complex number
# print(type('Asabeneh'))  # String
# print(type([1, 2, 3]))   # List
# print(type({'name':'Asabeneh'})) # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Set
# print(type((9.8, 3.14, 2.7)))    # Tuple

string_data = "hello"
list_data = list(string_data)
print(list_data)  # Output: ['h', 'e', 'l', 'l', 'o']


my_set = {"q","e","a"}
link = ("l","ink")
list_link = list(link)
print("link as a set :",list_link)


p1 = (1,2)
p2 = (3,4)
def eculidiane_distance(p1,p2):
    return sqrt( abs(p1[0]**2 - p2[0]**2) + abs(p1[1]**2 - p2[1]**2) )

print(eculidiane_distance(p1,p2)) 

your_name = input("i can't rememer your name champion...")
print("AAH you are the hylian champion",your_name)

