# def http_status(code: int) -> str:
#     match code:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Status"
# msg = http_status(2100)
# print('msg: ', msg)


# def process_point(point: tuple):
#     match point:
#         case (0, 0):
#             print("Origin")
#         case (0, y):
#             print(f"Y={y} axis")
#         case (x, 0):
#             print(f"X={x} axis")
#         case (x, y):
#             print(f"Point at ({x}, {y})")
#         case _:
#             print("Not a point")
# process_point((1, 1))


# def describe_number(x: int):
#     match x:
#         case x if x < 0:
#             print("Negative number")
#         case x if x == 0:
#             print("Zero")
#         case x if x > 0:
#             print("Positive number")
# describe_number(0)


# def analyze_list(lst: list):
#     match lst:
#         case []:
#             print("Empty list")
#         case [x]:
#             print(f"Single element: {x}")
#         case [x, y]:
#             print(f"Two elements: {x} and {y}")
#         case [x, *rest]:
#             print(f"First: {x}, rest: {rest}")
#         case _:
#             print("Unknown list")
# analyze_list([1, 2, 3]) 
# analyze_list([1, 2]) 
# analyze_list([]) 
# analyze_list([-1, 2, -3]) 

def handle_user(user: dict):
    try:
        match user:
            case {"name": name, "age": age}:
                print(f"User {name} is {age} years old.")
            case { "age": age}:
                print(f"User {name} is {age} years old.")
            case _:
                print("Invalid user data")
    except Exception as e:
        print(e)
handle_user({"name": "NI", "age": -30})
handle_user({ "email": "2OyH9@example.com"})
handle_user({"age": 0, "name": "2OyH9@example.com"})
handle_user({"age": 30, "email": "2OyH9@example.com"})