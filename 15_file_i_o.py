# file i/o use for data storage and data processing in python using our system or storage (hard disk, ram, etc.)

# types of file
# 1. text file
# 2. binary file

# modes
# 1. r (read)
# 2. w (write)
# 3. a (append)
# 4. r+ (read and write)
# 5. w+ (write and read)
# 6. a+ (append and read)
# 7. rb (read binary)
# 8. rt (read text)

# f = open('test.txt', 'w')
# f.write('hello world')
# f.close()

# f = open('test.txt', 'r')
# f = open('test.txt')
# # print(f.read()) # read whole file
# # print(f.readlines()) # read line by line and store in list
# # print(f.readline()) # read line by line 
# # print(f.readline()) # read line by line 
# f.close()

# f = open('test.txt', 'a') 
# f.write('\nhello world') # add new line and write
# f.close()

# f = open('test.txt', 'r+') # read and write
# print(f.read())
# f.write('\nhello world') # add new line and write
# f.close()

# f = open('test.txt', 'w+') # write and read
# f.write('\nhello world') 
# f.seek(0) # move pointer to start
# print(f.readlines()) 
# f.close()

# f = open('test.txt', 'a+') # append and read
# f.write('\nhello world') 
# f.seek(0) # move pointer to start
# print(f.readlines()) 
# f.close()

# # using with statement we don't need to close the file
# with open('test.txt', 'r') as f:
#     content = f.read()
#     if 'hello' in content:
#         print('yes')
#     else:
#         print('no')

# def generateTable(n):
#     with open('table.txt', 'w') as f:
#         for i in range(1, 11):
#             f.write(f'{n} * {i} = {n * i}\n')

# n = int(input('Enter a number: '))
# generateTable(n)

# import os
# with open('old.txt', 'r') as f:
#     content = f.read()
# with open('new.txt', 'w') as f1:
#     f1.write(content)
# os.remove('old.txt')

# multi file open using with
with (open('old.txt', 'r') as f, open('new.txt', 'w') as f1):
# with open('old.txt', 'r') as f, open('new.txt', 'w') as f1:
    content = f.read()
    f1.write(content)
