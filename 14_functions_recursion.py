def avg(n1=None, n2=None, n3=None):
    a = n1 if n1 is not None else int(input('Enter a number 1: '))
    b = n2 if n2 is not None else int(input('Enter a number 2: '))
    c = n3 if n3 is not None else int(input('Enter a number 3: '))
    print((a + b + c) / 3)

avg(5, 6, 7)
# avg(5,9)


# there are two types of functions
# 1. built-in functions (predefined functions) ex: print(), input()
# 2. user-defined functions (custom functions) ex: avg

def capitalize(string = 'piyu bhai'):
    return string.upper()

print(capitalize('piyu'))
print(capitalize())


# recursion is a function that calls itself

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# n = int(input('Enter a number: '))
# print(factorial(n))

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

# n = int(input('Enter a number: '))
# print(sum(n))


def pattern(n):
    if n == 0:
        return
    print('*' * n)
    pattern(n - 1)

pattern(5)
