# Here we need to find the max sum of the increasing and then decreasing sequnce
# This problem is variation of LIS
# To write it recursively
# we need to calculate max sum of  asceding subseqence and descending subsequence .
# => ascending sum till ith + (descending sum from ith -ith)
# we create two arrays to store asc sum till ith and desc sum from ith
# ascending sum means sum of LONGEST INC SUBSEQNCE



def max_sum_till(a,i):
    if i ==0:
        # list.append(a[0])
        return a[0]
    j=0
    mxm_sum = 0
    max_ind = 0

    for j in range(i):
        if a[j] < a[i]:
            sum =  max_sum_till(a,j)
            # list = max_sum_till(a,j)[1
            if sum > mxm_sum:
                mxm_sum = sum
                max_ind = j
    # print (a[i] , mxm_sum)
    # list.append(a[max_ind])
    sum = a[i]+mxm_sum
    return sum


def max_sum_from(a,i,l):
    if i ==l:
        return 0
    if i == l-1:
        # print (list)
        return 0
    mxm_sum =0
    max_ind =0
    for j in range(i+1,l):
        if a[j] < a[i]:
            sum = a[j]+max_sum_from(a,j,l)
            if sum > mxm_sum:
                mxm_sum = sum
                max_ind = j
    # list.append(a[max_ind])
    return  mxm_sum


def find_max_sum_of_bitonic(a):
    i =0
    l = len(a)
    max_sum =0
    max_ind =0
    global list
    list =[]
    for i in range(l):
        sum1 = max_sum_till(a,i)
        sum2 = max_sum_from(a,i,l)
        # print(sum1,sum2)
        if max_sum < sum1 + sum2:
            max_sum = sum1 + sum2

    print(max_sum)



if __name__ == "__main__":
    a=[80, 60, 30, 40, 20, 10]
    # a=[12,1, 15, 51, 45, 33, 100, 12, 18, 9]
    find_max_sum_of_bitonic(a)
