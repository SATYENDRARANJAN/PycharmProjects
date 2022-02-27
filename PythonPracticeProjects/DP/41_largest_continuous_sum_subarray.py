# to find the max sum contiguous subarray
# traverse the arry .
# find the sum till nth no.
# if its lesser than the sum till (n-1)th no. -->  if its < 0 ==> set sum =0  else summ = sum +  a[n-1]

# TC =o(N)
from sys import maxsize

from builtins import range, len


def find_sum(a):
    max_sum_till_here =  -maxsize-1
    sum_till_here= [0]

    for i in range(1,len(a)):
        sum_till_here += a[i]
        if sum_till_here <0:
            sum_till_here =0
        if sum_till_here>max_sum_till_here:
            max_sum_till_here =sum_till_here
    print (max_sum_till_here)



if __name__ == "__main__":
    a =[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(find_sum(a))