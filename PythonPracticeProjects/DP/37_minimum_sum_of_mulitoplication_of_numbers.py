# In this porblem , we need to find min sum of multiplication of n numbers
#  a = { 40 , 60 , 20} => (A1A2)A3
# m1 = {0,(2400 ,0),20 }
# m2 = {0 ,(2400 ,0), (2400 +0*20 , 20) =  {0 ,(2400 ,0), (2400  , 20)

#  a = { 40 , 60 , 20} => A1(A2A3)
# m1 = {40  ,(1200 ,80)}
# m2 = {(1200 +  80*40 ,20),( 1200, 80)} = {(4400 ,20)(1200,80)}

#  this problem is basically a variation of matrix chain multiplication problem .
# recursive
import sys


def count(a,i,j):
    if i ==j :
        return 0

    min_c = sys.maxsize
    for k in range(i , j):
        c = a[i-1] * a[k] * a[j] + count(a,i,k) + count(a, k+1,j)
        if c < min_c:
            min_c = c
    return min_c


if __name__ == "__main__" :
    global a
    a = [40 , 60 , 20]
    a = [1, 2, 3, 4, 3];

    n = len(a)
    print(count(a,1,n-1))