# Sanchit Baveja09:15
#  Create the function l_cache(str_arr) which takes the list of strings (any fruits) stored in str_arr.
# Output will be some elements of str_arr, called cache_fruits that can hold upto 4 strings
#
# Example
#
# Input = ["APPLE", "MANGO", "GUAVA","APPLE", "KIWI", "BANANA"], then the following steps are taken:
#
# "APPLE" does not exist in the cache_fruits , so cache_fruits=["APPLE"]
# "MANGO" does not exist in the cache_fruits, so cache_fruits= ["APPLE", "MANGO"].
# "GUAVA", does not exist in the cache_fruits,
# "GUAVA", does not exist in the cache_fruits, so cache_fruits= ["APPLE", "MANGO", "GUAVA"].
#  New input is "APPLE"  but it exists in the cache_fruits already so it is last element
#  ["MANGO", "GUAVA", "APPLE"].
# "KIWI",  does not exist in the cache_fruits, so cache_fruits= ["MANGO", "GUAVA", "APPLE","KIWI"].
# "BANANA" does not exist in the cache_fruits, but the number of elements can be 4 only, evict "MANGO" as it is not used.
#  cache_fruits= ["GUAVA","APPLE","KIWI","BANANA"]
#
# OTHER EXAMPLES
#
# Input: st
#
# Least recently used - evicted



def pop_to_top(a, item):
    stack =[]
    i = len(a)-1
    while (i>=0 and a[i]!=item ):
        stack.push(a[i])
        a[i]=None
        i = i-1
    if i>=0:
        #item found
        temp= a[i]
    k = len(stack)-1
    while(k >=0):
        a[i]=stack[k]
        i+=1;
        k-=1;
    a[i]=temp



def dequeue(a):
    i =0
    stack =[]
    while (i>0):
        stack.push(a[i])
        a[i]=None
        i-=1
    k = len(stack)-1
    while(k >=0):
        a[i]=stack[k]
        k-=1;


def queue(a,item):
    a[-1]=item

def lr_cache(a , item ):
    if item in a:
        # pop to top using stack
        pop_to_top(a, item )
    else:
        # last itme evicted
        # new one inserted
        a.pop()
        queue(a,item)





if __name__ == "__main__":
    a =[None] * 4
    lr_cache(a , 'MANGO' )
    lr_cache(a , 'KIWI' )
    lr_cache(a , 'MANGO' )
    print(a)
