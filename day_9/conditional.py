a = -3
if a > 0 :
    print("positive")
elif a == 0 :
    print("null")
else :
    print("negative")

# in one line
print("positive") if a>=0 else print("negative")

## exerciiises ####
#print("you are old enough to drive") if int(input("how old are you?"))>=18 else print("you're a baby")
#age = int(input("how old are you?"))
#print(f"you are {age-20} years older than me") if age > 20 else print(f"you are {20-age} years younger than me")

#a = int(input("a = "))
#b = int(input("b = "))

#print(f"{a} is bigger than {b}") if a>=b else print(f"{b} is bigger than {a}")


def grading(score):
    grades = ("A","B","C","D","F")
    if score > 80 and score <= 100: 
        return grades[0]
    elif score > 70 and score <= 89:
        return grades[1]
    elif score > 60 and score <= 69:
        return grades[2]
    elif score > 50 and score <= 59:
        return grades[3]
    elif score >= 0 and score <= 49:
        return grades[4]
    else:
        return "what did you do to get this score?!"
print(grading(-86))

def seasonof(mounth):
    seasons = {
        "Autumn": ("September", "October","November"),
        "Winter": ("December", "January" , "February"),
        "Spring": ("March", "April" , "May"),
        "Summer": ("June", "July" , "August")
    } 
    mounth = mounth.capitalize()
    if mounth in seasons["Autumn"]:
        return "Autumn"
    elif mounth in seasons["Winter"]:
        return "Winter"
    elif mounth in seasons["Spring"]:
        return "Spring"
    elif mounth in seasons["Summer"]:
        return "Summer"
    else: 
        return "Thats not a mounth buddy"
print(seasonof("november"))

def doihavethefruit(fruit):
    fruits = ['banana', 'orange', 'mango', 'lemon']
    if fruit not in fruits:
        fruits.append(fruit)    
    else:
        print('That fruit already exist in the list')
    return fruits
print(doihavethefruit("melon"))

