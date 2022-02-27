import collections

c1 =[12,3,4,5,6]
c2 =[4,4,5,78,3]


tup  = ("hi", {'1':"Python"}, 2)
tup[1]['1']='h'
print(tup[1]['1'])
print (tup)

# dict ={{1}:"a"}
dict ={frozenset({1}):"a"}
print ("dict  = ",dict)


t=([5,6],12)
print(t)
tup =('a','b','c')


class Details:
    age=11
    name='t'

d=Details()
print(getattr(d,"age"))
# print(getatttattr(d,"class"))

# globals() function return the dictionary of current global symbol table.
numList = [4, 5, 6,9,9]
strList = ['four', 'five', 'six','h']
strList2 = ['four', 'five', 'six','h']

# No iterables are passed
result = zip(numList,strList,strList2)

# Converting itertor to list
resultList = list(result)
print("resultList : ",resultList)



from collections import defaultdict
number = defaultdict(int)
number['one'] = 1
number['two'] = 2
number['three'] = "three"
print(number['three'])
print(number['two'])
#
# print(collections.Counter(c1)==collections.Counter(c2))
#
# #Reduce and map function . The map() function accepts a function and Python iterable object (list, tuple, string, etc)
# # as an arguments and returns a map object.
# # The function implements to each element of the list and returns an iterator as a result.
# import functools
#
# list1 = [10, 20, 30, 40, 50]
# list2 = [10, 20, 30, 50, 40, 60, 70]
# list3 = [10, 20, 30, 40, 50]
#
# if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, list1, list2), True):
#     print("The list1 and list2 are the same")
# else:
#     print("The list1 and list2 are not the same")
#
# if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, list1, list3), True):
#     print("The list1 and list3 are the same")
# else:
#     print("The list1 and list3 are not the same")
#
#
