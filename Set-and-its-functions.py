# Creating a empty set
# st = {}
# st = set()
# print(type(st))
# print(st)

# Creating set with initial items
st = {"banana", "orange", "mango", "lemon"}
# length of the set
# print(len(st))

# accessing elements in the set
# print("Does set st contain banana? ", "banana" in st)
# print("banana" in st)

# adding elements
fruits = {"banana", "orange", "mango", "lemon"}
# fruits.add("lime")
# print(fruits)
# fruits.update(["mahidur", "item1", "item2", "item3"])
# print(fruits)
# vegetables = ("tomato", "potato", "cabbage", "Onion")
# fruits.update(vegetables)
# print(fruits)

# removing item from set
# fruits.remove("banana")
# print(fruits)
# fruits.pop()
# print(fruits)

# clearing a set
# fruits.clear()
# print(fruits)

# converting a list to set
# lst = ['item1', 'item2', 'item3', 'item4', 'item1']
# st = set(lst)
# print(st)
# fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
# st = set(fruits)
# print(st)

# Joining set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

