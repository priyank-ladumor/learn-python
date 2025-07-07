# # Without walrus:
# line = input("Enter something: ")
# while line != "quit":
#     print(f"You said: {line}")
#     line = input("Enter something: ")


# With walrus:
while (line := input("Enter something: ")) != "quit":
    print(f"You said: {line}")
