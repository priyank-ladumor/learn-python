a = 89

def fun():
    global a
    a = 10
    print(a)

fun()
print(a)