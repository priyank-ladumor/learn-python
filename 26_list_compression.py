myList = [1, 3, 5, 6, 7]


# squaredList = []
# for item in myList:
#     squaredList.append(item * item)
    
squaredList = [x * x for x in myList]
print(squaredList)

n = 5
table = [x * n for x in range(1, 11)]
print('table: ', table)