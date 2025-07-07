# type of inheritance
# 1. Single Inheritance # class derived from another class
# 2. Multiple Inheritance # class derived from more than one class
# 3. Multilevel Inheritance # class derived from a class derived from another class
# 4. Hierarchical Inheritance # class derived from more than one base class

# # Base class (Parent)
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound"
# # Derived class (Child)
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks"
# # Another Derived class
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} meows"
# # Creating objects
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# # Accessing methods
# print(dog.speak())  # Output: Buddy barks
# print(cat.speak())  # Output: Whiskers meows


# # 1 Single Inheritance
# # Base class
# class Animal:
#     def eat(self):
#         print("Animal eats")

# # Derived class
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Usage
# d = Dog()
# d.eat()
# d.bark()



# # 2 Multiple Inheritance
# # Base class 1
# class Flyable:
#     def fly(self):
#         print("Can fly")

# # Base class 2
# class Swimmable:
#     def swim(self):
#         print("Can swim")

# # Derived class
# class Duck(Flyable, Swimmable):
#     def quack(self):
#         print("Duck quacks")

# # Usage
# du = Duck()
# du.fly()
# du.swim()
# du.quack()


# # 3 Multilevel Inheritance
# # Base class
# class Animal:
#     def move(self):
#         print("Animal moves")

# # Derived class
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walks")

# # Further derived class
# class Human(Mammal):
#     def speak(self):
#         print("Human speaks")

# # Usage
# h = Human()
# h.move()
# h.walk()
# h.speak()

# # 4 Hierarchical Inheritance
# # Base class
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# # Derived class 1
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Derived class 2
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")

# # Usage
# dog = Dog()
# cat = Cat()

# dog.sound()
# dog.bark()

# cat.sound()
# cat.meow()


# # for super key class
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"Animal __init__ called for {self.name}")

#     def speak(self):
#         print(f"{self.name} makes a sound")
# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Call the __init__ of the base class using super()
#         super().__init__(name)
#         self.breed = breed
#         print(f"Dog __init__ called for {self.name}, breed: {self.breed}")

#     def speak(self):
#         super().speak()  # Optional: call base class method
#         print(f"{self.name} barks")

# d = Dog("Buddy", "Golden Retriever")
# d.speak()