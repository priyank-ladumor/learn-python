a = set()  # Correct way to create an empty set
c = {}     # This actually creates an empty dictionary, not a set

# on set there is no indexing or slicing and there is no order and it is mutable

# if u want to use immutable set then use frozenset
f = frozenset({1, 2, 3}) 
# f.add(4)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'
print('f: ', f)

# s = {7, 1, 5, 3, 3, 6, '7'}  # Duplicates (like 3) are removed
# print(s)  # Output: {1, 3, 5, 6, 7}

s = {7, '7', 7.0}  # Duplicates (like 7) are removed
print(s)  # Output: {7, '7'} # if value is same then ignored type 

# list can not be used on set but tuple can be used
s = {7, '7', (1, 2, 3)}  # Duplicates (like 7) are removed
print(s)  # Output: {7, '7', (1, 2, 3)}

a = [1, 2, 3, 4, 5]
s = set(a)
print(a)
print(s) # return unique values only using set

s = {1, 2, 3}
s.add(4) 
print(s)  # Output: {1, 2, 3, 4}

s = {1, 2}
s.update([3, 4], (5, 6), {7})  # Adds elements from multiple iterables
print(s)  # Output: {1, 2, 3, 4, 5, 6}

s = {1, 2, 3}
s.discard(2)
s.discard(5)  # No error
print(s)  # Output: {1, 3}


s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}
# s.remove(5) would raise KeyError


s = {10, 20, 30}
elem = s.pop()
print(elem)  # Output: One of the elements
print(s)     # Remaining set Output: {20, 30}


s = {1, 2, 3}
s.clear()
print(s)  # Output: set()

s1 = {1, 2, 3}
s2 = s1.copy()
s2.add(4)
print(s1)  # Output: {1, 2, 3}
print(s2)  # Output: {1, 2, 3, 4}


# 🔄 Set Operations

a = {1, 2}
b = {2, 3}
print(a.union(b))     # {1, 2, 3}
print(a | b)          # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
print(a & b)              # {2, 3}

a = {5, 6, 7}
b = {6, 8, 9}
print(a.difference(b))    # {5, 7}
print(a - b)              # {5, 7}

c = {10, 11, 12}
d = {12, 13, 14}
print(c.difference(d))    # {10, 11}
print(c - d)              # {10, 11}

a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))  # {1, 4}
print(a ^ b)                      # {1, 4}

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True

a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # True

a = {1, 2}
b = {1, 2, 3}
print(a.isdisjoint(b))  # False

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True


