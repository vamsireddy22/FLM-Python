# Dictionary Methods

'''
    # keys()
    # values()
    # items()
    # get()
    # update()
    # copy()
    # clear()
'''


d = {
    'name':"Vamsi",
    'rollno':12345,
    'address':"TPT",
    'mobile':132535476
}

# print(d.keys())
# print(d.values())

# print(d.items())

# print(d.get('name'))
# print(d.get('age'))

d.update({'age':21})
d.update({'study':'B.Tech'})


d1 = d.copy()
print(d1)

d1.clear()
print(d1)










