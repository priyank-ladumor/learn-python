def greet():
    print("Hello")
    return "Hello"

def greet2():
    print("Hello2")
    return "Hello2"
    
if __name__ == "__main__":
    print("This module is being run directly")
    greet()
else:
    print("This module is being imported")