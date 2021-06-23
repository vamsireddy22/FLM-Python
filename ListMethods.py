# List Methods

'''
    # 1. append()
    # 2. clear()
    # 3. copy()
    # 4. count()
    # 5. extend()
    # 6. index()
    # 7. insert()
    # 8. pop()
    # 9. remove()
    # 10. reverse()
    # 11. sort()
'''

ls = [1,2,3,4,5]
# print(ls)

ls.append(6)
ls.append(7)
#print(ls)

# ls.clear()
# print(ls)

# print(ls)

# ls2 = ls.copy()
# print(ls2)

# ls.append(3)
# ls.append(4)
# ls.append(3)

# print(ls.count(4))

# [10,11,12,13]

ls1 = [10,11,12,13]
ls.extend(ls1)


# 1 2 3 4 5 6 7 7 8 1 2 3 4

# print(ls)
# print(ls.index(11,5,10))

# 1 2 3 4 5 6 7 10 11 12 13
# 0 1 2 3 4 5 6 7 8 9 10 11
# 1 2 3 4 5 6 7 15 10 11 12 13 

ls.insert(6,15)

# print(ls)

# ls.remove(15)

# print(ls)

# 13 12 11 10 15 7 6 5 4 3 2 1
# ls.reverse()
# print(ls)

newLs = [10,14,11,15,13,9,8,20]
# newLs.sort(reverse = True)
# print(newLs)

sortedLs = sorted(newLs)
print(sortedLs)

























