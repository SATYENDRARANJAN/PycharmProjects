# Convert list of tuple to list of list .
test_list = [(1, 2), (3, 4), (5, 6)]

res = [list(ele) for ele in test_list]
res = list(map(list,test_list))
print (res)


# convert list of string to list of tuples
test_list2 =['a,b','c,d','g,h']
test_list3 =['1,2','3,4','5,6']
res2 =  [tuple(ele.split(',')) for ele in test_list2]
res3 =  [tuple(map(int , ele.split(','))) for ele in test_list3]
print (res2)
print (res3)


# convert list of tuples into list
lt = [('Geeks', 2), ('For', 4), ('geek', '6')]
res4 = [item for t in lt for item in t ]
print (res4)