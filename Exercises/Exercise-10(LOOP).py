# Exercise-1
"""
Iterate 0 to 10 using for loop, do the same using while loop
"""
"""count = 0
while count <= 10:
    print(count)
    count += 1"""
# Exercise-2
"""
Iterate 10 to 0 using for loop, do the same using while loop.
"""
"""count = 10
while count >=0:
    print(count)
    count -= 1"""
# Exercise-3
"""
 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
     #
     ##
     ###
     ####
     #####
     ######
     #######
"""
"""for i in range(1, 8):
    print("#" * i)"""
# Exercise-4
"""
Use nested loops to create the following:
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
"""
"""for i in range(0, 8):
    for j in range(0, 8):
        print("#", end="")
    print("")"""

# Exercise-5
"""
Print the following pattern:
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
"""
"""for i in range(0, 11):
    print(f"{i} * {i} = {i*i}")"""
# Exercise-6
"""
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask']
 using a for loop and print out the items.
"""
"""skills = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for skill in skills:
    print(skill)"""

# Exercise-7
"""
Use for loop to iterate from 0 to 100 and print only even numbers
"""
"""for n in range(0, 101, 2):
    print(n)"""

# Exercise-8
"""
Use for loop to iterate from 0 to 100 and print only odd numbers
"""
"""for n in range(1, 101, 2):
    print(n)"""

# Exercise-9
"""
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
   The sum of all numbers is 5050.
"""
"""total = 0
for n in range(1, 101):
    total = total + n
print("sum = ", total)"""

# Exercise-10
"""
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    The sum of all evens is 2550. And the sum of all odds is 2500.
"""
"""sum_even = 0
sum_odd = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"sum of all evens is {sum_even} and sum of all odds is {sum_odd}")"""

# Exercise-11
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
"""for country in countries:
    if country.startswith("B"):
        print(country)"""

# Exercise- 12
""""
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
"""

"""lst = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(lst)):
    print(lst[len(lst)-i-1])"""


