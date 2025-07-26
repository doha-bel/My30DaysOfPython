# Strings only
first_name = 'Doha'
last_name = 'belkheir'
language = 'Python'
"""
formatting a string with % :
hadi % works like in C, it means it holds the place for something else to be put in there
and those things are added at the end after an % as a tuple.
"""
formated_string = 'I am %s %s. I study %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
tt = (radius, area)
formated_string = 'The area of circle with a radius %d is %.2f.' %tt # 2 refers the 2 significant digits after the point
print(formated_string)
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"


"""
we can also use this : {} and then add tha thing after in .format(tuple)
"""
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

"""
but for me, this has my heart : f"{}"
string interpolation, f-strings. 
Strings start with f and we can inject the data in their corresponding positions.
"""
formated_string = f'The area of a circle with a radius {radius} is {area:.2f}.'
print(formated_string)


############# Unpacking Characters:
word = "Hii! miku dayouu... miku dayouu"
# i want the i cz i clearly dont have it:
# _ , i = word
# print(i)

############## accessing charachter with index :
"""
from left to right we go 0,1,2,...n-1  and from right to left we go the negative -n....,-2,-1
"""
print(word[0],word[-1])
print(word.capitalize())
print(word.count("miku"))
print(word.endswith("dayouu"))
print(word.find("miku"))
print(word.rfind("miku"))
print(word.index("miku"))
print(word.rindex("miku"))
print(word.isalnum()) # space and the girls are not alpha num charachters. T-T
print(word.count("miku", 2, 10))

vocaloids = ["miku","teto","kaito","meiku","rin","lin","luka","hachi"]
my_vocaloids = ">".join(vocaloids) # imagine it puts something to 'join' the list 
print(my_vocaloids)

print(word.strip('miku dayouu'))

print(word.replace('miku','teto'))
print(word.split("!"))
print(word.split())  # this one without arguments splits words separated by a space

print(word.title()) # all words capitalized like a title 
print(word.capitalize()) # just the first word is capitalized

print(word.swapcase())
print(word.startswith("Hi"))


##### EXERCISEEEEEES ##########
stringy = "thirty" + "days" + "of" +"Python"
stringy2 = "Coding " + "For " + "All"
company = stringy2
print(company,len(company),company.upper().lower())
print(company[:6])
print(company.replace("Coding","Python"))
print(company.split(" ")) # splits words seprated by a space or whatever
faang = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(faang.split(","))
print(company.split()[0][0]+company.split()[1][0]+company.split()[2][0])

""" i think i hate dealing with strings in general, i don't want to memorise every built in function for them.
 can't they be normal arrays of charachters and that's all
very annoying! i hope strings die!
"""



