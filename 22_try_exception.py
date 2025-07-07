try:
    a = int(input('Enter a number: '))
    print(a)
except ValueError as v:
    print('ValueError:', v)
except Exception as e:
    print('Exception:', e)
else: # if try block does not raise any exception then else block will execute
    print('No exception')
finally: # finally block will always execute
    print('Finally block')
    

# def handle_user(user: dict):
#     try:
#         match user:
#             case {"name": name, "age": age}:
#                 if age < 0:
#                     raise ValueError("Age cannot be negative") # raise exception error
#                 elif age ==0:
#                     raise ZeroDivisionError("Age cannot be zero")
#                 print(f"User {name} is {age} years old.")
#             case _:
#                 print("Invalid user data")
#     except Exception as e:
#         print(e)
# handle_user({"age": 0, "name": "2OyH9@example.com"})
