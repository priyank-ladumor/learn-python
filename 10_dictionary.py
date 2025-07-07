a = {
    'a': 1,
    'b': 2,
    0: 'c'
}

b = [
    ('a', 1),
    ('b', 2)]

c = {} # empty dictionary

print(a.clear()) # clear the dictionary
 
# print(type(a), a) # return dict & mutable
# print(type(b), b) # return list & mutable

print(a.get('a')) # return the value & if not found return None
print(a.get('missing', 'Not Found'))  # Output: 'Not Found'
# print(a['a']) # return the value & if not found return error
# print(a.items()) # return the list of tuples
# print(a.keys()) # return the list of keys
# print(a.values()) # return the list of values

a.update({'c': 3, 0: 0}) # update the dictionary with key and if key is not present it will be added
# a['d'] = 4 # add new key
# a.pop('a') # remove key
# a.popitem() # remove last key
print(a)

for key, value in a.items():
    print(key, value)

dict1 = {'a': '13', 'b': '2'}
dict2 = {'a': '12', 'b': '2', 'c': '3'}

# for merge two dictionary
dict3 =  dict2 | dict1 # for merge dict2 to dict1 means dict1 will override dict2
dict3 =  dict1 | dict2 # for merge dict1 to dict2
print('dict3: ', dict3)