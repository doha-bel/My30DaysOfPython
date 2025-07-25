"""
some boolean operations i didnt know:
- is - checks if two objects are the same object like : 1 is 1 
- is not - checks if two objects are not the same 
- in - checks if the thing is in a list or a tuple or whatever
- not in - checks if it is not in the list or whatever

"""



# print('1 is 1', 1 is 1)                   # True - because the data values are the same
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
# print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
# print('coding' in 'coding for all') # True - because coding for all has the word coding
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# my_age = 20
# my_height = 1.64
# mu_complex = (3+3j)
# base = int(input("enter base = "))
# height = int(input("enter height = "))
# print(f"the area of this triangle is {base * height * 0.5} m^2")

# side_a = int(input("side a ="))
# side_b = int(input("side b ="))
# side_c = int(input("side c ="))
# print(f"perimetre of this triangle is : {side_a + side_b + side_c} m")

def find_slope(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])
# print("slope is m = ", find_slope([1,0],[0,-2]))

def calc_y(x):
    return x**2 + 6*x + 9
# x = int(input("enter x value : "))
# print("y = ", calc_y(x))

# len1 = len("python")
# len2 = len("dragon")
# print("lets see , ",type(str(float(len("python")))))

def is_even(x):
    return x%2 == 0
# x = int(input("enter x value : "))
# print("lets see, ",x,is_even(x))

# print("lets see, ",7//3 == int(2.7))
# print("lets see, ",int(9.8) == 10)
# hours = int(input("hours :"))
# rate_per_hour = int(input("rate per hour : "))
# print(f"Your weekly earning is {hours*rate_per_hour}")

# age= int(input("your age :"))
# print(f"You lived for {age *31536000 } seconds")


