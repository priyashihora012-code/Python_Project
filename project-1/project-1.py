
print("Welcome to the Interactive Personal Data Collector!\n")


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_num = int(input("Please enter your favourite number: "))

birth_year = 2026 - age


print("\nThank you! Here is the information we collected:\n")

print("Name:", name, "(Type:", type(name), ", Memory Address:", id(name), ")")
print("Age:", age, "(Type:", type(age), ", Memory Address:", id(age), ")")
print("Height:", height, "(Type:", type(height), ", Memory Address:", id(height), ")")
print("Favourite Number:", fav_num, "(Type:", type(fav_num), ", Memory Address:", id(fav_num), ")")

print("\nYour birth year is approximately:", birth_year,
      "(based on your age of", age, ")")

print("\nThank you for using the Personal Data Collector. Goodbye!")

'''
output:

Welcome to the Interactive Personal Data Collector!

Please enter your name: priya
Please enter your age: 20
Please enter your height in meters: 153.5
Please enter your favourite number: 5

Thank you! Here is the information we collected:

Name: priya (Type: <class 'str'> , Memory Address: 1518218439264 )
Age: 20 (Type: <class 'int'> , Memory Address: 140731037370072 )
Height: 153.5 (Type: <class 'float'> , Memory Address: 1518229948432 )
Favourite Number: 5 (Type: <class 'int'> , Memory Address: 140731037369592 )

Your birth year is approximately: 2006 (based on your age of 20 )

Thank you for using the Personal Data Collector. Goodbye!

'''