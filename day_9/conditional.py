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
print("you are old enough to drive") if int(input("how old are you?"))>=18 else print("you're a baby")
age = int(input("how old are you?"))
print(f"you are {age-20} years older than me") if age > 20 else print(f"you are {20-age} years younger than me")

a = int(input("a = "))
b = int(input("b = "))

print(f"{a} is bigger than {b}") if a>=b else print(f"{b} is bigger than {a}")



