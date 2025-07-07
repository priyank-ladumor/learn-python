
# class DemoClassMethod:
#     a = 1
#     @classmethod # for class method default value get
#     def class_method(cls):
#         print("This is a class method, {}".format(cls.a))
        
# c = DemoClassMethod()
# c.a = 2
# print('c.a: ', c.a)
# c.class_method()


# # property decorator and setter and getter
# # using property we can return func
# class Person:
#     def __init__(self, name):
#         self._name = name  # Protected attribute (_name) is used to back the property
#     @property
#     def name(self):
#         print("Getting name from Person")
#         return self._name
#     @name.setter
#     def name(self, value):
#         print("Setting name in Person")
#         if not value:
#             raise ValueError("Name cannot be empty.")
#         self._name = value
# class Employee(Person):
#     def __init__(self, name, employee_id):
#         super().__init__(name)  # Call the parent constructor
#         self._employee_id = employee_id
#     @property
#     def employee_id(self):
#         return self._employee_id
#     @employee_id.setter
#     def employee_id(self, value):
#         if not str(value).isdigit():
#             raise ValueError("Employee ID must be numeric.")
#         self._employee_id = value
# # using property decorator and setter we can get and set value without calling method (ex: e.name()) and set using e.name = "John Doe"
# e = Employee("John Doe", "12345")
# print(e.name)  # Output: John Doe
# e.name = "Jane Doe2"
# print('e.employee_id: ', e.employee_id)
# e.employee_id = "54321"
# print('e.employee_id: ', e.employee_id)
# print(e.name)  # Output: Jane Doe2


# operation overloading in python
# In Python, you can override the meaning of operators (like +, -, *, etc.) for your own classes using special methods like:
# | Operator | Method    |
# | -------- | --------- |
# | `+`      | `__add__` |
# | `-`      | `__sub__` |
# | `*`      | `__mul__` |
# | `==`     | `__eq__`  |

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
v = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v + v2
print(v3.x, v3.y) # 4 6
print(v3.__str__())
print(v3)
