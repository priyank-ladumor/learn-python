a = 1
# if elif else ladder

if(a == 2):
    print('a is 2') # given space is important for indentation means you are on if block
elif(a == 1):
    print('a is 1')
else:
    print('a is not 2 but {}'.format(a))
    
# ternary operator
print('a is 2') if a == 2 else print('a is not 2 but {}'.format(a))

a1 = int(input('Enter a number: '))

if(a1 % 2 == 0 and (a1 > 0 or a1 < 100) and a1 < 100):
    print('a1 is even')
elif(a1 > 100):
    print('a1 is greater than 100')
else:
    print('a1 is odd')