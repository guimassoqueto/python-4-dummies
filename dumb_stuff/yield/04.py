# Using the getsizeof you can know how memory optimized the usage of an generator can be

from sys import getsizeof

one_million = 10**6

list_compr = [x for x in range(one_million)]
print(getsizeof(list_compr))  # bytes used by list_compr: 8448728

list_gener = (x for x in range(one_million))
print(getsizeof(list_gener))  # bytes used by list_gener: 200
