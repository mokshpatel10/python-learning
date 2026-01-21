my_info = {
    "name" : "Moksh",
    "age" : 6 ,
    "major": "Comp sci"
}
#------------------------------------------------------------------------------------------------------------------------------------
print(my_info)

weekly_temps = dict(
    Monday=26,
    Tuesday=32,
    Wednesday=25,
    Thursday=28,
    Friday=27,
    Saturday=30,
    Sunday=31
)
#------------------------------------------------------------------------------------------------------------------------------------

print(weekly_temps)

pet = {"name": "Buddy", "type": "dog", "age": 3}

print(pet["name"])
print(pet["age"])

print(pet.get("color", "unknown"))
#------------------------------------------------------------------------------------------------------------------------------------

grades = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 58
}

student_name = "Charlie"

grade = grades.get(student_name)

if grade is None:
    print("Student not found.")
elif grade >= 60:
    print(f"{student_name} passed the course with {grade}.")
else:
    print(f"{student_name} failed the course with {grade}.")

#------------------------------------------------------------------------------------------------------------------------------------

products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}

print(products.get())

#------------------------------------------------------------------------------------------------------------------------------------

inventory = {}

inventory["apples"] = 10
inventory["mangoes"] = 12
inventory["bananas"]=13






