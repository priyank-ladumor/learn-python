hey = 'poi', 1, True, 1

hey2 = ('p', False, 1, 3.0, [], 1)

# tuples can not change (immutable)
print(type(hey))
print(hey2)
print(hey.index('poi')) # for which index is 'poi'
print(hey2.count(1)) # for how many times 1 is in the tuple
print(1 in hey) # check if 1 is in the tuple
print(hey[0:2]) # print from 0 to 2
print(hey + hey2) # concatenate
print(hey * 3) # repeat
print(len(hey))