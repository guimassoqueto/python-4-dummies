## first understand the usage of generators

# simple list remain in memory
list_compr = [x for x in range(10)]
print(list_compr)

# generator list where each element is creates by demand whenever it is called
# this list reduce memory utilization
list_gener = (x for x in range(10))
print(list_gener)


print(next(list_gener))  # 0
print(next(list_gener))  # 1

for i in list_gener:
    print(i)  # will print i 2,3,4,5,6,7,8,9

list_gener.close()  # close the generator
