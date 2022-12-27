
dog = {"name": "Doggy",
       "color": "Red",
       "legs": 4,
       "breed": True,
       "age": 5}

student = {
    "first_name": "Mahidur",
    "last_name": "Rahman",
    "gender": "Male",
    "age": 24,
    "marital_status": False,
    "skills": ['python', 'java', 'HTML', 'CSS', 'Javascript'],
    "country": "Bangladesh",
    "city": "Dhaka",
    "address": {
        "street": "space street",
        "zipcode": "262645"
    }
}

print(len(student))
print(student["skills"])
print(type(student["skills"]))
student["skills"].append("C++")
student["skills"].append("Jquery")
print(student["skills"])

keys = list(student.keys())
# values = student.values()
print(keys)
# print(values)

# del student["city"]
# print(student)
#
# del dog




