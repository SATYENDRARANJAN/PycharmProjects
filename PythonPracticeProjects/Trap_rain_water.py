from builtins import len, range, max, min


# Approach 1 : For each element find max element on left and find max element on right ;find their min and calculate storage are
# Time complexity = O(n^2)
# Space complexity = O(1)
def max_water_simple(arr, n):
    result =0
    max_left =0
    max_right=0
    for i in range(1,n-1):
        max_left = arr[i]
        for j in range(i):
            max_left = max(arr[j],max_left)

        max_right = arr[i]
        for j in range(i+1,n):
            max_right = max(arr[j],max_right)

        result += min(max_left,max_right) - arr[i]
    return result



# Here instead of finding max_left and max_right for each element , we create two arrays left[] and right[]
# that store max_left and max_right for each element in one traversal and then in another traversal , we find find storage at each element .
# Time complexity : O(n)
# Space complexity : O(n)
def max_water_memoized(arr, n):
    result =0
    left =[0]*n
    right =[0]*n

    for i in range(1,n-1):
        left[i] = max(left[i-1],arr[i-1])

    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1],arr[i+1])

    # just find  how much water can be stored at each step.
    for i in range(0,n):
        min_height = min(left[i],right[i]) -  arr[i]
        if (min_height >0 ):
            result += min_height
    return result


# Time complexity (0(n))
# Space complexity O(1)
def max_water(arr, n):
    result = 0
    left_max =0
    right_max =0
    lo = 0
    hi = n-1

    while(lo<hi):
        if arr[lo]<arr[hi]:
            if arr[lo] > left_max :
                left_max = arr[lo]
            else :
                result += left_max - arr[lo]
            lo +=1
        else:
            if arr[hi]>right_max:
                right_max = arr[hi]
            else:
                result += right_max -arr[hi]
            hi-=1
    return  result


# In this approach , basically the pointer keeps moving towards right and
# We start from i=1 , then find the next node such that node[i] > stack.peep()
# Time complexity O(n)
# Space complexity O(n)
def max_water_using_stack(arr, n):
    stack =[]
    result = 0
    for i in range(n):
        while(len(stack)!=0 and arr[i]>arr[stack[-1]]):
            top_el= arr[stack[-1]]
            stack.pop()
            if len(stack)==0:
                break
            dist = i-stack[-1]-1
            min_height = min(arr[stack[-1]],arr[i])-top_el
            result += dist * min_height
        stack.append(i)
    return result




if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)
    print(max_water(arr, n))
    print(max_water_using_stack(arr, n))
    print(max_water_simple(arr, n))
    print(max_water_memoized(arr, n))




# stack =  [ 0     ] , curr = 1   ==>
# stack =  [ 1     ] , curr = 1   ==>   Keep adding till stack.peep() > curr  and push current to stack and move curr to next i
# stack =  [ 1,0   ] , curr = 2   ==>   Now :=> stack.peep()=0 < curr ==> save top=0,pop , area+=min(2,stack.peep()=1)*1 =1*1  ==>
# stack =  [  1    ] , curr = 2   ==> pop 1 == add
# stack =  [  2    ] , curr = 1
# stack =  [ 2,1   ] , curr = 0
# stack =  [ 2,1,0 ] , curr = 1 ==> stack.peep()=0< curr ==> save top=0 , pop , area += min(2,stack.peep()=1) - top=0  *1 , find the distance = i - stack.peep() -1 , areasum += min(2,stack.peep()) * distance
# stack =  [ 2,1   ] , curr = 3 ==> stack.peep()=1< 3==> save top=1 , pop , dist = i - (stack.peep()=2) -1 * (min(ith , stack.peep()) - top)
# stack =  [ 2,    ] , curr = 1 ==> stack.peep()=2 , stack empty => break.
# stack =  [       ] , curr =
# stack =  [  2    ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =
# stack =  [       ] , curr =

