# Exercise- 1
"""
Filter only negative and zero in the list using list comprehension
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [i for i in numbers if i <= 0]
print(numbers)

# Exercise- 2
"""
Flatten the following list of lists of lists to a one dimensional list :
   list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
"""
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [num for row in list_of_lists for num in row for num in num]
print(flatten_list)
# Exercise- 3
"""
Using list comprehension create the following list of tuples:
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
"""
tpl_list = [(i, 1, i, i * i, i * i * i, i * i * i * i, i * i * i * i * i) for i in range(11)]
print(tpl_list)
# Exercise- 4
"""
Flatten the following list of lists of lists to a one dimensional list :
   list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[sub2[0].upper(), sub2[1].upper()] for sub in countries for sub2 in sub]
countries = [x for sub in countries for x in sub]
keys = ["country", "city"]
x = [{keys[0]: countries[idx], keys[1]: countries[idx + 1]} for idx in range(0, len(countries), 2)]
print(x)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [i for i in names for i in i for i in i]
name = [names[i] + " " + names[i + 1] for i in range(0, len(names), 2)]
print(name)
