from functools import reduce

# Example: Add Two Numbers
add = lambda x, y: x + y
print(add(3, 4))

# Example: Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Sorting with Lambda
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
words.sort(key=lambda name: len(name))
print(words)

# Mapping a List
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers)) # return list and map using lambda or any func and list
print(doubled)

# Reduce a List
numbers = [1, 2, 3, 4, 5]

def sunFun(x, y):
    return x + y
sum = reduce(lambda x, y: x + y, numbers) # it reduce the list like 1+2 then 3+3 then 6+4 then 10+5 and return 15 
sum = reduce(sunFun, numbers)
print(sum)