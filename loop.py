# While loop

"""count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)"""

"""
count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break
"""

"""
count = 0
while count < 10:
    if count == 5:
        continue
    print(count)
    count += 1
"""
# For loop

"""
numbers = [0, 1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    print(number)

"""

"""language = "Pythhon"
for letter in language:
    print(letter)"""

"""language = "Python"
for i in range(len(language)):
    print(language[i])"""

"""person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)"""

# The Range Function
# lst = list(range(11))
# print(lst)
# st = set(range(2, 11))
# print(st)
# lst = list(range(0, 11, 2))
# print(lst)

# for number in range(11):
#     print(number)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)
