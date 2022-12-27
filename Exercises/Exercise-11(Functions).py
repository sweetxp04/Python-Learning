# Exercise-1
"""
Declare a function _add_two_numbers_.
 It takes two parameters and it returns a sum.
"""

"""def add_two_numbers(num_one, num_two):
    total = num_one + num_two
    return total


print(add_two_numbers(20, 30))"""

# Exercise-2
"""
Area of a circle is calculated as follows:
 area = π x r x r. 
Write a function that calculates _area_of_circle_.
"""

"""def area_of_circle(radius):
    area = 3.1416 * radius * radius
    return area


print(area_of_circle(5))"""
# Exercise-3
"""
Write a function called add_all_nums which takes arbitrary number of arguments and 
sums all the arguments. Check if all the list items are number types.
 If not do give a reasonable feedback.
"""

"""def add_all_nums(*nums):
    total = 0
    for num in nums:
        if str(num).isdigit():
            total += int(num)
        else:
            return "All the entity should be number"

    return total


print(add_all_nums(10, 20, 40))"""

# Exercise-4
"""
Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
"""

"""def convert_celsius_to_fahrenheit(celcius):
    f = (celcius * 9 / 5) + 32
    return f


print(convert_celsius_to_fahrenheit(33))"""

# Exercise-5
"""
Write a function called check-season, it takes a month parameter and
 returns the season: Autumn, Winter, Spring or Summer.
"""

"""def check_season(month):
    month = month.title()
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    if month in winter:
        print("The season is Winter.")
    elif month in autumn:
        print("The season is Autumn.")
    elif month in spring:
        print("The season is Spring.")
    elif month in summer:
        print("The season is Summer.")
    else:
        print("Invalid Month.")


check_season("july")"""
# Exercise-6
"""
Declare a function named print_list. It takes a list as a parameter and 
it prints out each element of the list.
"""

"""def print_list(lst):
    for item in lst:
        print(item)


lst = ['banana', 'orange', 'mango', 'lemon']
print_list(lst)"""

# Exercise-7
"""
Declare a function named reverse_list. It takes an array as a parameter and 
it returns the reverse of the array (use loops).
"""

"""def reverse_list(lst):
    rev_list = []
    for i in range(len(lst)):
        rev_list.append(lst[len(lst) - i - 1])
    return rev_list


lst = ['banana', 'orange', 'mango', 'lemon']
print(reverse_list(lst))"""

# Exercise-8
"""
Declare a function named capitalize_list_items.
 It takes a list as a parameter and it returns a capitalized list of items
"""

"""ef capitalize_list_items(lst):
    lst_cap = []
    for item in lst:
        lst_cap.append(item.capitalize())
    return lst_cap


lst = ['banana', 'orange', 'mango', 'lemon']
print(capitalize_list_items(lst))"""
# Exercise-9
"""
Declare a function named add_item. It takes a list and an item parameters.
 It returns a list with the item added at the end.
"""

"""def add_items(lst, item):
    lst.append(item)
    return lst


lst = ['banana', 'orange', 'mango', 'lemon']
print(add_items(lst, "date"))"""
# Exercise-10
"""
Declare a function named add_item. It takes a list and an item parameters.
 It returns a list with the item added at the end.
"""
# Exercise-11
"""
Declare a function named evens_and_odds . It takes a positive integer as parameter and
 it counts number of evens and odds in the number.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
"""


"""def evens_and_odds(num):
    even = 0
    odd = 0
    for i in range(num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("The number of odds are", odd)
    print("The number of evens are", even)


evens_and_odds(100)"""