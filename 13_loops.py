# for i in range(1, 11):
#     print(i) # 1 2 3 4 5 6 7 8 9 10

# for i in range(1, 11, 2):
#     print(i) # 1 3 5 7 9

# for i in range(10, 0, -1):
#     print(i) # 10 9 8 7 6 5 4 3 2 1
    
# i = 1
# while i <= 10: # if condition is true then it will run the loop but if we didn't give condition or change the condition then it will run infinite loop
#     print(i) # 1 2 3 4 5 6 7 8 9 10
#     i += 1
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list
m = (1,5,6,9,10) # tuple
o = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5} # dictionary
a = [1, {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}, 3, 4, 5, 6, 7, 8, 9, 10] # list
s = 'string' # string

# for i in l:
#     print(i) # 1 2 3 4 5 6 7 8 9 10
    
# for i in m:
#     print(i) # 1 5 6 9 10
    
# for key, value in o.items():
#     print(key, value) 
#     # a 1
#     # b 2
#     # c 3
#     # d 4
#     # e 5

# for i in o:
#     print(i)
#     # a
#     # b
#     # c
#     # d
#     # e

# for q in a:
#     print(q, type(q))
#     # 1 <class 'int'>
#     # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} <class 'dict'>
#     # 3 <class 'int'>
#     # 4 <class 'int'>
#     # 5 <class 'int'>
#     # 6 <class 'int'>
#     # 7 <class 'int'>
#     # 8 <class 'int'>
#     # 9 <class 'int'>
#     # 10 <class 'int'>

# for i in s:
#     print(i) # s t r i n g

for i in range(5):
    pass # it does nothing but it is required

for i in range(3):
    if(i == 1):
        print('continue or break')
        # continue # it will skip the incoming logics and continue the loop 
        # break # it will break the loop
    print(i)
    # 0
    # 1
    # 2
        
else:
    print('done') # when condition is false then it will run for once
    # done
    
star = '*'
n = int(input('Enter a number: '))
# for i in range(1, n + 1):
#     print(' '  * (n - i), end='') # print spaces and end='' will not print new line
#     print(star * (2 * i - 1), end='') # print stars
#     print('\n') # print new line

# for i in range(1, n + 1):
#     if(i == 1 or i == n): # if i is 1 or i is n then print stars
#          print(star * n, end='')
#     else: # if i is not 1 or i is not n then print spaces
#         print(star, end='')
#         print(' ' * (n - 2), end='')
#         print(star, end='')
#     print('\n')
    
for i in range(1, 11):
    print(f"{n} x {11 - i } = {i * n}")