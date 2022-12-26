# Dictionary is nothing but key value pairs

# my_dict = {}  #blank dictionary
# print(type(my_dict))

# my_dict = {"Mahidur": "Burger", "Monmon": "Mutton", "Rahman": "Fish", "Sarker": {
#     "B": "Roti",
#     "L": "Rice",
#     "D": "Chicken"
# }, "Tanbir": "Junk Foor", "Shanto": "Dry Food"}


# print(my_dict)
# print(my_dict["Mahidur"])
# print(my_dict["Monmon"])
# print(my_dict["Sarker"]["B"])
# adding elements to dictionary
# print(my_dict)
# del my_dict["Shanto"]
# print(my_dict)

# d2 = my_dict.copy()
# del d2["Mahidur"]
# print(d2)
# print(my_dict)
# my_dict.update({"Moja": "Peyaju"})
# print(my_dict)
# print(my_dict.keys())
# print(type(my_dict.keys()))

person = {
    'first_name': 'Mahidur',
    'last_name': 'Rahman',
    'age': 250,
    'country': 'Bangladesh',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# print(len(person))
# print(person["country"])
# print(person["first_name"])
# print(person["skills"][4])
# print(person["address"]["zipcode"])

# print(person.get("first_name"))
# print(person.get("country"))
# print(person.get("skills")[0])
# print(person.get("sports"))
# print(person.get("address")["street"])

# person["job_title"] = "Instructor"
# person["skills"].append("HTML")
# print(person)

# print(person.items())

# keys = person.keys()
# print(keys)
#
# values = person.values()
# print(values)
