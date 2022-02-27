# In this problem we need to place tiles one above the other , in ascending order .
# Tiles are of size 1 to m
# Each tile can be used k times .

#
# def ways(h, m,k):
#     if h ==0 or m ==0 or k ==0:
#         return 0
#     totalways =0
#     for i in range(k+1):
#         if i>h and i>m and i>k:
#             totalways += ways(h-i,m-i,k-i)
#     return totalways
from builtins import range


def ways(h, m,k):
    print(h,m,k)
    totalways =0

    if h==0: return 1

    if h>m*k:
        return 0
    if (h == 1):
        return m;

    if (m == 1):
        return 1 if h <= k else 0;
    # if h<0:
    #     totalways= 0
    #     return 0
    # if h ==0:
    #     print("returning 1")
    #     totalways= 1
    #
    # if m ==0:
    #     totalways= 0
    # if k ==0:
    #     totalways+= ways(h,m-1,k1)
    for i in range(0,k+1):
        totalways += ways(h-i,m-1,k)
    print("******")
    return totalways

def ways1(h, m,k):
    print(h,m,k)
    totalways =0
    if h==0: return 1
    if h>m*k:
        return 0
    if (h == 1):
        return m;
    if (m == 1):
        return 1 if h <= k else 0;
    for i in range(0,k+1):
        totalways += ways(h-i,m-1,k)
    print("******")
    return totalways

k1=2
n, m, k = 3, 3, 2
if __name__=="__main__":
    print(ways(n,m,k))