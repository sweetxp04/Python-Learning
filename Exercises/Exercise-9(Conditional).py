# exercise 1
"""
age = int(input("Enter Your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")
"""
# exercise 2
"""your_ege = int(input("Enter your age: "))
my_age = 24
if my_age > your_ege:
    print(f"I am {my_age-your_ege} years older than you.")
elif my_age == your_ege:
    print("you and I are same age.")
else:
    print(f"You are {your_ege-my_age} years older than me.")"""

# Exercise 3
"""
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
if a is less b return a is smaller than b, else a is equal to b. Output:
```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
""""num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))
if num1 > num2:
    print(f"{num1} greater that {num2}")
else:
    print(f"{num2} greater that {num1}")"""
# Exercise 4
"""
Write a code which gives grade to students according to theirs scores:
        80-100, A
        70-89, B
        60-69, C
        50-59, D
        0-49, F
"""
""""mark = int(input("Enter your mark here: "))
if 80 <= mark <= 100:
    print("A")
elif 70 <= mark <= 79:
    print("B")
elif 60 <= mark <= 69:
    print("C")
elif 50 <= mark <= 59:
    print("D")
elif 0 <= mark <= 49:
    print("F")
else:
    print("Invalid mark.")"""

# Exercise 5
""""
Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
    June, July or August, the season is Summer
"""
"""Autumn = ["September", "October", "November"]
Winter = ["December", "January", "February"]
Spring = ["March", "April", "May"]
Summer = ["June", "July", "August"]
month = input("Enter month: ").title()
if month in Winter:
    print("The season is Winter.")
elif month in Autumn:
    print("The season is Autumn.")
elif month in Spring:
    print("The season is Spring.")
elif month in Summer:
    print("The season is Summer.")
else:
    print("Invalid Month.")"""

# Exercise 6
"""
The following list contains some fruits:
    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```
    If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
     If the fruit exists print('That fruit already exist in the list') 
"""
"""fruits = ['banana', 'orange', 'mango', 'lemon']
item = input("Enter fruits name here: ").lower()
if item in fruits:
    print("That fruit already exist in the list.")
else:
    fruits.append(item)
    print("The fruit added to the list.")
    print(fruits)"""


