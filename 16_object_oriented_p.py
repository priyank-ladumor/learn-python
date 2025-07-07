from random import randint

# OBJECT ORIENTED PROGRAMMING (OOP) MEANS CREATING OBJECTS FROM CLASSES AND USING THEIR ATTRIBUTES AND METHODS TO PERFORM ACTIONS 
# CLASS - IS A TEMPLATE FOR CREATING OBJECTS OR BLUEPRINT OF OBJECTS
# OBJECT - IS AN INSTANCE OF A CLASS

class Person: # Noun -> Person
    # this __any-name__ method is a dunder / magic method which is a automatically called method
    def __init__(self, name, age): # Constructor -> __init__ # Class Attributes -> name, age # self is a reference to the current object
        self.name = name
        self.age = age
        
    def introduce(self): # Verb -> introduce
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
        
person1 = Person("Priyank", 20) # instance / Object -> person1
person1.introduce()
print('person1.age: ', person1.age)

person1.age = 22 # instance / object attributes
print('person1.age: ', person1.age)


class NormalClass:
    hello = 'Hello'
    world = 'World'
    
    def getInfo(self, otherPassVar = None):
        print(f'{self.hello} {self.world} {otherPassVar}')
        
    @staticmethod
    def printMSG():
        print('This is a static method')
    
normal = NormalClass()
normal.getInfo('otherPassVar')
normal.printMSG()

# print('normal.hello: ', normal.hello)
# print('normal.world: ', normal.world)

class Demo:
    a = 1
    
o = Demo()
print('o.a1: ', o.a) # instance attributes show default value
o.a = 2
print('o.a2:', o.a) # instance attributes show updated value
print(Demo.a) # class attributes show default value