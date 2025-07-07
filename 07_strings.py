a = "a"
b = 'b'
c = '''c'''
d = """abcdefghijklmnopqrstuvwxyz"""

piyu = 'piyu bhai'

e = len(d)

# f = d[1]
# f = d[-1]
# f = d[1:3]
# f = d[-4:-1]
# f = d[:3] # its means from 0 to 3
# f = d[1:] # its means from 1 to end
# f = d[::-1] # its means reverse
f = d[1:6:4] # its means from 1 to 6 with step 4 

g = d.upper()
# h = d.startswith('abc')
h = d.endswith('xyz')
i = piyu.capitalize()
j = piyu.title()

k = piyu.replace('bhai', 'sir')

l = "hello \nworld" # for new line
m = "hello \t world" # for tab
n = "hello \bworld" # for backspace
o = "hello \rworld" # for return
p = "hello \"ji\" world" # for double quotes

q = "hello \a world" # for alert bell

r = "hello\world" # for space

# name = input("Enter your name: ")
name = "piyu"
# s = "My name is {}".format(name)
s = f"My name is {name}"

t = "hey my friend".find('e') # its return index

u = ['1', '2', '3']
v = ','.join(u)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
print(t)
print(u)
print(v)